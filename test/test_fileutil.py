# -*- coding: utf-8 -*-

from unittest2 import TestCase

from module.fileutil import write_cvs_items


__author__ = 'Jack'


class FileUtilTest(TestCase):
    def setUp(self):
        pass

    def test_write_down(self):
        rows = ["testA1|testA2", "testB1|testB2", "testC1|testC2"]
        write_cvs_items(rows=rows)

    def test_write_down_with_chinese(self):
        rows = [u"测试A1|测试A2", u"测试B1|测试B2", u"测试C1|测试C2"]
        write_cvs_items(rows=rows)