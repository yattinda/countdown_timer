from datetime import datetime, time
from holiday import between_holiday_num
import workdays


def count(target_datetime, holiday_omit):
    target_datetime = datetime.combine(target_datetime, time(0, 0, 0))
    now_datetime = datetime.utcnow()
    remain_datetime = target_datetime - now_datetime
    d = workdays.networkdays(now_datetime, target_datetime)
    if holiday_omit:
        d = d - between_holiday_num(now_datetime, target_datetime)
    m, s = divmod(remain_datetime.seconds, 60)
    h, m = divmod(m, 60)
    return d, h, m, s
