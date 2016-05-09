# -*- coding: utf-8 -*-

# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses
# modified by Jack Wang

from datetime import date
import email

from imapclient import IMAPClient

from module.fileutil import write_cvs_items
from module.mailutil import get_subject, get_sender, is_reply_mail, combine_sender_n_subject
from module import settings


host = settings.get('EMAIL_HOST')
username = settings.get('EMAIL_USERNAME')
password = settings.get('EMAIL_PASSWORD')
folder_study = settings.get('FOLDER_STUDY')
ssl = False
server = IMAPClient(host, use_uid=True, ssl=ssl)


def save_full_messages(search_ids=[]):
    sum_num = 0
    check_num = 0
    for msgid in search_ids:
        check_num += 1
        print("checking... %s" % check_num)
        response = server.fetch(msgid, ['RFC822'])
        messageString = response[msgid]['RFC822']
        msgStringParsed = email.message_from_string(messageString)
        subject = get_subject(msgStringParsed['Subject'])
        sender = get_sender(msgStringParsed['From'])
        if is_reply_mail(subject):
            continue
        sum_num += 1
        print('From:%s Subject:%s\n' % (sender, subject))
    return sum_num


def get_from_addr_from_envelope(envelope):
    return envelope.from_[0].__str__()


def list_message_headers(search_ids=[]):
    sender_list = []
    subject_list = []
    date_list= []
    check_num = 0
    for msgid in search_ids:
        # check_num += 1
        # print "checking... %s" % check_num
        response = server.fetch(msgid, [b'ENVELOPE'])
        envelope = response[msgid][b'ENVELOPE']
        subject = get_subject(envelope.subject)
        _date = get_subject(envelope.date)
        sender = get_sender(get_from_addr_from_envelope(envelope))
        if is_reply_mail(subject):
            continue
        sender_list.append(sender)
        date_list.append(_date)
        subject_list.append(subject)
        print('From:%s Subject:%s' % (sender, subject))
    return sender_list, date_list, subject_list


def get_mail_titles():
    server.login(username, password)
    print(folder_study.encode('utf-8'))
    select_info = server.select_folder(folder_study)
    # select_info = server.select_folder(u'\u5176\u4ed6\u6587\u4ef6\u5939/trash')
    print('%d messages in trash' % select_info[b'EXISTS'])

    messages_since = server.search([u'UNSEEN', u'SINCE', date(2016, 4, 7)])
    messages_before = server.search([u'UNSEEN', u'BEFORE', date(2016, 5, 18)])
    messages = list(set(messages_since) & set(messages_before))
    print("%d messages that aren't seen" % len(messages))
    print(messages)

    # server.add_flags(messages, '\Seen')
# u'UNSEEN',
    print("Messages:")
    senders, dates, subjects = list_message_headers(messages)
    # total_subjects = save_full_messages(messages)
    print(dates)

    titles = []
    for (sender, subject) in zip(senders, subjects):
        titles.append(combine_sender_n_subject(sender, subject))
    write_cvs_items(rows=titles)
    print("总数为 %s" % len(senders))

    server.logout()
    return senders
