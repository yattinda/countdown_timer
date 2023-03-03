from datetime import datetime
import streamlit as st
from counter import count
import time
import streamlit_toggle as tog

st.title('n日後に死ぬワニ')

with st.sidebar:
    input_date = st.date_input(
        "when is the target date?", datetime(2023, 2, 15))
    holiday_omit = tog.st_toggle_switch(label="祝日をカウントしない",
                                        default_value=False,
                                        label_after=False,
                                        inactive_color='#D3D3D3',
                                        active_color="#11567f",
                                        track_color="#29B5E8"
                                        )

# プレースホルダー
count_area = st.empty()

while (True):
    d, h, m, s = count(input_date, holiday_omit)
    display = f'{d:02} days {h:02}: {m:02} : {s:02}'
    count_area.title(display)
    time.sleep(1)
