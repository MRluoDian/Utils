# -*- coding: utf-8-*-
import json
import datetime
import pytz
import time


def utc_to_local(country_code, utc_time_str, local_format="%Y-%m-%d %H:%M:%S"):
    utc_time_str = utc_time_str[:-1] + "+00:00"
    local_tz = pytz.timezone(pytz.country_timezones(country_code)[0])
    utc_dt = datetime.datetime.strptime(utc_time_str, '%Y-%m-%dT%H:%M:%S+00:00')
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    date_time = datetime.datetime.strptime(local_dt.strftime(local_format), local_format)
    return date_time


def local_to_utc(local_time: datetime):
    time_struct = time.mktime(local_time.timetuple())
    utc_st = str(datetime.datetime.utcfromtimestamp(time_struct))
    return f'{"T".join(utc_st.split(" "))}Z'


def utc_to_bj(utc_time_str, utc_format='%Y-%m-%dT%H:%M:%SZ'):
    local_tz = pytz.timezone('Asia/Shanghai')
    local_format = "%Y-%m-%d %H:%M:%S"
    utc_dt = datetime.datetime.strptime(utc_time_str, utc_format)
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz).replace(microsecond=0)
    time_data = datetime.datetime.strptime(local_dt.strftime(local_format), local_format)
    return time_data
