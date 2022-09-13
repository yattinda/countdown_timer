import streamlit as st
from counter import count
import time

with st.sidebar:
    input_date = st.date_input("when is the target date?")
    
#プレースホルダー
count_area = st.empty()

while(True):
    d, h, m, s = count(input_date)
    display = f'{d:02} days {h:02}: {m:02} : {s:02}'
    count_area.title(display)
    time.sleep(1)
