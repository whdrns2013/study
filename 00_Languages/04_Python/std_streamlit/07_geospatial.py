import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.title("07. 지리공간 시각화")

# 1. 지도 표시 위치 (서울)
lat = 37.5665
lon = 126.9780

# 2. 데이터 만들기
chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [lat, lon],
    columns = ["lat", "lon"]
)

# 3. 지도 시각화
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=lat,
        longitude=lon,
        zoom=10,
        pitch=50
    ),
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=chart_data,
            get_position="[lon, lat]",
            radius=150,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True
        ),
        pdk.Layer(
            "ScatterplotLayer",
            data=chart_data,
            get_position="[lon, lat]",
            get_color="[50, 200, 75, 160]",
            get_radius=150,
        )
    ]
))