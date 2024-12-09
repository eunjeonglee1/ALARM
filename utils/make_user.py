import streamlit as st

class User():
    def __init__(self):
        if 'allergies' not in st.session_state:
            st.session_state.allergies = ''
        if 'user_food' not in st.session_state:
            st.session_state.user_food = ''
        self.allergies = st.session_state.allergies
        self.user_food = st.session_state.user_food

    def update(self, allergy, food):
        self.allergies = allergy
        self.user_food = food
        st.session_state.allergies = allergy
        st.session_state.user_food = food
        # st.write('업데이트 완료')