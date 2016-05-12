from module import report
from module.mailfetcher import get_mail_senders_and_subjects_by_duration

__author__ = 'Jack'


def check_the_colleague_name_in_sender_list(colleague, sender_list):
    colleague_names = colleague.split(',')
    for colleaguename in colleague_names:
        for sender in sender_list:
            if colleaguename in sender:
                not_send_list.remove(colleague)
                return


def filter_colleagues_who_is_not_in_senders(sender_list, colleague_list):
    for colleague in colleague_list:
        not_send_list.append(colleague)
        check_the_colleague_name_in_sender_list(colleague, sender_list)

    print(not_send_list)
    return not_send_list


if __name__ == "__main__":
    global not_send_list
    report.generate()
    # not_send_list = []
    # senders = get_mail_senders_and_subjects_by_duration()
    # colleagues = get_names()

    # not_send_list = filter_colleagues_who_is_not_in_senders(senders, colleagues)
    # print "%i out of %i colleagues do not send yet" % (len(not_send_list), len(colleagues))

    # print(senders)
