from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def makemodel():
    ans = """ https://www.10000recipe.com/recipe/’’’insert here’’’"""

    # Prompt
    template3 = '''

    Question : {question}


    사용자가 알레르기와 요리명 정보를 전달할거야. 맞춤법은 고쳐줘.
    만약 사용자의 알레르기 정보가 주어지면 알레르기를 리스트에서 참고해줘.
    참고로 계란,달걀,반숙은 난류야.
    ['소고기','난류','돼지고기','닭고기','새우','게','오징어','고등어','조개류','우유','땅콩',
     '호두','잣','대두','복숭아','토마토','밀','메밀','아황산류']
    꼭 알레르기와 질문은 분리해야해.
    food에는 알레르기 성분들을 제외한 핵심적인 요리이름만 넣어줘!.
    사용자가 알레르기 정보를 주지 않는다면 {prev_allergy}를 알레르기 정보로 사용해.
    다른거 추천해달라하면 {prev_food}를 요리명에 넣어줘
    쓸데없는 말 넣지말고 다음 형식을 따라서 대답해줘:
    {ans3}
    '''

    template2 = ''' {site_document} 참고해서 요리제목, 재료, 레시피를 한국어로 알려줘.

    {ans2}
    '''

    template4 = '''
            Extract and normalize the following list of ingredients according to these conditions:
            1. Choose one when ingredients are connected with '또는', '~나', 'or' 
            2. Use the same name for similar ingredients.
            3. Ensure the core ingredient remains.
            4. Make sure the number of ingredients in the output is the same as in the input list of ingredients
            5. Ensure that the input and output ingredients are in a 1:1 correspondence

            Provide a Dictionary in which original ingredient names are keys and normalized ingredient names are values.
            Output must be korean
            Just response Dictionary

            {ingredients}


    '''
    template__0 = '''
    사용자에게 {allergy}가 없는 {user_food} 레시피 알려줘
    '''

    prompt2 = ChatPromptTemplate.from_template(template2)
    prompt3 = ChatPromptTemplate.from_template(template3)
    prompt4 = ChatPromptTemplate.from_template(template4)
    prompt__0 = ChatPromptTemplate.from_template(template__0)

    # Model
    llm = ChatOpenAI(
        model='gpt-3.5-turbo-0125',
        temperature=0.6,
        max_tokens=1000,
    )
    llm4 = ChatOpenAI(
        model="gpt-4-turbo",
        temperature=0.2,
        max_tokens=100,
    )

    return llm, llm4, prompt2, prompt3, prompt4, prompt__0