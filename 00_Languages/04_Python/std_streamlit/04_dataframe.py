# 04.dataframe.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("04. 데이터프레임")
st.write("Streamlit 으로 DataFrame을 보여줄 수 있다.")
st.write("이미지 컬럼, 프로그레스 바 컬럼 등 다양한 컬럼 형식을 지원하고")
st.write("웹앱에서 실시간 편집도 가능하다.")

# 1. 데이터 제작
num_rows = st.slider("Number of Rows", 1, 100, 50)
np.random.seed(42)
data = []
for i in range(num_rows):
    data.append(
        {
            "Preview": f"https://picsum.photos/400/200?lock={i}",
            "Size": f"({np.random.randint(800, 1000)}, {np.random.randint(400, 500)})",
            "Like": np.random.choice([True, False]),
            "Like Ratio": np.random.randint(65, 99),
        }
    )
data = pd.DataFrame(data)

# 2. 컬럼 설정
config = {
    "Preview": st.column_config.ImageColumn(),
    "Like Ratio": st.column_config.ProgressColumn()
}

# 3. 데이터프레임 표현 & 편집 가능 여부 설정
if st.toggle("편집 모드"):
    edited_data = st.data_editor(data, column_config=config, use_container_width=True)
else:
    st.dataframe(data, column_config=config, use_container_width=True)