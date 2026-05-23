# 02_markdown.py
import streamlit as st

st.title("Ai there!👋")

content = """

## Intro  

Jongya의 개발 블로그입니다.
세상의 다양한 문제들을 해결하는 개발자가 되고 싶습니다.

**:rainbow[Streamlit]** 은 마크다운 문법을 표함해 아래와 같은 컨텐츠를 표현할 수 있습니다.  

| 기능      | 설명                                  |
| ------- | ----------------------------------- |
| 텍스트 출력  | 제목, 설명, Markdown 표시                 |
| 데이터 표시  | DataFrame, 테이블, JSON 출력             |
| 차트      | 선 그래프, 막대 그래프, 지도, Plotly/Altair 연동 |
| 입력 위젯   | 버튼, 슬라이더, 체크박스, 파일 업로드              |
| 레이아웃    | 사이드바, 탭, 컬럼, 컨테이너                   |
| 상태 관리   | 사용자의 입력 상태 저장                       |
| AI/챗 UI | 채팅 입력창, 메시지 형태 UI 구성                |
| 배포      | Streamlit Community Cloud 등으로 공유 가능 |

이번 포스팅 시리즈에서는 스트림릿을 다뤄보도록 하겠습니다.  
"""

# markdown
st.markdown(content)

# button
if st.button("Send baloons"):
    st.balloons()