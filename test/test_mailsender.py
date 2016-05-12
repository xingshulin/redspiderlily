# -*- coding: utf-8 -*-
from datetime import date

from unittest2 import TestCase

from module.mailsender import send, generate_body
from test.constant import ONLINE_TEST_WITH_REAL_MAIL_AND_DB

__author__ = 'Jack'


class MailSenderTest(TestCase):
    _from = None
    _to = None

    def setUp(self):
        global _from, _to
        _from = date(2015, 5, 1)
        _to = date(2016, 5, 1)
        pass

    @staticmethod
    def test_smtp_sender_works():
        if not ONLINE_TEST_WITH_REAL_MAIL_AND_DB:
            return
        article_list = {'abc': 'jack@xingshulin.com', 'bcd': 'john@xingshulin.com'}
        test_content = {'to': 'wangzhe@xingshulin.com',
                        'subject': '[双周学习分享]单周总结',
                        'article_dict': article_list,
                        'compliance_dict': None,
                        'noncompliance_dict': None}
        send(test_content)

    def test_smtp_generate_body_properly(self):
        test_file = open('template/odd_email_test_file.html', 'r', encoding='utf-8')
        test_data = test_file.read().replace('\n', '').replace(' ', '')
        article_list = {'abc': 'QingCloud<noreply+0@qingcloud.com>', 'bcd': 'john@xingshulin.com'}
        test_content = {'to': 'wangzhe@xingshulin.com',
                        'subject': '[双周学习分享]单周总结',
                        'article_dict': article_list,
                        'compliance_dict': None,
                        'noncompliance_dict': None}
        result_data = generate_body(test_content).replace('\n', '').replace(' ', '')
        self.assertEqual(result_data, test_data)
