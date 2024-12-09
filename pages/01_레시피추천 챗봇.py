from utils.mo import *
from langchain_core.output_parsers import StrOutputParser

from utils.make_user import User
from utils.pre_chain import *
from utils.findvector import *
from utils.webloader import *
# from utils.loader import *

# st.set_page_config(layout='centered')


user1 = User()


col1,col2 = st.columns([0.5,4])
with col2:
    st.header('알러지 프리 레시피 마법사️',divider='red')
with col1:
    st.image('image/iOS 이미지2.jpg',width=70)

with st.container(height=100):
    st.write('''
            🧙‍♂️ 알레르기명과 요리명을 작성하시면 알레르기 성분을 제외한 레시피를 알려드립니다.  
        ''')
    st.caption('ex) 돼지고기 알레르기가 있는데 카레요리 알려줘 / 우유,대두,계란 알레르기가 있는데 빵을 먹고싶어')


# chat 히스토리를 초기화
if 'messages' not in st.session_state:
    st.session_state.messages = []


# 히스토리로부터 들어있는 메세지를 출력
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])


#####################################################################################################
if query := st.chat_input("알레르기명과 요리명을 입력하세요."):
    with st.chat_message('user'):
        st.markdown(query)
        st.session_state.messages.append({'role': 'user', 'content': query})
# query = '우유,대두,계란 알레르기가 있는데 빵을 먹고싶어'
# query2 = '소고기 알레르기가 있는데 스테이크를 먹고싶어'
# query3 = '돼지고기 알레르기 있는데 고기요리 알려줘'
#####################################################################################################

    # start1 = time.time()

    # e-----------------------------------------------------------------------------------------------------------


    llm, llm4, prompt2, prompt3, prompt4, prompt__0 = makemodel()

    # 일대일 알레르기,코드 매핑
    # oto_dict = oto_data('data/식품_코드_일대일매칭.csv')

    ans2 = """{'name':’’’insert here’’’,'ingredients':’’’insert here’’’,'recipe':[’’’insert here’’’]}"""
    ans3 = """{'allergy':'''insert here''','food':'''insert here'''}"""


    def format_docs(docs):
        return '\n\n'.join([d.page_content for d in docs])


    model_parser = llm | StrOutputParser()
    model_parser4 = llm4 | StrOutputParser()

    # Chain
    chain3 = (prompt3
              | model_parser4)
    al_food_json = chain3.invoke(
        {'question': query, 'prev_allergy': user1.allergies, 'prev_food': user1.user_food, 'ans3': ans3})
    # st.write(al_food_json)
    al_food_dict = ast.literal_eval(al_food_json)

    # '조개류, 고등어' 인경우 공백이 문제가되므로 공백도 제거해준다
    if type(al_food_dict['allergy']) == list:
        # 이 코드를 str일때도 해주면 '돼','지','고','기' 같은 형태가 나와서 분리해줌
        allergys = [a.strip(' ') for a in ','.join(al_food_dict['allergy']).split(',')]
    elif type(al_food_dict['allergy']) == str:
        allergys = [a.strip(' ') for a in al_food_dict['allergy'].split(',')]

    al_code = []


    for allergy in allergys:
        for a, b in st.session_state.oto.items():
            if b == allergy:
                al_code.append(a)
                break


    # st.write(f'allergys:{allergys}')
    # st.write(f'al_code:{al_code}')
    user_food = al_food_dict['food']
    # st.write(f'사용자 입력 음식: {user_food}')

    user1.update(allergys, user_food)
    # st.write('벡터스토어에서 가져오는중...')

    # 벡터스토어에서 가저오기
    # s-----------------------------------------------------------------------------------------------------------

    context = find(st.session_state.retriever, user_food)

    # e-----------------------------------------------------------------------------------------------------------


    # st.write('검색 완료...!')
    recipe_num, url_num, cross_message, warning_message = CrossAndWarn(st.session_state.ingredient,st.session_state.raw_material,
                                                                       st.session_state.processed_food, st.session_state.recipe, st.session_state.cross,
                                                                       user_food, context, al_code)

    # 해당하는 음식이 없을 경우
    if recipe_num == -1:
        st.write('죄송합니다. 만개의 레시피에는 존재하지 않는 레시피입니다. GPT 3.5를 사용해서 레시피 추천해드릴께요.')
        chain__0 = (prompt__0
                    | model_parser)
        ex_food = chain__0.invoke({'allergy': allergys, 'user_food': user_food})

        result = st.write_stream(response_generator(ex_food))
        st.session_state.messages.append({'role': 'assistant', 'content': result})

    else:
        site = 'https://www.10000recipe.com/recipe/' + f'{url_num}'
        site_document = webload(site)

        chain2 = (prompt2
                  | model_parser
                  )

        response_temp = chain2.invoke({'site_document': site_document, 'ans2': ans2})
        response = ast.literal_eval(response_temp)

        # end1 = time.time()
        # st.write(f"답변 시간 : {end1 - start1:.5f} sec")

        with st.chat_message('assistant'):
            assistant_message = f"""요리제목: {response['name']}\n\n재료: {response['ingredients']}\n\n레시피:\n"""
            for i, re in enumerate(response['recipe']):
                assistant_message += f'\n  {'-'} {re}\n'

            # 교차반응 얘기해주기

            c, cross_comment_li, warn_comment_li = replaceCode(st.session_state.ing_name, recipe_num, st.session_state.oto, cross_message,
                                                               warning_message, al_code)

            if (cross_comment_li or warn_comment_li):
                assistant_message += f'\n※주의사항\n'
                if cross_comment_li:
                    assistant_message += f'\n사용자의 알레르기식품({c})은\n'
                    for c_key, c_val in cross_comment_li.items():
                        assistant_message += f'\n{c_key}({c_val}함유) 와(과) 교차반응을 일으킬 수 있습니다!\n'

                if warn_comment_li:
                    for ke, va in warn_comment_li.items():
                        assistant_message += f'\n가공식품 {ke}에 {va}가 함유 되있습니다!\n'

            result = st.write_stream(response_generator(assistant_message))
            st.session_state.messages.append({'role': 'assistant', 'content': result})

            if cross_comment_li:
                cross_reaction_info = '''\n📌교차반응이란?\n
                                        \n알레르기 교차반응은 신체의 면역체계가 어떠한 물질(예: 돼지고기)에 들어 있는 단백질을 다른 물질(예: 타과일)
                                        에 들어 있는 단백질과 유사하다고 인식하면서 발생합니다. 환자가 실제로 그 중 하나와 접촉하면, 그것이 알레르기 유발 단백질이 맞는지에 관계없이 
                                        면역체계는 같은 방식으로 반응할 수 있으며  경우에 따라 알레르기 증상을 유발할 수도 있습니다.\n'''
                st.caption(cross_reaction_info)


            image_urls = st.session_state.image[st.session_state.image['일련번호'] == recipe_num]['이미지'].tolist()


            # 이미지 없을때 예외처리
            if not image_urls:
                st.caption("레시피 이미지가 없습니다.")
            else:
                st.write('📷레시피 이미지')
                with st.container(height=500):
                    st.image(image_urls)


