import streamlit as st
from streamlit_option_menu import option_menu
import importlib



# 사용방법, 결과관련한 설명

st.html("<div style='text-align: center; font-size: 300%;'><b>ALARM⏰</b></div>")
st.html("<div style='text-align: center;'><b>Al</b>lergy, <b>A</b>ssessment, <b>R</b>ecognition, <b>M</b>anagement</div>")
st.divider()

st.write('''식품알레르기에 대한 정보를 찾기 어려웠던분들을 위한 서비스!   
         알레르기 정보와 서비스를 하나의 페이지로 담아 여러분들께 **ALARM**이 알려드립니다!🧚‍♀️''')

st.divider()

st.subheader('🍔 ALARM를 만든 배경',divider='orange')
col1, col2 = st.columns(2)
with col1:
    st.write('1. 식품 알레르기  위험성')
    col1_1,col1_2 = st.columns(2)
    with col1_1:
        st.image('image/배경1.jpg')
    with col1_2:
        st.image('image/배경2.jpg')
    st.caption('출처 : http://www.healtip.co.kr/news/articleView.html?idxno=3980#rs')

    st.write('3. 식품 알레르기 성분표 인식 저조')
    st.write("2015년 9월 전국 초, 중, 고 학생을 대상으로 한 조사에서 67.9%가 알레르기 유발식품 표시제에 대해 불만족. "
             "'성분표시 라벨을 쉽게 찾을 수 없다', '성분표시에 대한 내용이 구체적이지 않다'. ")

with col2:
    st.write('2. 식품 알레르기 표시대상 증가추세')
    st.image('image/배경3.jpg')

    st.write('4. 벤치마킹(알러지알려줘, 알러드림)')
    st.write(''': 알러지알려줘 서비스 종료   
: 알러드림의 경우, HACCP(한국식품안전관리인증원)에 등록된 식품만 확인할 수 있음. 식품 표준 바코드만 허용하므로 접근성 한계
''')

st.divider()


st.subheader('🥨 기능 및 사용방법',divider='rainbow')
tab1,tab2,tab3,tab4 = st.tabs(['레시피추천 챗봇','성분표 이미지인식','대체식품 알리미봇','알레르기 증상정보'])

with tab1:
# st.subheader('레시피추천 챗봇',divider='gray')
    col1,col2 = st.columns([2,1])
    with col1:
        st.write('🍳사용방법 : ')
        st.write('사용자의 알레르기를 작성한뒤 알고싶은 요리명을 작성하시면 요리주제에 맞게 추천해드립니다.')
        st.write('🍕내용 설명 : ')
        st.write('''레시피 제목과 재료, 요리순서를 알려드립니다.   
        레시피 이미지도 첨부되어있어 보다 요리를 쉽게 따라할 수 있습니다.''')
        st.write('''🍬주의사항 관련:   
                 1. 가공식품에 해당 알레르기가 성분이 함유되어있음을 주의해줍니다.   
                 2. 교차반응을 일으킬수 있는 성분에 대해 알려드립니다.''')
        cross_reaction_info = '''\n📌교차반응이란?\n
                                                \n알레르기 교차반응은 신체의 면역체계가 어떠한 물질(예: 돼지고기)에 들어 있는 단백질을 다른 물질(예: 타과일)
                                                에 들어 있는 단백질과 유사하다고 인식하면서 발생합니다. 환자가 실제로 그 중 하나와 접촉하면, 그것이 알레르기 유발 단백질이 맞는지에 관계없이 
                                                면역체계는 같은 방식으로 반응할 수 있으며  경우에 따라 알레르기 증상을 유발할 수도 있습니다.\n'''
        st.caption(cross_reaction_info)

    with col2:
        st.image('image/레시피추천챗봇 이미지.jpg')


with tab2:
    # st.subheader('성분표 이미지인식',divider='gray')
    col3,col4 = st.columns([2,1])
    with col3:
        st.write('🍳사용방법 : ')
        st.write('모든 제품의 성분표가 나와있는 부분을 사진찍어서 jpg,png 상관없이 모든 사진파일을 업로드 하시면 됩니다.')
        st.write('🍕내용 설명 : ')
        st.write('''원본과 인식이 되어진 부분에 대해 이미지가 나옵니다.   
        원재료명과 함유성분, 같은시설에서 제조한 부분까지 분석하여 19가지의 알레르기 성분에 해당하는것이 있다면 그부분만 간단하게 확인할 수 있게
        표 형태로 나타납니다.''')


    with col4:
        st.image('image/알레르기 스캐너 이미지.jpg')

with tab3:
    col1,col2 = st.columns([2,1])
    with col1:
        st.write('🍳사용방법 : ')
        st.write('알레르기명을 챗봇에 질문하면 됩니다.')
        st.write('🍕내용 설명 : ')
        st.write('''알레르기가 있는 식품 대신에 비슷한 영양성분인 대체식품을 추천해드립니다.''')

    with col2:
        st.image('image/대체식품 알리미봇 이미지.jpg')

with tab4:
    col1,col2 = st.columns([2,1])
    with col1:
        st.write('🍳사용방법 : ')
        st.write('종류별로 되어있는 탭을 선택하고 알러지명을 선택하면 됩니다.')
        st.write('🍕내용 설명 : ')
        st.write('''선택한 해당 알레르기 증상에 대해 확인 할 수 있습니다.''')

    with col2:
        st.image('image/알레르기 증상정보 이미지.jpg')

st.divider()





# 'utils.loader' 모듈 임포트
module_name = 'utils.loader'
module = importlib.import_module(module_name)
# 모듈의 모든 속성을 현재 네임스페이스로 가져오기
for attribute_name in dir(module):
    if not attribute_name.startswith('__'):
        globals()[attribute_name] = getattr(module, attribute_name)


