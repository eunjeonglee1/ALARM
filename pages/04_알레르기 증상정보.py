from utils.info import *

st.header('알러지 리포트: 증상 파악하기',divider='orange')

with st.container(height=60):
    st.write('''
            📌먼저 종류를 고르고 알러지명을 선택하시면 해당 **알러지 증상**에 대해 알려드려요. 
        ''')

tab1,tab2,tab3,tab4,tab5,tab6,tab7 = st.tabs(['육류','해산물','유제품 및 난류','견과류 및 콩류','과일','곡류','기타'])

with tab1:
    genre = st.radio(
        "알레르기가 있는 품목을 고르세요",
        ['소고기','돼지고기','닭고기'], horizontal=True,label_visibility='collapsed')
    st.subheader(genre)
    infomation(genre)

with tab2:
    genre = st.radio(
        "알레르기가 있는 품목을 고르세요",
        ['새우','게','오징어','고등어','조개류'], horizontal=True,label_visibility='collapsed')
    st.subheader(genre)
    infomation(genre)

with tab3:
    genre = st.radio(
        "알레르기가 있는 품목을 고르세요",
        ['우유','난류(계란)'], horizontal=True,label_visibility='collapsed')
    st.subheader(genre)
    infomation(genre)

with tab4:
    genre = st.radio(
        "알레르기가 있는 품목을 고르세요",
        ['땅콩','호두','잣','대두'], horizontal=True,label_visibility='collapsed')
    st.subheader(genre)
    infomation(genre)

with tab5:
    genre = st.radio(
        "알레르기가 있는 품목을 고르세요",
        ['복숭아','토마토'], horizontal=True,label_visibility='collapsed')
    st.subheader(genre)
    infomation(genre)

with tab6:
    genre = st.radio(
        "알레르기가 있는 품목을 고르세요",
        ['밀','메밀'], horizontal=True,label_visibility='collapsed')
    st.subheader(genre)
    infomation(genre)

with tab7:
    genre = st.radio(
        "알레르기가 있는 품목을 고르세요",
        ['이황산류'], horizontal=True,label_visibility='collapsed')
    st.subheader(genre)
    infomation(genre)

st.write('👇 자세한 내용을 확인하려면 아래의 버튼을 눌러주세요')
st.link_button("식품안전나라", "https://www.foodsafetykorea.go.kr/portal/board/boardDetail.do?menu_no=3409&menu_grp=MENU_NEW05&bbs_no=bbs820&ntctxt_no=1064525&start_idx=2&nticmatr_yn=N&bbs_type_cd=03&ans_yn=N&order_type=01&list_img_use_yn=Y&atch_file_posbl_yn=Y&cmt_yn=N&kword_use_yn=N&natn_cd_use_yn=N&tag_use_yn=N&meta_use_yn=N&show_cnt=12")



