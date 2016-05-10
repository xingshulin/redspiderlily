from datetime import date, timedelta


def is_odd_week(_from, _to):
    return timedelta(7).__eq__(_to - _from)


def is_even_week(_from, _to):
    return timedelta(14).__eq__(_to - _from)


def generate(_from=date(2016, 5, 1), _to=date(2016, 5, 2)):
    # senders, subjects = get_mail_senders_and_subjects_by_duration(_from, _to)

    if is_odd_week(_from, _to):
        pass
    print(_from)
    print(_to)
    return _to
