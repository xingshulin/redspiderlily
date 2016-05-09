# -*- coding: utf-8 -*-
from email.header import decode_header
__author__ = 'Jack'


def to_unicode(s, encoding):
    if encoding:
        return s.decode(encoding)
    else:
        return s


def parse_address(msg_addr):
    msg_addr = msg_addr.strip(' ')
    msg_pair = msg_addr.split(' ')
    if len(msg_pair) == 2:
        mail_name = decode_header((msg_pair[0]).strip('\"'))[0]
        mail_address = msg_pair[1]
        full_address = to_unicode(mail_name[0], mail_name[1]) + mail_address
    else:
        full_address = msg_addr
    return full_address


def get_sender(msg_from):
    sender = parse_address(msg_from)
    return sender


def get_receivers(msg_to):
    msg_to = msg_to.replace('\n', '')
    msg_receiver_list = msg_to.split(',')
    receivers = []
    for msg_receiver in msg_receiver_list:
        receivers.append(parse_address(msg_receiver))
    return receivers


def get_subject(msg_subject):
    if isinstance(msg_subject, bytes):
        msg_subject = msg_subject.decode('utf-8')
    subject = decode_header(str(msg_subject))
    return to_unicode(subject[0][0], subject[0][1])


def is_reply_mail(_subject):
    _subject = _subject
    return ("回复" in _subject.lower()) or ("re:" in _subject.lower())


def combine_sender_n_subject(sender, subject):
    return sender + '|' + subject.replace(',', '_')