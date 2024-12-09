import streamlit as st
import pandas as pd
from openai import OpenAI
import time
import os

combined_df1 = pd.read_csv('data/토마토_대두.csv', index_col=[0])
combined_df2 = pd.read_csv('data/나머지.csv', index_col=[0])

api_key = os.environ['OPENAI_API_KEY']
client = OpenAI(api_key = api_key)


st.header('알러지 안심 대체식품 추천봇🤖',divider='orange')

with st.container(height=100):
    st.write('''
            📢 아래에 해당하는 **식품알레르기명** 을 작성하시면 :red[대체식품]을 추천해드립니다.
        ''')
    st.caption('ex) 계란 / 돼지고기')

with st.popover("알레르기명 보기"):
    st.table({'식품알레르기 종류':['난류','소고기','돼지고기','닭고기','새우','게','오징어','고등어','조개류','우유','땅콩','호두','잣','대두','복숭아','토마토',
         '밀','메밀','이황산류']})


def find_alternative(allergic_food):
    # 첫 번째 데이터프레임에서 검색
    alternatives1 = combined_df1[combined_df1["알레르기식품"] == allergic_food]
    if not alternatives1.empty:
        return alternatives1

    # 두 번째 데이터프레임에서 검색
    alternatives2 = combined_df2[combined_df2["알레르기식품"] == allergic_food]['대체식품']
    if not alternatives2.empty:
        return alternatives2.values

    return None


def chat_with_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        n=1,
        stop=None,
        temperature=0.5
    ).model_dump()
    return response['choices'][0]['message']['content']

# chat 히스토리를 초기화
if 'history' not in st.session_state:
    st.session_state.history = []

# 히스토리로부터 들어있는 메세지를 출력
for message in st.session_state.history:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

if user_input := st.chat_input("알레르기 식품을 입력하세요"):
    with st.chat_message('user'):
        st.markdown(user_input)
        st.session_state.history.append({'role': 'user', 'content': user_input})


    # 난류대신 계란으로 대답할 시 바꿔주는 코드
    if user_input == '계란':
        alternatives = find_alternative('난류')
    elif user_input == '돼지':
        alternatives = find_alternative('돼지고기')
    elif user_input == '소':
        alternatives = find_alternative('소고기')
    elif user_input in ['조개','홍합','굴','바지락']:
        alternatives = find_alternative('조개류')
    elif user_input in ['이황산류']:
        alternatives = find_alternative('아황산류')
    else:
        alternatives = find_alternative(user_input)


    if alternatives is None:
        prompt = f"해당 알레르기 식품에 대한 대체식품 정보를 찾을 수 없습니다."

    elif isinstance(alternatives, pd.DataFrame):
        lists = []
        for idx, row in alternatives.iterrows():
            lists.append(row['대체식품'])
        prompt = f"사용자가 '{user_input}'에 알레르기가 있습니다. 이를 대체할 수 있는 식품은 '{lists}'입니다."

    else:
        prompt = f"사용자가 '{user_input}'에 알레르기가 있습니다. 이를 대체할 수 있는 식품은 '{alternatives}'입니다."

    with st.chat_message('assistant'):
        response = chat_with_openai(prompt)
        def response_generator():
            for word in response:
                yield word
                time.sleep(0.03)
        result = st.write_stream(response_generator())
        st.session_state.history.append({'role': 'assistant', 'content': result})



