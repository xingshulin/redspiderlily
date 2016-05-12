import smtplib
from email.mime.text import MIMEText

from module import settings

smtp_host = settings.get('SMTP_HOST')
username = settings.get('EMAIL_USERNAME')
password = settings.get('EMAIL_PASSWORD')


def generate_msg(kwargs):
    # mail body with content
    body = kwargs['body']

    msg = MIMEText(body, _subtype='html', _charset='UTF-8')
    msg['to'] = kwargs['to']
    msg['from'] = username
    msg['subject'] = kwargs['subject']
    return msg


def send(kwargs):
    smtp = smtplib.SMTP()
    smtp.connect(smtp_host, 25)
    smtp.login(username, password)
    smtp.send_message(generate_msg(kwargs))
    smtp.quit()
