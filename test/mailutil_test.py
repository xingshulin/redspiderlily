# -*- coding: utf-8 -*-
import email

from unittest2 import TestCase

from module.mailutil import get_sender, get_subject, get_receivers

__author__ = 'Jack'


class SimpleTest(TestCase):

    def setUp(self):
        global msgStringParsed
        txt = open("test_email.txt")
        test_email = txt.read()
        msgStringParsed = email.message_from_string(test_email)

    def test_format_from(self):
        sender = get_sender(msgStringParsed["From"])
        self.assertEqual(u"文迪<wendi@xingshulin.com>", sender)

    def test_format_to(self):
        receivers = get_receivers(msgStringParsed["to"])
        self.assertEqual(u"qinhan<qinhan@xingshulin.com>", receivers[0])
        self.assertEqual(u"王哲<wangzhe@xingshulin.com>", receivers[1])
        self.assertNotEqual(u"技术部<tech@xingshulin.com>", receivers[0])

    def test_format_subject_and_date(self):
        subject = get_subject(msgStringParsed["Subject"])
        self.assertEqual("Re: test for imapclient", subject)
        mail_date = msgStringParsed["Date"]
        self.assertEqual("Mon, 21 Dec 2015 20:03:54 +0800", mail_date)

