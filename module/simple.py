# -*- coding: utf-8 -*-

# Copyright (c) 2014, Menno Smits
# Released subject to the New BSD License
# Please see http://en.wikipedia.org/wiki/BSD_licenses
# modified by Jack Wang

from __future__ import unicode_literals
import email

from imapclient import IMAPClient

from util import to_unicode
from module import settings


host = settings.get('HOST')
username = settings.get('USERNAME')
password = settings.get('PASSWORD')
ssl = False

server = IMAPClient(host, use_uid=True, ssl=ssl)
server.login(username, password)

list_folders = server.list_folders()
for foldername in list_folders:
    print foldername
# studyfolder = "我的文件夹/study".decode('utf-8').encode('utf-8')
select_info = server.select_folder(u'\u5176\u4ed6\u6587\u4ef6\u5939/test')
print('%d messages in study' % select_info['EXISTS'])

messages = server.search(['NOT', 'DELETED'])
print("%d messages that aren't deleted" % len(messages))

print("Messages:")
# response = server.fetch(messages, ['FLAGS', 'ENVELOPE'])
response = server.fetch(messages, ['RFC822'])
# response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE'])
for msgid, data in response.iteritems():
    # envelop = data[b'ENVELOPE']
    # subject = envelop.subject
    # print('   ID %d: %s bytes, flags=%s' % (msgid,
    # subject,
    #                                         data[b'FLAGS'],))
    messageString = data['RFC822']
    msgStringParsed = email.message_from_string(messageString)
    subject = email.Header.decode_header(msgStringParsed["Subject"])
    sub = to_unicode(subject[0][0], subject[0][1])

    print 'Date:%s\nFrom:%s\nSubject:%s\n%s' % \
          (msgStringParsed['date'], msgStringParsed['From'], sub, msgStringParsed.get_payload())
