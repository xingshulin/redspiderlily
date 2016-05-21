# -*- coding: utf-8 -*-
import datetime
from unittest2 import TestCase

from module.dateutil import add_months

__author__ = 'Jack'


class DateUtilTest(TestCase):
    def setUp(self):
        pass

    def test_write_down(self):
        x = "2015-01-30"
        _date = add_months(datetime.datetime(*[int(item) for item in x.split('-')]), 1)
        self.assertEqual(type(_date), datetime.date)
