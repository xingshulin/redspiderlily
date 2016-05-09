# -*- coding: utf-8 -*-

import pymysql.cursors
from module import settings


# Open database connection
host = settings.get('DATABASE_HOST')
port = settings.get('DATABASE_PORT')
database = settings.get('DATABASE_DATABASE')
username = settings.get('DATABASE_USERNAME')
password = settings.get('DATABASE_PASSWORD')
namesql = settings.get('SQL_NAME')
db = None


def open_db():
    db = pymysql.connect(host=host, port=int(port), user=username, passwd=password, db=database)
    return db.cursor()


def retrieve_data_from_db(sql):
    cursor = open_db()

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
    except Exception as e:
        print(e)
        print("Error: unable to fecth data")
    return names
