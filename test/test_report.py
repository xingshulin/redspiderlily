# -*- coding: utf-8 -*-
from datetime import date
import mock

from unittest2 import TestCase

from module.report import is_odd_week, is_even_week, compose_odd_week_email, generate, compose_even_week_email
from test.constant import ONLINE_TEST_WITH_REAL_MAIL_AND_DB, ONLINE_TEST_SEND_MAIL

__author__ = 'Jack'


class ReportTest(TestCase):
    _from = None
    _to = None

    def setUp(self):
        global _from, _to
        _from = date(2016, 5, 2)
        _to = date(2016, 5, 9)
        pass

    @mock.patch('module.report.get_mail_senders_and_subjects_by_duration',
                return_value=(['QingCloud<noreply+0@qingcloud.com>',
                               'QingCloud<noreply+2@qingcloud.com>',
                               'QingCloud<noreply+3@qingcloud.com>'],
                              ['[QingCloud] 节点 "PEK1" 的 主机"prod-es-23" 监控告警状态变为: 正常',
                               '[QingCloud] 节点 "PEK1" 的 主机"prod-db-136" 监控告警状态变为: 正常',
                               '[QingCloud] 节点 "PEK1" 的 公网IP"xsl_production_ip" 监控告警状态变为: 告警']))
    def test_generate_report_when_target_duration_has_been_fixed(self, retrieve):
        """----------------Verify behavior-----------------------------"""
        global _from, _to
        if not ONLINE_TEST_SEND_MAIL:
            return
        _from = date(2016, 5, 2)
        _to = date(2016, 5, 9)
        result = generate(_from, _to)
        self.assertTrue(result)

    @mock.patch('module.report.get_mail_senders_and_subjects_by_duration',
                return_value=([], []))
    def test_generate_report_failed_when_target_duration_has_been_fixed_but_no_mail(self, retrieve):
        """----------------Verify behavior-----------------------------"""
        result = generate(_from, _to)
        self.assertFalse(result)

    def test_is_odd_week_when_gap_equal_to_7(self):
        self.assertTrue(is_odd_week(date(2016, 5, 9), date(2016, 5, 16)))

    def test_is_even_week_when_gap_equal_to_14(self):
        self.assertFalse(is_odd_week(date(2016, 5, 9), date(2016, 5, 23)))
        self.assertTrue(is_even_week(date(2016, 5, 9), date(2016, 5, 23)))

    def test_is_summary_when_gap_not_equal_to_7_or_14(self):
        self.assertFalse(is_odd_week(date(2016, 4, 9), date(2016, 5, 23)))
        self.assertFalse(is_even_week(date(2016, 4, 9), date(2016, 5, 23)))

    def test_compose_odd_email_can_zip_senders_and_subjects_into_a_msg_dictionary(self):
        test_file = open('template/odd_email_test_file.html', 'r', encoding='utf-8')
        test_body = test_file.read().replace('\n', '').replace(' ', '')
        test_content = {'to': 'wangzhe@xingshulin.com',
                        'subject': '[双周学习分享]单周总结',
                        'body': test_body}

        senders = ['QingCloud<noreply+0@qingcloud.com>', 'john@xingshulin.com']
        subjects = ['abc', 'bcd']

        msg_content = compose_odd_week_email(senders, subjects)
        self.assertEqual(msg_content['to'], test_content['to'])
        self.assertEqual(msg_content['subject'], test_content['subject'])
        self.assertEqual(msg_content['body'].replace('\n', '').replace(' ', ''), test_content['body'])

    def test_compose_even_week_email_can_zip_senders_and_subjects_into_a_msg_dictionary(self):
        test_file = open('template/even_email_test_file.html', 'r', encoding='utf-8')
        test_body = test_file.read().replace('\n', '').replace(' ', '')
        test_content = {'to': 'wangzhe@xingshulin.com',
                        'subject': '[双周学习分享]双周汇总',
                        'body': test_body}

        senders = ['QingCloud<noreply+0@qingcloud.com>', 'john@xingshulin.com']
        subjects = ['abc', 'bcd']

        msg_content = compose_even_week_email(authors=senders, topics=subjects)
        self.assertEqual(msg_content['to'], test_content['to'])
        self.assertEqual(msg_content['subject'], test_content['subject'])
        self.assertEqual(msg_content['body'].replace('\n', '').replace(' ', ''), test_content['body'])
