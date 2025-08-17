
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

@st.cache_data
def get_stations_data():
    """取得車站資料"""
    return datasource.get_stations_names()

@st.cache_data
def get_date_range():
    """取得日期範圍"""
    return datasource.get_date_range()

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


date_range = get_date_range()
if date_range is None:
    st.error("無法取得日期範圍，請檢查資料庫連線或查詢是否正確。")
    st.stop()

# 轉換為 datetime.date（如果 datasource 回傳字串）
try:
    min_date, max_date = date_range
    if isinstance(min_date, str):
        min_date = date_range.date.fromisoformat(min_date)
    if isinstance(max_date, str):
        max_date = date_range.date.fromisoformat(max_date)
except Exception as e:
    st.error(f"無法解析日期範圍: {e}")
    st.stop()

# sidebar 顯示日期範圍選擇器，僅限於取得的日期範圍
selected_dates = st.sidebar.date_input(
    "選擇日期範圍",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)
# 如果使用者只選單一日期，將其視為起訖相同
if isinstance(selected_dates, tuple) and len(selected_dates) == 2:
    start_date, end_date = selected_dates
else:
    start_date = end_date = selected_dates













st.write("您選擇的車站:", station)
st.write("日期範圍:", start_date, "至", end_date)

# 請使用datasource.get_station_data_by_date 函數取得資料,並顯示資料
data = datasource.get_station_data_by_date(station, start_date, end_date)
if data is None:
    st.error("無法取得車站資料，請稍後再試。")
else:
    st.write("進出站人數資料:")
    for row in data:
        st.write(row)