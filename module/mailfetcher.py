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


def save_full_messages(search_ids=[], server=None):
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


def list_message_headers(search_ids=[], server=None):
    sender_list = []
    subject_list = []
    for msgid in search_ids:
        response = server.fetch(msgid, [b'ENVELOPE'])
        envelope = response[msgid][b'ENVELOPE']
        subject = get_subject(envelope.subject)
        sender = get_sender(get_from_addr_from_envelope(envelope))
        if is_reply_mail(subject):
            continue
        sender_list.append(sender)
        subject_list.append(subject)
        print('From:%s Subject:%s' % (sender, subject))
    return sender_list, subject_list


def get_mail_senders_and_subjects_by_duration(_from=date(2015, 5, 1), _to=date(2016, 5, 1)):
    server = IMAPClient(host, use_uid=True, ssl=ssl)
    server.login(username, password)
    select_info = server.select_folder(folder_study)
    print('%d messages in study' % select_info[b'EXISTS'])

    messages_since = server.search([u'SINCE', _from])
    messages_before = server.search([u'BEFORE', _to])
    messages = list(set(messages_since) & set(messages_before))
    print("%d messages that are in duration" % len(messages))

    print("Messages:")
    senders, subjects = list_message_headers(messages, server)
    # total_subjects = save_full_messages(messages, server)

    output_list = []
    for (sender, subject) in zip(senders, subjects):
        output_list.append(combine_sender_n_subject(sender, subject))
    write_cvs_items(rows=output_list)
    print("总数为 %s" % len(senders), len(subjects))

    server.logout()
    return senders, subjects
