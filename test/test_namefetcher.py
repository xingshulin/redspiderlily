# -*- coding: utf-8 -*-
import mock
from unittest2 import TestCase
from module.namefetcher import get_names

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
        print "second name is %s" % result[1]
        self.assertEqual(result[0], 'prettyboy')
        self.assertEqual(result[2], 'spikerlily')


