import time, PyOfficeRobot
import pandas as pd
from datetime import datetime
import requests, locale

def get_current_weather_without_api(city):
    base_url = f"https://wttr.in/{city}?format=3"

    response = requests.get(base_url)
    if response.status_code == 200:
        weather_info = response.text
        return weather_info
    else:
        return "Error fetching weather data"

def getDailyReport():
    res = DateMsg() + WeatherMsg()
    PyOfficeRobot.chat.send_message("akinaustin", res)

def DateMsg():
    current_date = datetime.now()
    year = str(current_date.year)
    month = str(current_date.month)
    day = str(current_date.day)
    weekday = current_date.strftime('%A')
    weekday_translation = {
        'Monday': '星期一',
        'Tuesday': '星期二',
        'Wednesday': '星期三',
        'Thursday': '星期四',
        'Friday': '星期五',
        'Saturday': '星期六',
        'Sunday': '星期日'
    }
    weekday_sts = {
        'Monday': '加油工作！！！',
        'Tuesday': '再接再厉！！！',
        'Wednesday': '这周已经过了一半了！',
        'Thursday': '过了周四就是周末！',
        'Friday': '马上就要周末了啊啊啊啊啊',
        'Saturday': '哈哈哈哈哈哈哈哈哈哈哈哈',
        'Sunday': '哈哈哈哈哈哈哈哈哈'
    }
    response_data = '' + year + '年' + month + '月' + day + '日 ' + weekday_translation[weekday] + '{ctrl}{ENTER}' + weekday_sts[weekday] + '{ctrl}{ENTER}'
    return response_data

def WeatherMsg():
    hz_weather = str(get_current_weather_without_api("hangzhou"))
    sh_weather = str(get_current_weather_without_api("shanghai"))
    mun_weather = str(get_current_weather_without_api("munchen"))

    return '今日天气:' + '{ctrl}{ENTER}' + '     ' + hz_weather + '{ctrl}{ENTER}' +  '     ' + sh_weather + '{ctrl}{ENTER}' +  '     ' + mun_weather + '{ctrl}{ENTER}'

def FootballMsg():
    flag = 0
    if flag==0:
        return ''
    else:
        return '球赛信息: '



if __name__ == "__main__":
    print(WeatherMsg())

