import streamlit as st
from streamlit_option_menu import option_menu


st.subheader('식품 알레르기란 무엇일까요?',divider='red')
st.write('''식품 알레르기란, ***원인이 되는 식품을 섭취한 후에 면역글로불린 E(IgE)나 림프구 등 우리 몸의 면역체계가 식품 내 항원과 반응하여 
다양한 증상을 일으키는 면역 과민반응 현상***입니다.''')
st.write('매우 적은 양이라도 특정 식품을 먹을 때마다 반응이 일어나고, 심한 경우 생명을 위협할 수 있으니 제대로 알고 대처해야 합니다')
st.image('image/홈페이지.png')
st.write('사람마다 알레르기를 일으키는 식품의 종류와 양이 다르고, 식품 섭취 후 반응이 나타나는 시간, 증상의 정도 등이 다양합니다.')


st.subheader('식품 알레르기 유발식품 표시',divider='orange')

col1, col2,col3 = st.columns([4,0.5,3.5])
with col1:
    st.html("<div style='text-align: center;'><b>🍙식품 알레르기 유발식품 표시제<b></div>")
    st.image('image/식품알레르기 종류.jpg')
    st.write('모든 가공식품에는 식약처에서 고시한 **19가지 알레르기 유발식품**을 표기하도록 하고 있습니다.')

with col3:
    st.html("<div style='text-align: center;'><b>🥨알레르기 유발식품 표시 확인방법<b></div>")
    st.image('image/알레르기 유발식품 표시 확인방법.jpg')
    st.image('image/알레르기 유발식품 표시 확인방법2.jpg')


st.subheader('식품 라벨 읽는 방법',divider='green')
col3_1,col3_2 = st.columns([2.5,1])
with col3_1:
    st.html('''
    <table border="1" style="width:100%; border-collapse: collapse; text-align: center;">
        <tr><tr bgcolor="#FFA8A8"><th colspan="1">1. 작은 글씨 모두 읽기</th></th></tr>
        <tr><td >식품 라벨을 꼼꼼하게 확인해요!</td></tr>
        <tr bgcolor="#FFA8A8"><th colspan="1">2. 알레르기 식품의 다른 표현 알아두기</th></tr>
        <tr><td>우유 - 카제인, 유청 단백 등</td></tr>
        <tr><td>계란 - 난백, 난황, 알부민 등으로 표기될 수 있음</td></tr>
        <tr><tr bgcolor="#FFA8A8"><th colspan="1">3. 교차반응이 나타날 수 있는 식품 살피기</th></th></tr>
        <tr><td>우유-산양유, 땅콩-견과류, 새우-게, 바닷가재 등</td></tr>
        <tr><tr bgcolor="#FFA8A8"><th colspan="1">4. 알레르기 식품으로 만든 2차 식품도 주의하기</th></th></tr>
        <tr><td>우유로 만든 유제품, 알레르기 식품 유래 비타민 등</td></tr>
    </table>
    ''')
with col3_2:
    st.image('image/free-sticker-cooking-11752470.png')

st.divider()
st.caption('출처 : https://www.foodsafetykorea.go.kr/portal/board/boardDetail.do?menu_no=3120&menu_grp=MENU_NEW01&bbs_no=bbs001&ntctxt_no=1091412')
st.caption('''서울특별시교육청·서울시(복지건강본부)식품안전과. (2011). 식품 알레르기 이렇게 알아보아요!.  
서울특별시 아토피 천식 교육정보센터. (2021). 식품표시/라벨 읽는법 (p.15).''')