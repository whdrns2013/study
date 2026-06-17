# 10.javascript.py
# import streamlit as st
# import streamlit.components.v1 as components

# st.title("10. Streamlit에서 Javascript 사용하기")
# st.write("만약 프론트에서 처리할 데이터가 많다면? Javascript를 써보자")
# st.write("브라우저 기반 스톱워치")

# # 1. Javascript
# components.html(
#     """
#     <div style="font-family: sans-serif; text-align: center;">
#       <h1 id="display">00:00.00</h1>
#       <button onclick="start()">시작</button>
#       <button onclick="stop()">정지</button>
#       <button onclick="reset()">초기화</button>
#     </div>

#     <script>
#       let startTime;
#       let elapsed = 0;
#       let timerInterval;
#       let running = false;

#       function updateDisplay() {
#         const time = running ? Date.now() - startTime + elapsed : elapsed;

#         const minutes = Math.floor(time / 60000);
#         const seconds = Math.floor((time % 60000) / 1000);
#         const centiseconds = Math.floor((time % 1000) / 10);

#         document.getElementById("display").innerText =
#           String(minutes).padStart(2, "0") + ":" +
#           String(seconds).padStart(2, "0") + "." +
#           String(centiseconds).padStart(2, "0");
#       }

#       function start() {
#         if (!running) {
#           startTime = Date.now();
#           timerInterval = setInterval(updateDisplay, 50);
#           running = true;
#         }
#       }

#       function stop() {
#         if (running) {
#           elapsed += Date.now() - startTime;
#           clearInterval(timerInterval);
#           running = false;
#           updateDisplay();
#         }
#       }

#       function reset() {
#         clearInterval(timerInterval);
#         startTime = null;
#         elapsed = 0;
#         running = false;
#         updateDisplay();
#       }

#       updateDisplay();
#     </script>
#     """,
#     height=250,
# )
import streamlit as st
from components.stopwatch import stopwatch

st.title("스톱워치")

result = stopwatch(key="stopwatch")

st.write("Python으로 받은 값")

if result is None:
    st.info("아직 기록된 시간이 없습니다.")
else:
    start_datetime = result.get("start_datetime")
    elapsed_ms = result.get("elapsed_ms", 0)

    st.write("시작일시:", start_datetime)
    st.write("경과시간(ms):", elapsed_ms)
    st.write("경과시간(초):", round(elapsed_ms / 1000, 2))

    if start_datetime:
        st.success(f"시작일시 {start_datetime}, 경과시간 {elapsed_ms / 1000:.2f}초")