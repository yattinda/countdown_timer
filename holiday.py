import jpholiday

def between_holiday_num(now_datetime, target_datetime):
    holidays_list = jpholiday.between(now_datetime, target_datetime)
    for holiday in holidays_list:
        # 土日かぶったときの除外
        if holiday(0).weekday > 4:
            continue
        holiday_num += 1
    return holiday_num

