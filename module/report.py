from collections import Counter
from datetime import date, timedelta

from jinja2 import Environment, DictLoader

from module.fileutil import read_mail_template
from module.mailfetcher import get_mail_senders_and_subjects_by_duration
from module.mailsender import send
from module.namefetcher import get_names


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


def compose_odd_week_email(**kwargs):
    article_dict = dict(zip(kwargs.get('topics', []), kwargs.get('authors', [])))
    article_dict = collections.OrderedDict(sorted(article_dict.items()))
    pages = ('base.html', 'odd_email.html')
    body = generate_body(pages, articles=article_dict)
    msg_content = {'to': kwargs.get('mail_group', "wangzhe@xingshulin.com"),
                   'subject': '[单周结束总结]',
                   'body': body}
    return msg_content


def total_peers():
    return len(get_names())


def compose_even_week_email(**kwargs):
    article_dict = dict(zip(kwargs.get('topics', []), kwargs.get('authors', [])))
    article_dict = collections.OrderedDict(sorted(article_dict.items()))
    pages = ('base.html', 'even_email.html')
    article_count = len(article_dict)
    peers_count = total_peers()
    body = generate_body(pages, articles=article_dict, topic_count=article_count,
                         unsubmitted=(peers_count - article_count))
    msg_content = {'to': kwargs.get('mail_group', "wangzhe@xingshulin.com"),
                   'subject': '[双周结束汇总]',
                   'body': body}
    return msg_content


def compose_summary_email(**kwargs):
    author_counts = Counter(kwargs.get('authors', []))
    for key, value in author_counts.items():
        print(str(key) + " | " + str(value))
    return None


def generate(_from=date(2016, 5, 9), _to=date(2016, 5, 16), mail_group="wangzhe@xingshulin.com"):
    senders, subjects = get_mail_senders_and_subjects_by_duration(_from, _to)

    if senders is None or subjects is None or len(senders) == 0 or len(subjects) == 0:
        return False

    if is_odd_week(_from, _to):
        msg_content = compose_odd_week_email(authors=senders, topics=subjects,
                                             mail_group=mail_group)
    elif is_even_week(_from, _to):
        peers_count = 3
        msg_content = compose_even_week_email(authors=senders, topics=subjects, peers=peers_count,
                                              mail_group=mail_group)
    else:
        compose_summary_email(authors=senders, topics=subjects, mail_group=mail_group)

    send(msg_content)

    return True
