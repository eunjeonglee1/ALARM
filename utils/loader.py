import pandas as pd
from langchain_community.document_loaders.csv_loader import CSVLoader
from utils.vecsto import *


@st.cache_data
def loader_data(file_path):
    loader = CSVLoader(file_path=file_path, encoding='utf-8')
    data = loader.load()
    return data
@st.cache_data
def recipe_data(file_path):
    df = pd.read_csv(file_path)
    return df

@st.cache_data
def ingredient_data(file_path):
    df = pd.read_csv(file_path)
    return df

@st.cache_data
def raw_material_data(file_path):
    df = pd.read_csv(file_path)
    return df

@st.cache_data
def processed_food_data(file_path):
    df = pd.read_csv(file_path)
    return df

@st.cache_data
def ing_name_data(file_path):
    df = pd.read_csv(file_path)
    return df

@st.cache_data
def oto_data(file_path):
    df = pd.read_csv(file_path)
    oto_dict = df.set_index('코드').to_dict()
    oto_dict = oto_dict['식품명']
    return oto_dict

@st.cache_data
def cross_data(file_path):
    df = pd.read_csv(file_path)
    df.drop(columns=['Unnamed: 0', '알레르기식품명', '교차반응식품명'], inplace=True)
    return df

@st.cache_data
def image_data(file_path):
    df = pd.read_csv(file_path)
    return df


if 'oto' not in st.session_state:
    st.session_state.oto = oto_data('data/식품_코드_일대일매칭.csv')
if 'recipe' not in st.session_state:
    st.session_state.recipe = recipe_data('data/레시피_일련번호.csv')
if 'ingredient' not in st.session_state:
    st.session_state.ingredient = ingredient_data('data/레시피_재료.csv')
if 'raw_material' not in st.session_state:
    st.session_state.raw_material = raw_material_data('data/원재료.csv')
if 'processed_food' not in st.session_state:
    st.session_state.processed_food = processed_food_data('data/가공식품.csv')
if 'ing_name' not in st.session_state:
    st.session_state.ing_name = ing_name_data('data/재료명2_수정.csv')
if 'cross' not in st.session_state:
    st.session_state.cross = cross_data('data/알레르기_교차반응_매핑_수정본.csv')
if 'loader' not in st.session_state:
    st.session_state.loader = loader_data('data/레시피이름_url번호.csv')
if 'retriever' not in st.session_state:
    st.session_state.retriever = create_vectorstore(st.session_state.loader)
if 'image' not in st.session_state:
    st.session_state.image = image_data('data/recipe_content_final.csv')


