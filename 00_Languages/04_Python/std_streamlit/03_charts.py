# 03_charts.py
import streamlit as st
import pandas as pd
import numpy as np

st.title("03. 차트")
st.write("Streamlit 은 다양한 데이터 시각화를 지원합니다.")

# 1. 사용자 선택 인터랙션 박스
all_users = ["Alice", "Bob", "Charly"]
with st.container(border=True):
    users = st.multiselect("Users", all_users, default=all_users)
    rolling_average = st.toggle("Rolling average")

# 2. 데이터 만들기
np.random.seed(42)
data = pd.DataFrame(np.random.randn(20, len(users)), columns=users)
if rolling_average:
    data = data.rolling(7).mean().dropna()

# 3. 페이지 내부 탭에 차트 표시
tab1, tab2, tab3 = st.tabs(["Chart", "Scatter", "Dataframe"])
tab1.line_chart(data, height=250)
tab2.scatter_chart(data, height=250)
tab3.dataframe(data, height=250, use_container_width=True)