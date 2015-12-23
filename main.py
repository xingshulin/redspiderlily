from module.mailfetcher import get_mail_titles
from module.namefetcher import get_names

__author__ = 'Jack'


def filter_colleagues_who_is_not_in_senders(sender_list, colleague_list):
    not_send_list = []
    for colleague in colleague_list:
        not_send_list.append(colleague)
        for sender in sender_list:
            if colleague in sender:
                not_send_list.remove(colleague)
                break
    print not_send_list
    return not_send_list


if __name__ == "__main__":
    senders = get_mail_titles()
    colleagues = get_names()

    not_send_list = filter_colleagues_who_is_not_in_senders(senders, colleagues)
    print "%i out of %i colleagues do not send yet" % (len(not_send_list), len(colleagues))