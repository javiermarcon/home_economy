# -*- coding: utf-8 -*-

import email
import imaplib

class manage_email:

    mail_obj = None

    def __init__(self, user, password, server="imap.gmail.com", port=993, use_ssl=True):
        """
        logins in the mail server tofetch mails
        :param user: email account used to login
        :param password: password of the email account
        :param server: imap server
        :param port: port used to connect
        :return:
        """
        self.user = user
        self.password = password
        if use_ssl:
            self.mail_obj = imaplib.IMAP4_SSL(server, port)
        else:
            self.mail_obj = imaplib.IMAP4(server, port)
        self.mail_obj.login(self.user, self.password)

    def __exit__(self, type, value, traceback):
        self.mail_obj.close()
        self.mail_obj.logout()

    def select_folder(self, folder='inbox'):
        """
        Selects a mail folder
        :param folder: folder to select
        :return: True or false
        """
        msgs = self.mail_obj.select(folder)
        if msgs[0] == 'OK':
            return True
        return False

    def search_messages(self, last_message=None, patterns=None):
        """
        searchs messages using a pattern or list of patterns
        all patterns are described in: https://tools.ietf.org/html/rfc3501#page-49
        :param patterns: string or list of patterns to search ex: (UNSEEN SUBJECT "zz")
        :param last_message: last message searched, to return only messages after that id
        :return: list of message ids

        Pattern examples:
        messages since yesterday:
        date = (datetime.date.today() - datetime.timedelta(1)).strftime("%d-%b-%Y")
        '(SENTSINCE {0})'.format(date)
        From someone: (FROM {0})'.format('sarasa@gmail.com'.strip())
        Unread messages: '(UNSEEN)'
        Subject containing zz: '(SUBJECT "zz")'
        """
        patterns = self.normalize_patterns(patterns)
        type, data = self.mail_obj.uid('search', None, patterns)
        id_list = [ int(x) for x in data[0].split() ]
        if last_message:
            if not isinstance(last_message, int):
                last_message = int(last_message)
            id_list = [ x for x in id_list if x > last_message ]
        return id_list

    def normalize_patterns(self, patterns):
        """
        returns patterns to search in a string
        :param patterns: patterns to search
        :return: string with patterns normalized
        """
        if isinstance(patterns, list):
            patterns = " ".join(patterns)
            if not patterns.startswith("("):
                patterns = "(" + patterns
            if not patterns.endswith(")"):
                patterns = patterns + ")"
        if not patterns:
            patterns = 'ALL'
        return patterns

    def get_mail_folders(self):
        return self.mail_obj.list()

    def get_emails(self, mail_list):
        """
        fetches the email
        :param mail_list:
        :return:
        """
        for num in mail_list :
            typ, data = self.mail_obj.uid('fetch', num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1])
                    msg_resp = { "subject": msg['subject'],
                                "from": msg['from'],
                                 "date": msg["Date"], #.strftime("%a, %d %b %Y %H:%M:%S")),
                                "body": self.get_first_text_block(msg),
                                "attachments": self.get_attachments(msg),
                                "msg": msg }


            yield msg_resp

    def get_attachments(self, msg):
        """
        Lee un attachment de un mail
        :param msg: message content
        :return: a dictionary with filenames and file contents of the attachments that the message has
        """
        atts = {}
        for part in msg.walk():
            #if part.get_content_type() == 'application/octet-stream':
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            fileName = part.get_filename()
            if bool(fileName):
                atts[fileName] = part.get_payload(decode=1)
        return atts


    def mark_read(self, num):
        """
        Marca el mensaje colo leido
        :param num: numero de mensaje
        :return: retorna "ok" si anduvo bien
        """
        typ, data = self.mail_obj.store(num, '+FLAGS', '\\Seen')
        return typ

    def get_first_text_block(self, email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            for part in email_message_instance.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return email_message_instance.get_payload()


"""
EMAIL_ACCOUNT = "your@gmail.com"
PASSWORD = "your password"

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL_ACCOUNT, PASSWORD)
mail.list()
mail.select('inbox')
result, data = mail.uid('search', None, "UNSEEN") # (ALL/UNSEEN)
i = len(data[0].split())

for x in range(i):
    latest_email_uid = data[0].split()[x]
    result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
    # result, email_data = conn.store(num,'-FLAGS','\\Seen')
    # this might work to set flag to seen, if it doesn't already
    raw_email = email_data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)

    # Header Details
    date_tuple = email.utils.parsedate_tz(email_message['Date'])
    if date_tuple:
        local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
    email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
    email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

    # Body details
    for part in email_message.walk():
        if part.get_content_type() == "text/plain":
            body = part.get_payload(decode=True)
            file_name = "email_" + str(x) + ".txt"
            output_file = open(file_name, 'w')
            output_file.write("From: %s\nTo: %s\nDate: %s\nSubject: %s\n\nBody: \n\n%s" %(email_from, email_to,local_message_date, subject, body.decode('utf-8')))
            output_file.close()
        else:
            continue
"""