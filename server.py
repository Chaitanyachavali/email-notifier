#!/usr/bin/env python3

from imapclient import IMAPClient
import time

DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = ''
PASSWORD = ''
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 0
MAIL_CHECK_FREQ = 2
NOTIFY_ON_NO_INT_CONN = False

try:
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
            if NOTIFY_ON_NO_INT_CONN:
                print(e)
            else:
                pass
except KeyboardInterrupt:
    print("Service being closed by user")