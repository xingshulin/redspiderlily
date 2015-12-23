# -*- coding: utf-8 -*-

import MySQLdb

from module import settings


# Open database connection
host = settings.get('DATABASE_HOST')
port = settings.get('DATABASE_PORT')
database = settings.get('DATABASE_DATABASE')
username = settings.get('DATABASE_USERNAME')
password = settings.get('DATABASE_PASSWORD')


def open_db():
    global db, cursor

    db = MySQLdb.connect(host=host, port=int(port), user=username, passwd=password, db=database)
    cursor = db.cursor()


def retrieve_data_from_db(sql):
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    return results


def close_db():
    db.close()