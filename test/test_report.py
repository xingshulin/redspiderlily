# -*- coding: utf-8 -*-
from datetime import date

import collections
from unittest2 import TestCase

from module.report import is_odd_week, is_even_week, compose_odd_email, generate
from test.constant import ONLINE_TEST_WITH_REAL_MAIL_AND_DB

__author__ = 'Jack'


class ReportTest(TestCase):
    _from = None
    _to = None

    def setUp(self):
        global _from, _to
        _from = date(2015, 5, 1)
        _to = date(2016, 5, 1)
        pass

    def test_generate_report_when_target_duration_has_been_fixed(self):
        """----------------Verify behavior-----------------------------"""
        if not ONLINE_TEST_WITH_REAL_MAIL_AND_DB:
            return
        result = generate(_from, _to)

        self.assertEqual(result, date(2016, 5, 1))
        pass

    def test_is_odd_week_when_gap_equal_to_7(self):
        self.assertTrue(is_odd_week(date(2016, 5, 9), date(2016, 5, 16)))

    def test_is_even_week_when_gap_equal_to_14(self):
        self.assertFalse(is_odd_week(date(2016, 5, 9), date(2016, 5, 23)))
        self.assertTrue(is_even_week(date(2016, 5, 9), date(2016, 5, 23)))

    def test_is_summary_when_gap_not_equal_to_7_or_14(self):
        self.assertFalse(is_odd_week(date(2016, 4, 9), date(2016, 5, 23)))
        self.assertFalse(is_even_week(date(2016, 4, 9), date(2016, 5, 23)))

    def test_compose_odd_email_can_zip_senders_and_subjects_into_a_msg_dictionary(self):
        test_content = {'to': 'wangzhe@xingshulin.com', 'article_dict': {'a': 'me', 'b': 'you', 'c': 'he'},
                        'noncompliance_dict': None, 'compliance_dict': None, 'subject': '[双周学习分享]单周总结'}
        senders = ['a', 'b', 'c']
        subjects = ['me', 'you', 'he']
        msg_content = compose_odd_email(senders, subjects)
        self.assertEqual(msg_content['to'], test_content['to'])
        self.assertEqual(msg_content['compliance_dict'], test_content['compliance_dict'])
        self.assertEqual(msg_content['noncompliance_dict'], test_content['noncompliance_dict'])
        self.assertEqual(msg_content['subject'], test_content['subject'])
        self.assertEqual(msg_content['article_dict'], test_content['article_dict'])

