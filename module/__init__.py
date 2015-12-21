import os

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
    from ConfigParser import SafeConfigParser

    parser = SafeConfigParser()
    parser.read(CFG_PATH)

    username = parser.get('ACCOUNT', 'username')
    password = parser.get('ACCOUNT', 'password')
    host = parser.get('ACCOUNT', 'host')
    ssl = parser.get('ACCOUNT', 'ssl')
else:
    raise ConfigurationException(
        "Config error "
    )

if not (host and username and password):
    raise ConfigurationException(
        "Please make sure you have configured the host, username, and "
        "password either in your Django settings or in a config.ini file."
    )

settings['USERNAME'] = username
settings['PASSWORD'] = password
settings['HOST'] = host
settings['SSL'] = ssl