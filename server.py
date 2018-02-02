#!/usr/bin/env python3

from imapclient import IMAPClient
import time

DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = 'chavalichaithanyachinna@gmail.com'
PASSWORD = 'chavali@chinna'
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 0   # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 2 # check mail every 60 seconds

while True:
    try:
        server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
        server.login(USERNAME, PASSWORD)

        if DEBUG:
            print('Logging in as ' + USERNAME)
            select_info = server.select_folder(MAILBOX)
            print('%d messages in INBOX' % select_info[b'EXISTS'])

        folder_status = server.folder_status(MAILBOX, 'UNSEEN')
        newmails = int(folder_status[b'UNSEEN'])

        if DEBUG:
            print("You have %d new emails" % newmails)
        time.sleep(MAIL_CHECK_FREQ)
    except Exception as e:
        print(e)