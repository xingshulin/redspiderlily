# -*- coding: utf-8 -*-

import csv

__author__ = 'Jack'

mail_path = os.path.join(
    os.path.dirname(__file__), 'template'
)


def write_cvs_items(filename='mails.csv', rows=[]):
    csvwriter = csv.writer(open(filename, 'w', newline='', encoding='utf-8'), delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for row in rows:
        items = row.split('|')
        csvwriter.writerow([item for item in items])


def read_mail_template(path='/odd_email.html'):
    return open(mail_path + path, 'r', encoding='utf-8').read()
