# -*- coding: utf-8 -*-
import os
import sys

__all__ = ['settings']

__title__ = 'redspiderlily'
__version__ = '0.1'
__description__ = 'imap client'
__url__ = 'http://www.xingshulin.com'
__author__ = 'Jack Wang'
__licence__ = 'Apache 2.0'
__copyright__ = 'Copyright 2015'


class ConfigurationException(Exception):
    pass


CFG_PATH = os.path.join(
    os.path.dirname(__file__), 'config.ini'
)

settings = dict()

wsdl_url = username = password = None

if os.path.exists(CFG_PATH):
    from configparser import ConfigParser
    parser = ConfigParser()
    parser.read(CFG_PATH, encoding='utf-8')

    email_username = parser.get('EMAIL', 'username')
    email_password = parser.get('EMAIL', 'password')
    email_host = parser.get('EMAIL', 'host')
    email_smtp_host = parser.get('EMAIL', 'smtp_host')
    email_ssl = parser.get('EMAIL', 'ssl')

    database_host = parser.get('DATABASE', 'host')
    database_port = parser.get('DATABASE', 'port')
    database_database = parser.get('DATABASE', 'database')
    database_username = parser.get('DATABASE', 'username')
    database_password = parser.get('DATABASE', 'password')

    folder_study = parser.get('FOLDER', 'study')

    sql_names = parser.get('SQL', 'names')
else:
    raise ConfigurationException(
        "Config error "
    )

if not (database_host and database_username and database_password and email_host and email_username and email_password):
    raise ConfigurationException(
        "Please make sure you have configured the host, username, and "
        "password either in your Django settings or in a config.ini file."
    )

settings['DATABASE_HOST'] = database_host
settings['DATABASE_PORT'] = database_port
settings['DATABASE_USERNAME'] = database_username
settings['DATABASE_PASSWORD'] = database_password
settings['DATABASE_DATABASE'] = database_database
settings['FOLDER_STUDY'] = folder_study
settings['SQL_NAME'] = sql_names

settings['EMAIL_USERNAME'] = email_username
settings['EMAIL_PASSWORD'] = email_password
settings['EMAIL_HOST'] = email_host
settings['SMTP_HOST'] = email_smtp_host
settings['EMAIL_SSL'] = email_ssl

