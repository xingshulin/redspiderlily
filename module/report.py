import collections
from datetime import date, timedelta

from jinja2 import Environment, DictLoader

from module.fileutil import read_mail_template
from module.mailfetcher import get_mail_senders_and_subjects_by_duration
from module.mailsender import send


def generate_body(pages, **kwargs):
    env = Environment()
    template_page = pages[1]
    templates = dict((name, read_mail_template(name)) for name in pages)
    env.loader = DictLoader(templates)
    mail_template = env.get_template(template_page)
    return mail_template.render(kwargs)


def is_odd_week(_from, _to):
    return timedelta(7).__eq__(_to - _from)


def is_even_week(_from, _to):
    return timedelta(14).__eq__(_to - _from)


def compose_odd_week_email(authors, topics):
    article_dict = dict(zip(topics, authors))
    article_dict = collections.OrderedDict(sorted(article_dict.items()))
    pages = ('base.html', 'odd_email.html')
    body = generate_body(pages, articles=article_dict)
    msg_content = {'to': 'wangzhe@xingshulin.com',
                   'subject': '[双周学习分享]单周总结',
                   'body': body}
    return msg_content


def compose_even_week_email(**kwargs):
    article_dict = dict(zip(kwargs.get('topics', []), kwargs.get('authors', [])))
    article_dict = collections.OrderedDict(sorted(article_dict.items()))
    pages = ('base.html', 'even_email.html')
    body = generate_body(pages, articles=article_dict, topic_count=2, unsubmitted=1)
    msg_content = {'to': 'wangzhe@xingshulin.com',
                   'subject': '[双周学习分享]双周汇总',
                   'body': body}
    return msg_content


def compose_summary_email(kwargs):
    return None


def generate(_from=date(2016, 5, 1), _to=date(2016, 5, 2)):
    senders, subjects = get_mail_senders_and_subjects_by_duration(_from, _to)

    if senders is None or subjects is None or len(senders) == 0 or len(subjects) == 0:
        return False

    if is_odd_week(_from, _to):
        msg_content = compose_odd_week_email(senders, subjects)
    elif is_even_week(_from, _to):
        peers_count = 3
        msg_content = compose_even_week_email(authors=senders, topics=subjects, peers=peers_count)
    else:
        compose_summary_email(senders, subjects)

    send(msg_content)

    return True
