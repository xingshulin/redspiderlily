# -*- coding: utf-8 -*-

import csv


__author__ = 'Jack'


def write_cvs_items(filename='mails.csv', rows=[]):
    csvwriter = csv.writer(open(filename, 'wb'), delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for row in rows:
        items = row.split('|')
        csvwriter.writerow([items.encode("utf-8") for items in items])