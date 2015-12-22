# -*- coding: utf-8 -*-
import email
from operator import add
import sys

from unittest2 import TestCase
from module import settings

from module.mailutil import get_sender, get_subject, get_receivers, is_reply_mail

__author__ = 'Jack'

def get_charset(message, default="ascii"):
    # Get the message charset
    return message.get_charset()
    return default


def process_single_part(part, file_path):
    content_type = part.get_content_type()
    print content_type
    filename = part.get_filename()
    print 'file %s' % filename
    charset = get_charset(part)
    # 是否有附件
    if filename:
        h = email.Header.Header(filename)
        dh = email.Header.decode_header(h)
        fname = dh[0][0]
        encodeStr = dh[0][1]
        if encodeStr != None:
            if charset == None:
                fname = fname.decode(encodeStr, 'gbk')
            else:
                fname = fname.decode(encodeStr, charset)
        data = part.get_payload(decode=True)
        print('Attachment : ' + fname)
        # 保存附件
        if fname != None or fname != '':
            savefile(fname, data, file_path)
    else:
        if content_type in ['text/plain']:
            suffix = '.txt'
        if content_type in ['text/html']:
            suffix = '.htm'
        if charset == None:
            mailContent = part.get_payload(decode=True)
        else:
            mailContent = part.get_payload(decode=True).decode(charset)

    print mailContent, suffix
    return mailContent, suffix


def get_body(msg, file_path):
    for part in msg.walk():
        if not part.is_multipart():
            mail_content, suffix = process_single_part(part, file_path)
    return mail_content, suffix


class SimpleTest(TestCase):
    def setUp(self):
        global msgStringParsed
        txt = open("test_email.txt")
        test_email = txt.read()
        msgStringParsed = email.message_from_string(test_email)

    def test_format_from(self):
        print msgStringParsed["From"]
        from_txt = ""
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

    def test_format_body(self):
        file_path = "./"
        mailContent, suffix = get_body(msgStringParsed, file_path)

    def test_string(self):
        if "tech@xingshulin.com" in u"技术部<tech@xingshulin.com>":
            print "cool"

    def test_is_reply_mail_when_contains_re(self):
        subject_with_chinese = u"Re: 回复：浅谈懒人模式"
        subject_with_english = u"Re: test for imapclient"
        subject_with_no_re = u"浅谈懒人模式"
        self.assertTrue(is_reply_mail(subject_with_chinese))
        self.assertTrue(is_reply_mail(subject_with_english))
        self.assertFalse(is_reply_mail(subject_with_no_re))