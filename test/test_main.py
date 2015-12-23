# -*- coding: utf-8 -*-

from unittest2 import TestCase

from main import filter_colleagues_who_is_not_in_senders


__author__ = 'Jack'


class MainTest(TestCase):
    def setUp(self):
        pass

    def test_filter_colleagues_who_is_not_in_senders(self):
        senders = ["testA1@xingshulin.com", "testB1@xingshulin.com", "testC1@xingshulin.com"]
        colleagues = ["testA1", "testA2", "testB1", "testC1"]
        not_send_list = filter_colleagues_who_is_not_in_senders(senders, colleagues)
        self.assertEqual(len(not_send_list), 1)
        self.assertEqual(not_send_list[0], "testA2")
