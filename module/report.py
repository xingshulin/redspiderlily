from datetime import date, timedelta

from module.mailfetcher import get_mail_senders_and_subjects_by_duration
from module.mailsender import send


def is_odd_week(_from, _to):
    return timedelta(7).__eq__(_to - _from)


def is_even_week(_from, _to):
    return timedelta(14).__eq__(_to - _from)


def compose_odd_email(authors, topics):
    article_dict = dict(zip(topics, authors))
    msg_content = {'to': 'wangzhe@xingshulin.com',
                   'subject': '[双周学习分享]单周总结',
                   'article_dict': article_dict,
                   'compliance_dict': None,
                   'noncompliance_dict': None}
    return msg_content


def generate(_from=date(2016, 5, 1), _to=date(2016, 5, 2)):
    senders, subjects = get_mail_senders_and_subjects_by_duration(_from, _to)

    if senders is None or subjects is None or len(senders)==0 or len(subjects)==0:
        return False

    if is_odd_week(_from, _to):
        msg_content = compose_odd_email(senders, subjects)
        send(msg_content)
    return True
