# -*- coding: utf-8 -*-
"""
=============================================================
Created on Mar 15 2015
@author: c
Please download jholiday here:
    http://www.h3.dion.ne.jp/~sakatsu/index.htm
This code help you to download Japan's weather/holiday data.
pyquery, jholiday, datetime, numpy is needed.
=============================================================
"""
from pyquery import PyQuery as pq
import jholiday
import datetime
import numpy as np


def getnahaWeather(title):
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/10min_s1.php?'
           'prec_no=91&block_no=47936&year=%d&month=%d&day=%d&view=p1'
           % (title.year, title.month, title.day)
           )
    #  pyquery
    query = pq(url, parser='html')
    day = query('.data_0_0')
    precipitation = range(144)
    for i, item in enumerate(day):
        if i % 10 == 2:
            precipitation[int(i/10)] = "Precipitation(mm): %s"\
                % pq(item).text()
    rainfall = np.repeat(precipitation, 2)
    return rainfall


def kyotoWeather(title):
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?'
           'prec_no=61&block_no=47759&year=%d&month=%d&view=p1'
           % (title.year, title.month))
    query = pq(url, parser='html')
    day = query('.data_0_0')
    dayW = pq(day[20*title.day-2:20*title.day]).text().encode('utf8')
    rainfall0 = pq(day[3+20*(title.day-1)]).text()
    try:
        rainfall = float(rainfall0)
    except:
        rainfall = 0
    return dayW, rainfall


def sendaiWeather(title):
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?'
           'prec_no=34&block_no=47590&year=%d&month=%d&view=p1'
           % (title.year, title.month))
    query = pq(url, parser='html')
    day = query('.data_0_0')
    dayW = pq(day[20*title.day-2:20*title.day]).text().encode('utf8')
    rainfall0 = pq(day[3+20*(title.day-1)]).text()
    try:
        rainfall = float(rainfall0)
    except:
        rainfall = 0
    return dayW, rainfall


def nahaWeather(title):
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?'
           'prec_no=91&block_no=47936&year=%d&month=%d&view=p1'
           % (title.year, title.month))
    query = pq(url, parser='html')
    day = query('.data_0_0')
    dayW = pq(day[20*title.day-2:20*title.day]).text().encode('utf8')
    rainfall0 = pq(day[3+20*(title.day-1)]).text()
    print rainfall0
    try:
        rainfall = float(rainfall0)
    except:
        rainfall = 0
    return dayW, rainfall


def tokyoWeather(title):
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?'
           'prec_no=44&block_no=47662&year=%d&month=%d&view=p1'
           % (title.year, title.month))
    query = pq(url, parser='html')
    day = query('.data_0_0')
    dayW = pq(day[20*title.day-2:20*title.day]).text().encode('utf8')
    rainfall0 = pq(day[3+20*(title.day-1)]).text()
    print rainfall0
    try:
        rainfall = float(rainfall0)
    except:
        rainfall = 0
    return dayW, rainfall


def yokohamaWeather(title):
    url = ('http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?'
           'prec_no=46&block_no=47670&year=%d&month=%d&view=p1'
           % (title.year, title.month))
    query = pq(url, parser='html')
    day = query('.data_0_0')
    dayW = pq(day[20*title.day-2:20*title.day]).text().encode('utf8')
    rainfall0 = pq(day[3+20*(title.day-1)]).text()
    print rainfall0
    try:
        rainfall = float(rainfall0)
    except:
        rainfall = 0
    return dayW, rainfall


def dayType(title):
    if jholiday.holiday_name(date=title) is not None:
        dayP = jholiday.holiday_name(date=title).encode('utf8')
        dayT = "holiday"
    else:
        dayP = title.strftime('%a')
        if title.weekday() not in [5, 6]:
            dayT = "weekday"
        else:
            dayT = "weekend"
    return dayP, dayT


if __name__ == '__main__':
    title = datetime.date(2013, 1, 1)
    yokohamaw = yokohamaWeather(title)
    tokyow = tokyoWeather(title)
    naha = nahaWeather(title)
    kyoto = kyotoWeather(title)
    sendai = sendaiWeather(title)
    dayT, dayP = dayType(title)
    print dayT, dayP, yokohamaw, tokyow, naha, kyoto, sendai
