import pandas as pd

from utils.mo import *
from stqdm import stqdm
from time import sleep
from tabulate import tabulate

api_url = os.environ['NAVER_API_URL']
secret_key = os.environ['Secret_Key']


st.header('알러지 스캐너',divider='orange')

with st.container(height=60):
    st.write('''
            🔎 **제품의 상세정보 이미지**를 사진찍어서 파일업로드하시면 **알레르기 성분**을 분석해드립니다.
        ''')

uploaded_file = st.file_uploader("파일을 업로드하세요",label_visibility='collapsed')

if uploaded_file is not None:

    progress_text = "이미지 분석중..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.05)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)




    # files = [('file', open(uploaded_file, 'rb'))]
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    file_content = uploaded_file.read()
    files = {'file': (uploaded_file.name, file_content)}

    file_extension = uploaded_file.name.split('.')[-1].lower()

    request_json = {'images': [{'format': f'{file_extension}',
                                'name': 'demo'
                                }],
                    'requestId': str(uuid.uuid4()),
                    'version': 'V2',
                    'timestamp': int(round(time.time() * 1000)),
                    'enableTableDetection': True
                    }

    payload = {'message': json.dumps(request_json).encode('UTF-8')}

    headers = {
        'X-OCR-SECRET': secret_key,
    }

    response = requests.request("POST", api_url, headers=headers, data=payload, files=files)
    result = response.json()

    # st.write(result)

    # 임시 파일로 저장
    with NamedTemporaryFile(delete=False, suffix=f'{file_extension}') as temp_file:
        temp_file.write(file_content)
        temp_file_path = temp_file.name

    # OpenCV로 이미지 읽기
    img = cv2.imread(temp_file_path)

    # BGR에서 RGB로 변환
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # # OpenCV 이미지를 PIL 이미지로 변환
    # img_pil = Image.fromarray(img_rgb)

    if img is not None:
        roi_img = img_rgb.copy()
        for field in result['images'][0]['fields']:
            text = field['inferText']
            vertices_list = field['boundingPoly']['vertices']
            pts = [tuple(vertice.values()) for vertice in vertices_list]
            topLeft = [int(_) for _ in pts[0]]
            topRight = [int(_) for _ in pts[1]]
            bottomRight = [int(_) for _ in pts[2]]
            bottomLeft = [int(_) for _ in pts[3]]

            cv2.line(roi_img, topLeft, topRight, (0, 255, 0), 2)
            cv2.line(roi_img, topRight, bottomRight, (0, 255, 0), 2)
            cv2.line(roi_img, bottomRight, bottomLeft, (0, 255, 0), 2)
            cv2.line(roi_img, bottomLeft, topLeft, (0, 255, 0), 2)
            roi_img = put_text(roi_img, text, topLeft[0], topLeft[1] - 10, font_size=30)

            # print(text)
        # st.image([img, roi_img],["Original", "ROI"])



        col1, col2 = st.columns(2)
        with col1:
            st.image([img_rgb], caption=["Original Image"], width=200, use_column_width=True)
        with col2:
            st.image([roi_img], caption=["Processed Image"], width=200, use_column_width=True)


        my_bar.empty()



        progress_text = "알레르기성분 분석중..."
        my_bar = st.progress(0, text=progress_text)
        for percent_complete in range(100):
            time.sleep(0.05)
            my_bar.progress(percent_complete + 1, text=progress_text)


        # 응답 내용을 정리
        try:
            table_dict = {}

            cells = result['images'][0]['tables'][0]['cells']
            for cell in cells:
                row = cell['rowIndex']
                col = cell['columnIndex']
                rowspan = cell['rowSpan']
                colspan = cell['columnSpan']
                text = " ".join([word['inferText'] for line in cell['cellTextLines'] for word in line['cellWords']])

                # Store cell information
                if row not in table_dict:
                    table_dict[row] = {}
                table_dict[row][col] = {'text': text, 'rowspan': rowspan, 'colspan': colspan}

            table = []
            for row in table_dict:
                for col in table_dict[row]:
                    cell_info = table_dict[row][col]
                    table.append(cell_info['text'])
            full_text = ' '.join(table)
        except:
            all_texts = []
            for field in result['images'][0]['fields']:
                text = field['inferText']
                all_texts.append(text)
            full_text = ' '.join(all_texts)

        # DB 연결
        conn = mysql.connector.connect(
            host='localhost',
            database='allergy_recipe',
            user='root',
            password='1234'
        )

        # 알레르기 코드
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM allergy_code;')
        records = cur.fetchall()
        allergy_df = pd.DataFrame(records, columns=['code', 'name'])

        # 교차반응 코드
        cur2 = conn.cursor()
        cur2.execute(f'SELECT * FROM cross_code;')
        records2 = cur2.fetchall()
        cross_df2 = pd.DataFrame(records2, columns=['code', 'name'])

        # 두 코드 합치기
        final_df = pd.concat([allergy_df, cross_df2])

        # 코드 리스트로 만들기
        allergy_data = final_df['name'].values
        list_data = allergy_data.flatten().tolist()
        check_list = list_data + ['계란', '알류(가금류)', '알류', '아황산류', '쇠고기']


        client = OpenAI()

        # 답변형식 지정
        ans = """{'원재료명':['''insert here'''], '함유성분':['''insert here'''], '같은시설에서 제조':['''insert here''']}"""

        # ChatGPT 호출
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "당신은 영양성분표의 원재료 및 함유, 알레르기를 분석하여 JSON 형식으로 출력하는 데 도움이 되는 조력자입니다."},
                {"role": "user", "content": f'''{full_text}을 분석해 주세요.  {ans}의 형식으로 말해주세요.
                함유성분 {check_list}만 입니다. 이 리스트에 있는것만 검색하고 그외의 것은 생략해주세요.
                없을시엔 표시하지 말아주세요'''},
            ],
            temperature=0
        )

        # ChatGPT 회신
        message = response.choices[0].message.content

        # st.write(message)

        data = json.loads(message)

        # OCR데이터를 알레르기코드와 부분일치시키기
        matching = {category: [item for item in items if any(check in item for check in check_list)] for
                    category, items
                    in data.items()}
        # result_df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in matching.items()])).fillna('')

        # 최대 열 수 설정
        max_columns = 5

        # 각 카테고리별 데이터프레임 리스트
        dataframes = []

        for key, items in matching.items():
            if key == '원재료명':
                # 데이터가 없으면 빈 칸을 유지
                if not items:
                    items = [""]

                # 항목들을 최대 max_columns씩 분할하여 행을 생성
                rows = [items[i:i + 1] for i in range(0, len(items), 1)]

                # 데이터프레임 생성
                df = pd.DataFrame(rows)

                # HTML 테이블 생성
                html_table = row_html_table(df)

                # HTML 테이블을 Streamlit에 표시
                st.markdown(html_table, unsafe_allow_html=True)
            else:
                # 데이터가 없으면 빈 칸을 유지
                if not items:
                    items = [""]

                # 항목들을 최대 max_columns씩 분할하여 행을 생성
                rows = [items[i:i + max_columns] for i in range(0, len(items), max_columns)]

                # 데이터프레임 생성
                df = pd.DataFrame(rows)
                # HTML 테이블 생성
                html_table = create_html_table(df, key)
                # HTML 테이블을 Streamlit에 표시
                st.markdown(html_table, unsafe_allow_html=True)

        time.sleep(1)
        my_bar.empty()
