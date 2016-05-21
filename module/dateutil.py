# -*- coding: utf-8 -*-
import calendar

import datetime

__author__ = 'Jack'


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day)


def convert_str2date(time_str):
    return datetime.datetime(*[int(item) for item in time_str.split('-')])
