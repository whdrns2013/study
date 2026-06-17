# 08_file_upload.py
import streamlit as st
from PIL import Image
import pandas as pd
import base64

st.title("08. File Upload")

# 0. 이미지를 담고 있는 리스트
if "image_list" not in st.session_state:
    image_list = []
    st.session_state.image_list = image_list

# 1. 파일 업로드
uploaded_file = st.file_uploader("업로드할 이미지를 선택", type=["jpg", "jpeg", "png"])

# 2. 파일 업로드시 데이터프레임에 추가
if uploaded_file:
    file_bytes = uploaded_file.getvalue()
    encoded_image = base64.b64encode(file_bytes).decode()
    mime_type = uploaded_file.type
    st.session_state.image_list.append(
        {
            "id": uploaded_file.file_id,
            "image_name": uploaded_file.name,
            "image": f"data:{mime_type};base64,{encoded_image}",
            "size": uploaded_file.size,
        }
        )

# 3. 데이터프레임 표출
config = {"image":st.column_config.ImageColumn()}
st.dataframe(pd.DataFrame(st.session_state.image_list), column_config=config, use_container_width=True)