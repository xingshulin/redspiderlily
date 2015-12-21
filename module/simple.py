# -*- coding: utf-8 -*-

# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses
# modified by Jack Wang

from __future__ import unicode_literals
import email

from imapclient import IMAPClient

from mailutil import get_subject, get_sender
from module import settings


host = settings.get('HOST')
username = settings.get('USERNAME')
password = settings.get('PASSWORD')
ssl = False

server = IMAPClient(host, use_uid=True, ssl=ssl)
server.login(username, password)

select_info = server.select_folder(u'\u5176\u4ed6\u6587\u4ef6\u5939/test')
print('%d messages in study' % select_info['EXISTS'])

messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted" % len(messages))

print("Messages:")
response = server.fetch(messages, ['RFC822'])
for msgid, data in response.iteritems():
    messageString = data['RFC822']
    msgStringParsed = email.message_from_string(messageString)
    subject = get_subject(msgStringParsed['Subject'])
    sender = get_sender(msgStringParsed['From'])
    date = msgStringParsed['date']
    print 'Date:%s\nFrom:%s\nSubject:%s\n%s' % \
          (date, sender, subject, msgStringParsed.get_payload())
