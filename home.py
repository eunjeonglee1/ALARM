from st_pages import get_nav_from_toml
import streamlit as st


nav = get_nav_from_toml(
    ".streamlit/pages_sections.toml"
)

st.logo(
    'image/로고 이미지2.png',
    link='http://192.168.75.166:8501/',
    icon_image='image/로고 아이콘.png',
)

pg = st.navigation(nav)


pg.run()