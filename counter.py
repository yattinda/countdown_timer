from datetime import datetime, time
import workdays

def count(grad_time):
    grad_time = datetime.combine(grad_time, time(0, 0, 0))
    now_time = datetime.utcnow()
    remain_time = grad_time - now_time
    d = workdays.networkdays(now_time, grad_time)
    m, s = divmod(remain_time.seconds, 60)
    h, m = divmod(m, 60)
    return d, h, m, s
