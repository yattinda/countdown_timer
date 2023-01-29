import jpholiday
import datetime

def between_holiday_num(today_datetime, target_datetime):
    holiday_num = jpholiday.between(today_datetime, target_datetime)
    return holiday_num + 1

