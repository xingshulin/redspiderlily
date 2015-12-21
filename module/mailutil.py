import email

__author__ = 'Jack'


def to_unicode(s, encoding):
    if encoding:
        return unicode(s, encoding)
    else:
        return unicode(s)


def parse_address(msg_addr):
    msg_addr = msg_addr.strip(' ')
    msg_pair = msg_addr.split(' ')
    if len(msg_pair) == 2:
        mail_name = email.Header.decode_header((msg_pair[0]).strip('\"'))[0]
        mail_address = msg_pair[1]
        full_address = to_unicode(mail_name[0], mail_name[1]) + mail_address
    else:
        full_address = msg_addr
    return full_address


def get_sender(msg_from):
    sender = parse_address(msg_from)
    return sender


def get_receivers(msg_to):
    msg_to = msg_to.replace('\n', '')
    msg_receiver_list = msg_to.split(',')
    receivers = []
    for msg_receiver in msg_receiver_list:
        receivers.append(parse_address(msg_receiver))
    return receivers


def get_subject(msg_subject):
    subject = email.Header.decode_header(msg_subject)
    return to_unicode(subject[0][0], subject[0][1])
