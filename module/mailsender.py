import collections
import smtplib
from email.mime.text import MIMEText

from jinja2 import Template

from module import settings
from module.fileutil import read_mail_template

smtp_host = settings.get('SMTP_HOST')
username = settings.get('EMAIL_USERNAME')
password = settings.get('EMAIL_PASSWORD')


def generate_body(kwargs):
    mail_template = Template(read_mail_template('/odd_email.html'))

    articles = kwargs['article_dict']
    articles = collections.OrderedDict(sorted(articles.items()))
    content_dict = {"articles": articles}
    return mail_template.render(content_dict)


def generate_msg(kwargs):
    # mail body with content
    body = generate_body(kwargs)

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
