import numpy as np
import platform
from PIL import ImageFont, ImageDraw, Image
import matplotlib.pyplot as plt
import pandas as pd
import mysql.connector

import uuid
import json
import time
import cv2
import requests
from openai import OpenAI
import re
import os

import streamlit as st
from io import StringIO
from tempfile import NamedTemporaryFile

# from langchain_community.vectorstores import FAISS

import ast
import bs4


def plt_imshow(title='image', img=None, figsize=(8, 5)):
    plt.figure(figsize=figsize)

    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []

            for i in range(len(img)):
                titles.append(title)

        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)

            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])

        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()

# OpenCV의 putText를 이용하여 한글을 출력하는 경우 한글이 깨지는 문제를 해결하기 위한 Funtion
def put_text(image, text, x, y, color=(0, 255, 0), font_size=22):
    if type(image) == np.ndarray:
        color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(color_coverted)

    if platform.system() == 'Darwin':
        font = 'AppleGothic.ttf'
    elif platform.system() == 'Windows':
        font = 'malgun.ttf'

    image_font = ImageFont.truetype(font, font_size)
    font = ImageFont.load_default()
    draw = ImageDraw.Draw(image)

    draw.text((x, y), text, font=image_font, fill=color)

    numpy_image = np.array(image)
    opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    return opencv_image


# 함수: 알레르기가 없는 레시피 번호,url일련번호, 교차반응 메세지, 가공식품에 알레르기가 포함된 메세지
def CrossAndWarn(ingredient_df,raw_material_df,processed_food_df,recipe_df,cross,user_food, context, allergys=None):

    # 멀티쿼리
    # recipe_numbers_li = re.findall(r'레시피번호: (\d+)', context)
    # recipe_numbers_li =[int(i) for i in recipe_numbers_li ]

    # 벡터스토어에서 가져온 항목중 요리명이 포함된 음식만 추출

    c_temp = [doc for doc in context if re.search(fr'{user_food}', doc.page_content)]
    # 벡터스토어에 요리명이 아예 없는경우 (ex. 비건탕수육)
    if len(c_temp) == 0:
        return -1, '-1', {}, {}

    # 셔플 # 사용자에게 더욱 다양하게 주기위해서 셔플
    import random
    random.shuffle(c_temp)

    # 일반쿼리
    recipe_numbers_li = [re.search(r'레시피번호:\s*(\d+)', doc.page_content).group(1) for doc in c_temp]
    recipe_numbers_li = [int(i) for i in recipe_numbers_li]

    # 셔플
    import random
    random.shuffle(recipe_numbers_li)


    # cross.drop(columns=['Unnamed: 0', '알레르기식품명', '교차반응식품명'], inplace=True)
    c = cross.set_index(['알레르기코드']).to_dict()

    # temp는 이중리스트구조 [['A09', 'C29', 'C15'], ['A05', 'A06', 'A07', 'C27', 'C10', 'C17', 'C03']]를 다시 일차원 리스트로
    temp = [c['교차반응코드'][allergy].split(',') for allergy in allergys]

    # c_li는 교차반응코드를 중복없이 받을꺼임
    c_li = []

    for li in temp:
        for i in li:
            c_li.append(i)

    c_li = list(set(c_li))

    count = 1
    # 레시피번호 하나씩 확인하는 절차
    for num in recipe_numbers_li:
        # st.write(f'{count}번째')
        count += 1
        # st.write(f'레시피 번호 : {num}')

        # cnt=0이면 원재료에 알레르기성분 있다 cnt=1이면 정상 cnt=-1이면 못찾음
        cnt = -1
        # 재료df에서 레시피번호에 해당하는 요리
        temp_df = ingredient_df[ingredient_df['Recipe_Num'].isin([num])]

        # 재료들을 리스트에 넣어둠
        ingred_li = ingredient_df[ingredient_df['Recipe_Num'].isin([num])]['Ingredients_Code']
        temp_li = []

        temp_raw_dict = {}  # 원재료 교차반응 담을꺼임 ex){ 재료1:[코드1,코드2...], ... }
        temp_pre_dict = {}  # 가공식품 교차반응 담을꺼임 ex){ 재료2:[코드1,코드2...], ... }
        warning = {}

        # 알레르기 가공품에 해당하는 목록들을 모음
        temp_preprocess = []

        # 알러지가 없으면 넘어가자~~
        if allergys == None:
            break

        # 각각의 재료
        # st.write('원재료 확인 시작')
        for ingredient in list(ingred_li):
            # st.write(ingredient)
            # 교차반응 코드 넣음 (딕셔너리에
            temp_li = []

            # 원재료 비교
            # 재료에 해당하는 코드(알레르기와 비교할꺼임)
            for code in list(raw_material_df[raw_material_df['Ingredients_Code'] == ingredient]['Allergy_Code']):
                # 알레르기코드와 원재료 알레르기코드와 같으면 끝.
                if code in allergys:
                    cnt = 0
                    break
                if code in c_li:
                    temp_li.append(code)

            temp_raw_dict[ingredient] = temp_li

            if cnt == 0:
                # st.write(f'레시피 번호 {num}에 재료 {ingredient}에 알레르기 성분 존재.')
                break
        if cnt == 0:
            # st.write('다음 번호 확인')
            continue

        # 재료를 가공식품 테이븝에서 비교
        # st.write('가공식품 확인 시작')
        cnt = 1
        for ingredient in list(ingred_li):
            # st.write(ingredient)

            # 알레르기 가공식품 경고
            temp_warn = []
            temp_li = []

            for code in list(processed_food_df[processed_food_df['Ingredients_Code'] == ingredient]['Allergy_Code']):

                if code in allergys:
                    temp_warn.append(code)

                if code in c_li:
                    temp_li.append(code)

            temp_pre_dict[ingredient] = temp_li
            warning[ingredient] = temp_warn

        if cnt == 1:
            # st.write('문제 없음')
            # st.write('끝')
            break

    if cnt == 1:
        combined = {}
        for key in temp_raw_dict.keys():
            combined[key] = temp_raw_dict[key] + temp_pre_dict[key]

            url_num = recipe_df[recipe_df['Recipe_Num'] == num]['URL_Num']
            u = url_num.values[0]

            # 레시피 번호, 교차반응 메세지, 가공식품에 알레르기가 포함된 메세지
        return num, u, combined, warning

    else:
        return -1, '-1', {}, {}

# 위의 함수에서 받은 경고가 code(ex.A04)로 구현되있기때문에 이름으로 바꿔준다
def replaceCode(ing_name_df,recipe_num,oto_dict, cross_message, warning_message, allergys=None):
    cross_comment_li = {}
    warn_comment_li = {}

    # 알러지 코드도 한글로
    c = []
    for allergy in allergys:
        c.append(oto_dict[allergy])

    if allergys == None:
        return c, cross_comment_li, warn_comment_li

    for ikey, ival in cross_message.items():
        if ival:
            # 재료코드를 재료이름으로 바꾸기
            code_Name = \
            ing_name_df[(ing_name_df['Recipe_Num'] == recipe_num) & (ing_name_df['Ingredients_Code'] == ikey)][
                'Ingredient_Name']
            code_Name = code_Name.values[0]

            # 유발 식품 넣어두기
            food_names = []
            for val in ival:
                food_names.append(oto_dict[val])
            cross_comment_li[code_Name] = food_names

    for ikey, ival in warning_message.items():
        if ival:
            # 재료코드를 이름으로 바꾸기
            code_Name = \
            ing_name_df[(ing_name_df['Recipe_Num'] == recipe_num) & (ing_name_df['Ingredients_Code'] == ikey)][
                'Ingredient_Name']
            code_Name = code_Name.values[0]

            # 유발 식품 넣어두기
            food_names = []
            for val in ival:
                food_names.append(oto_dict[val])
            warn_comment_li[code_Name] = food_names

    return c, cross_comment_li, warn_comment_li


def format_docs(docs):
    return '\n\n'.join([d.page_content for d in docs])


def response_generator(message):
    for word in message:
        yield word
        time.sleep(0.03)


# HTML 테이블 생성 함수
def create_html_table(df,key):
    html = '<table border="1" style="width:100%; border-collapse: collapse; text-align: center;">'
    html += f'<tr><tr bgcolor="#FFA8A8"><th colspan="5">{key}</th></th></tr>'
    for index, row in df.iterrows():
        html += '<tr>'
        html += ''.join([f'<td>{cell if cell is not None else ""}</td>' for cell in row])
        html += '</tr>'
    html += '</table>'
    return html
def row_html_table(df):
    html = '<table border="1" style="width:100%; border-collapse: collapse; text-align: center;">'
    html += '<tr><tr bgcolor="#FFA8A8"><th colspan="1">원재료명</th></th></tr>'
    for index, row in df.iterrows():
        html += '<tr>'
        html += ''.join([f'<td>{cell if cell is not None else ""}</td>' for cell in row])
        html += '</tr>'
    html += '</table>'
    return html