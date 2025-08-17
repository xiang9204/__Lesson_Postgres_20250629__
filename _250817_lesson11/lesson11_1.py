
# 當輸出df變數時,st.write()會自動執行
"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import datasource


st.sidebar.title("台鐵車站資訊")
st.sidebar.header("2023年各站進出人數")
st.subheader("進出站人數顯示區")

@st.cache_resource
def get_stations_data():
    """取得車站資料"""
    return datasource.get_stations_names()

station_names = get_stations_data()

if station_names is None:
    st.error("無法取得車站資料，請檢查資料庫連線或查詢是否正確。")
    st.stop()



# 詢問 AI 的敘述，使其自動生成 code /
# sidebar 要先顯示常用的車站
# 使用者可以很快的選擇
# 如果不常用的車站名稱，再使用 selectbox


# 定義常用車站
common_stations = ["台北", "板橋", "新竹", "台中", "高雄", "其他"]

# sidebar 顯示常用車站按鈕
selected_common = st.sidebar.radio(
    "常用車站快速選擇",
    options=common_stations,
    index=0
)

# 判斷是否選擇其他車站
if selected_common == "其他":
        station = st.sidebar.selectbox(
        "請選擇車站",
        station_names,
    )    
else:
# 若未選擇常用車站，則顯示所有車站選擇
    station = selected_common

st.write("您選擇的車站:", station)

