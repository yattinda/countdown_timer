import jpholiday

def between_holiday_num(today_datetime, target_datetime):
    holidays_list = jpholiday.between(today_datetime, target_datetime)
    for holiday in holidays_list:
        # 土日かぶったときの除外
        if holiday(0).weekday > 4:
            continue
        holiday_num += 1
    return holiday_num

