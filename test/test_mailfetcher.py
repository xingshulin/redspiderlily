# -*- coding: utf-8 -*-

from unittest2 import TestCase

from module.mailutil import combine_sender_n_subject

__author__ = 'Jack'


class MailFetcherTest(TestCase):
    def setUp(self):
        pass

    def test_combine_sender_n_subject_in_right_way_when_subject_contains_comma(self):
        subject = "Complete API Design, Build, and Document Process"
        sender = "test_sender"
        result = combine_sender_n_subject(sender, subject)
        self.assertEqual("test_sender|Complete API Design_ Build_ and Document Process", result)
