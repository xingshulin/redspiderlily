# -*- coding: utf-8 -*-

import MySQLdb

from module import settings


# Open database connection
host = settings.get('DATABASE_HOST')
port = settings.get('DATABASE_PORT')
database = settings.get('DATABASE_DATABASE')
username = settings.get('DATABASE_USERNAME')
password = settings.get('DATABASE_PASSWORD')
namesql = settings.get('SQL_NAME')


def open_db():
    global db, cursor

    db = MySQLdb.connect(host=host, port=int(port), user=username, passwd=password, db=database)
    cursor = db.cursor()


def retrieve_data_from_db(sql):
    open_db()

    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()

    close_db()
    return results


def close_db():
    db.close()


def get_names():
    try:
        names = []
        names_from_db = retrieve_data_from_db(namesql)
        for name in names_from_db:
            names.append(name[0].strip(','))
    except Exception, e:
        print e
        print "Error: unable to fecth data"
    return names