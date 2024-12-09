import streamlit as st


def infomation(genre):
    if genre == '난류(계란)':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
            - 알레르기 증상    
                - 목구멍의 부종, 기도 협착, 경련으로 인한 호흡곤란
                - 혈압 강하를 동반한 쇼크
                - 복부 통증, 경련
                - 맥박의 상승
                - 현기증, 머리가 어찔하거나 의식을 상실함''')
            with col2:
                st.image('image/알레르기증상 이미지4.jpg')

    elif genre == '우유':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 두드러기
                    - 쌕쌕거리는 호흡(천명음)
                    - 구토
                    - 혈변
                    - 복부 경련
                    - 기침과 호흡 곤란 
                    - 콧물
                    - 눈물
                    - 가려운 피부 발진(종종 입가 주변)
                    - 유아가 다양한 불쾌감으로 인해 빈번하게 우는 증상
                    - 목구멍의 부종, 기도 협착과 경련으로 인한 호흡곤란
                    - 안면홍조
                    - 가려움
                    - 혈압 강하를 동반한 쇼크''')
            with col2:
                st.image('image/알레르기증상 이미지3.jpg')

    elif genre == '밀':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 입 또는 목의 부종, 가려움, 염증
                    - 두드러기, 가려움을 동반한 발진 또는 피부 부종
                    - 코의 충혈
                    - 가려움, 눈물
                    - 호흡곤란
                    - 경련, 메스꺼움 또는 구토
                    - 설사
                    - 목구멍의 부종 및 긴장
                    - 흉통 또는 긴장
                    - 심각한 호흡곤란
                    - 연하곤란
                    - 창백, 청색증
                    - 현기증 또는 어지러움
                    - 서맥''')
            with col2:
                st.image('image/알레르기증상 이미지5.jpg')

    elif genre == '복숭아':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 복통, 설사, 구역, 구토, 위경련
                    - 두드러기(알레르기성 두드러기), 가려움, 습진
                    - 쌕쌕거림, 코막힘, 호흡곤란, 반복적인 기침
                    - 쇼크, 순환계 붕괴
                    - 목 조임, 쉰 목, 삼키기 어려움
                    - 창백한 피부 또는 파란 피부 색
                    - 어지러움, 현기증, 실신, 약한 맥박
                    - 아나필락시스
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지6.jpg')

    elif genre == '이황산류':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 두통, 복통, 메스꺼움, 순환기장애, 위점막자극, 기관지염
                    - 기관지 수축, 두드러기, 접촉성 피부염
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지7.jpg')

    elif genre in ['돼지고기', '소고기', '닭고기']:
        with st.container(border=True):
            col1,col2 = st.columns([2,0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 발진, 두드러기, 가려움증
                    - 복통 구토 설사
                    - 천명음(쌕쌕거림) 기침 호흡곤란
                    - 아나필락시스
                    - 진드기(학명 ‘Amblyomma americanum’)에의한 증상 
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지.jpg')

    elif genre == '대두':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 입가의 얼얼함
                    - 두드러기, 가려움 또는 습진
                    - 입술, 얼굴, 혀, 목구멍 및 다른 부위의 부종
                    - 콧물 또는 호흡곤란
                    - 복부 흉통, 설사, 메스꺼움 또는 구토
                    - 현기증, 머리가 몽롱하거나 혼미
                    - 목구멍의 부종, 기도 협착과 경련증으로 인한 호흡곤란
                    - 혈압 강하를 동반한 쇼크
                    - 맥박 저하
                    - 현기증, 머리가 어찔하거나 의식 불명
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지8.jpg')

    elif genre == '땅콩':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 피부 두드러기, 홍조 또는 부종
                    - 입가나 목구멍이 가렵거나 죄여오는 느낌
                    - 설사, 위경련, 메스꺼움 또는 구토와 같은 소화 불량
                    - 가슴을 죄여오는 느낌
                    - 숨쉬기가 짧거나 헐떡거림
                    - 콧물 또는 코 막힘  
                - 아나필락스 작용후 증상
                    - 목구멍의 부종, 기도 협색증으로 인한 호흡곤란
                    - 혈압 강하를 동반한 쇼크
                    - 맥박의 상승
                    - 현기증, 머리가 어찔하거나 의식 상실
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지9.jpg')

    elif genre in ['호두','잣']:
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 복통, 경련, 메스꺼움 및 구토
                    - 설사
                    - 삼키기 어려움(연하장애)
                    - 입, 목, 눈, 피부 또는 다른 부위의 가려움
                    - 코막힘, 콧물
                    - 숨가쁨
                    - 아나필락시스, 잠재적으로 생명을 위협하는 사건
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지10.jpg')

    elif genre in ['게', '새우','오징어','조개류']:
        with st.container(border=True):
            col1,col2 = st.columns([3,1])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 두드러기, 가려움 또는 습진
                    - 입술, 얼굴 혀, 목구멍이나 몸의 다른 부분의 부종, 가려움
                    - 숨을 헐떡이며 쉬거나 코의 울혈 또는 호흡곤란
                    - 복부 통증, 설사, 메스꺼움 또는 구토
                    - 현기증, 머리가 어찔하거나 실신
                    - 입 안의 따가움
                - 아나필락스 작용후 증상
                    - 목구멍의 부종, 기도 협착과 경련증으로 인한 호흡곤란
                    - 혈압 강하를 동반한 쇼크
                    - 맥박의 상승
                    - 현기증, 머리가 어찔하거나 의식 상실
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지2.jpg')

    elif genre == '메밀':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 복통, 설사, 구역, 구토, 위경련
                    - 두드러기(알레르기성 두드러기), 가려움, 습진
                    - 쌕쌕거림, 코막힘, 호흡곤란, 반복적인 기침
                    - 쇼크, 순환계 붕괴
                    - 삼키기 어려움, 쉰 목, 삼키기 어려움
                    - 창백한 피부 또는 푸른 피부 색 
                    - 어지러움, 현기증, 실신, 약한 맥박
                    - 아나필락시스
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지11.jpg')

    elif genre == '고등어':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 복통, 설사, 구역, 구토, 위경련
                    - 두드러기(알레르기성 두드러기), 가려움, 습진
                    - 쌕쌕거림, 코막힘, 호흡곤란, 반복적인 기침
                    - 쇼크, 순환계 붕괴
                    - 목 조임, 쉰 목, 삼키기 어려움
                    - 창백한 피부 또는 파란 피부 색
                    - 어지러움, 현기증, 실신, 약한 맥박
                    - 생명에 위협이 될 수도 있는 아나필락시스
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지12.jpg')

    elif genre == '토마토':
        with st.container(border=True):
            col1, col2 = st.columns([2, 0.7])
            with col1:
                st.write('''
                - 알레르기 증상    
                    - 복통, 설사, 구역, 구토, 위경련
                    - 두드러기(알레르기성 두드러기), 가려움, 습진
                    - 쌕쌕거림, 코막힘, 호흡곤란, 반복적인 기침
                    - 쇼크, 순환계 붕괴
                    - 목 조임, 쉰 목, 삼키기 어려움
                    - 창백한 피부 또는 파란 피부 색
                    - 어지러움, 현기증, 실신, 약한 맥박
                    - 생명에 위협이 될 수도 있는 아나필락시스
        
                    ''')
            with col2:
                st.image('image/알레르기증상 이미지13.jpg')