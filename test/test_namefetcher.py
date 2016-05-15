# -*- coding: utf-8 -*-
import mock
from unittest2 import TestCase

from module.namefetcher import get_names
from test.constant_in_test import ONLINE_TEST_PEER_QUANPIN_NAME_IN_TEST_NAME_FETCHER

__author__ = 'Jack'


class MailFetcherTest(TestCase):
    def setUp(self):
        pass

    @mock.patch('module.namefetcher.retrieve_data_from_db',
                return_value=((',prettyboy',), (',smartgirl',), (',spikerlily',)))
    def test_get_names(self, retrieve):
        """----------------Verify behavior-----------------------------"""
        result = get_names()
        self.assertEqual(len(result), 3)
        print("second name is %s" % result[1])
        self.assertEqual(result[0], 'prettyboy')
        self.assertEqual(result[2], 'spikerlily')

    def test_online_peer_quanpin_name_on_may_13th(self):
        """----------------Verify behavior-----------------------------"""
        if not ONLINE_TEST_PEER_QUANPIN_NAME_IN_TEST_NAME_FETCHER:
            return
        result = get_names()
        self.assertEqual(len(result), 53)

