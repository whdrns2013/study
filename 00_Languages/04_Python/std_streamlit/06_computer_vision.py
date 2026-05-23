# 06_computer_vision
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import requests

st.title("06. Computer Vision")
st.write("Streamlit은 전통적 머신러닝 데모 웹앱을 만드는 데에도 유용하다.")

# 1. 보여줄 파일 업로드 기능
uploaded_file = st.file_uploader("업로드할 이미지를 선택", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
else:
    image = Image.open(requests.get("https://picsum.photos/200/120", stream=True).raw)

# 2. 엣지 검출  
edges = cv2.Canny(np.array(image), 100, 200)

# 3. 각 탭에서 엣지와 원본 이미지 표현
tab1, tab2 = st.tabs(["엣지 검출 결과", "원본 이미지"])
tab1.image(edges, use_container_width=True)
tab2.image(image, use_container_width=True)