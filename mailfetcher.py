# -*- coding: utf-8 -*-

# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses
# modified by Jack Wang

from __future__ import unicode_literals
import email

from imapclient import IMAPClient

from module.mailutil import get_subject, get_sender, is_reply_mail
from module import settings


def save_full_messages(search_ids=[]):
    sum_num = 0
    check_num = 0
    for msgid in search_ids:
        check_num += 1
        print "checking... %s" % check_num
        response = server.fetch(msgid, ['RFC822'])
        messageString = response[msgid]['RFC822']
        msgStringParsed = email.message_from_string(messageString)
        subject = get_subject(msgStringParsed['Subject'])
        sender = get_sender(msgStringParsed['From'])
        if is_reply_mail(subject):
            continue
        sum_num += 1
        print 'From:%s Subject:%s\n' % (sender, subject)
    return sum_num


def get_from_addr_from_envelope(envelope):
    return envelope.from_[0].__str__()


def list_message_headers(search_ids=[]):
    senderlist = []
    check_num = 0
    for msgid in search_ids:
        check_num += 1
        print "checking... %s" % check_num
        response = server.fetch(msgid, ['ENVELOPE'])
        envelope = response[msgid]['ENVELOPE']
        subject = get_subject(envelope.subject)
        sender = get_sender(get_from_addr_from_envelope(envelope))
        if is_reply_mail(subject):
            continue
        senderlist.append(sender)
        print 'From:%s Subject:%s\n' % (sender, subject)
    return senderlist


host = settings.get('EMAIL_HOST')
username = settings.get('EMAIL_USERNAME')
password = settings.get('EMAIL_PASSWORD')
ssl = False

server = IMAPClient(host, use_uid=True, ssl=ssl)
server.login(username, password)
select_info = server.select_folder(u'\u5176\u4ed6\u6587\u4ef6\u5939/study')
print('%d messages in study' % select_info['EXISTS'])

messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted" % len(messages))
print messages
print("Messages:")
senders = list_message_headers(messages)
# total_subjects = save_full_messages(messages)

print "总数为 %s" % len(senders)