# 09_interactive.py
import streamlit as st

st.title("09. 유저 인터랙션")
st.write("사용자와 인터랙션 할 수 있는 다양한 도구들(Input Widget)도 준비되어있다.")

# 01. buttons  
st.markdown("##### (1) 버튼")
bc1, bc2, bc3 = st.columns(3)
with bc1: st.button(label="버튼 - Primary", key="코드단 식별자", on_click=st.balloons, type="primary")
with bc2: st.button(label="버튼 - Secondary(기본값)", key="Secondary", on_click=st.balloons, type="secondary", icon="😀")
with bc3: st.button(label="버튼 - tertiary", key="tertiary", on_click=st.balloons, type="tertiary")
st.space()

# 02. Selection  
st.markdown("##### (1) 선택방법")
sc11, sc12, sc13 = st.columns(3)
with sc11: st.checkbox(label="- 체크박스 -")
with sc12: st.color_picker(label="- 컬러 피커 -")
with sc13: st.feedback(options="faces")
sc21, sc22, sc23 = st.columns(3)
with sc21: st.multiselect(label="- 다중선택 -", options=["1번", "2번", "기타"])
with sc22: st.pills(label="- pills -", options=["1번", "2번", "기타"])
with sc23: st.radio(label="- 라디오버튼 -", options=["1번", "2번", "기타"])
st.segmented_control(label="segmented control")