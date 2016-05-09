# -*- coding: utf-8 -*-
from email import message_from_string
from email.header import decode_header, Header
import sys

from unittest2 import TestCase

from module.mailutil import get_sender, get_subject, get_receivers, is_reply_mail

__author__ = 'Jack'

def get_charset(message, default="ascii"):
    # Get the message charset
    return message.get_charset()


def savefile(fname, data, file_path):
    pass


def process_single_part(part, file_path):
    content_type = part.get_content_type()
    print(content_type)
    filename = part.get_filename()
    print('file %s' % filename)
    charset = get_charset(part)
    # 是否有附件
    if filename:
        h = Header(filename)
        dh = decode_header(h)
        fname = dh[0][0]
        encodeStr = dh[0][1]
        if encodeStr is not None:
            if charset is None:
                fname = fname.decode(encodeStr, 'gbk')
            else:
                fname = fname.decode(encodeStr, charset)
        data = part.get_payload(decode=True)
        print('Attachment : ' + fname)
        # 保存附件
        if (fname is not None) or (fname != ''):
            savefile(fname, data, file_path)
    else:
        if content_type in ['text/plain']:
            suffix = '.txt'
        if content_type in ['text/html']:
            suffix = '.htm'
        if charset is None:
            mail_content = part.get_payload(decode=True)
        else:
            mail_content = part.get_payload(decode=True).decode(charset)

    print(mail_content, suffix)
    return mail_content, suffix


def get_body(msg, file_path):
    for part in msg.walk():
        if not part.is_multipart():
            mail_content, suffix = process_single_part(part, file_path)
    return mail_content, suffix


class SimpleTest(TestCase):
    msg_string_parsed = None

    def setUp(self):
        global msg_string_parsed
        txt = open("test_email.txt")
        test_email = txt.read()
        msg_string_parsed = message_from_string(test_email)

    def test_format_from(self):
        print(msg_string_parsed["From"])
        sender = get_sender(msg_string_parsed["From"])
        self.assertEqual(u"文迪<wendi@xingshulin.com>", sender)

    def test_format_to(self):
        receivers = get_receivers(msg_string_parsed["to"])
        self.assertEqual(u"qinhan<qinhan@xingshulin.com>", receivers[0])
        self.assertEqual(u"王哲<wangzhe@xingshulin.com>", receivers[1])
        self.assertNotEqual(u"技术部<tech@xingshulin.com>", receivers[0])

    def test_format_subject_and_date(self):
        subject = get_subject(msg_string_parsed["Subject"])
        self.assertEqual("Re: test for imapclient", subject)
        mail_date = msg_string_parsed["Date"]
        self.assertEqual("Mon, 21 Dec 2015 20:03:54 +0800", mail_date)

    @staticmethod
    def test_format_body():
        file_path = "./"
        mail_content, suffix = get_body(msg_string_parsed, file_path)

    @staticmethod
    def test_string():
        if "tech@xingshulin.com" in u"技术部<tech@xingshulin.com>":
            print("cool")

    def test_is_reply_mail_when_contains_re(self):
        subject_with_chinese = u"Re: 回复：浅谈懒人模式"
        subject_with_english = u"Re: test for imapclient"
        subject_with_no_re = u"浅谈懒人模式"
        self.assertTrue(is_reply_mail(subject_with_chinese))
        self.assertTrue(is_reply_mail(subject_with_english))
        self.assertFalse(is_reply_mail(subject_with_no_re))