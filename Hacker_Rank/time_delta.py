#URL: https://www.hackerrank.com/challenges/python-time-delta/problem

def time_delta(t1, t2):
    from datetime import datetime as dt
    fmt = "%a %d %b %Y %H:%M:%S %z"
    return str(int(abs( (dt.strptime(t1,fmt) - dt.strptime(t2,fmt)).total_seconds() )))
