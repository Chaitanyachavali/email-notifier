#!/usr/bin/env python3

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf
from imapclient import IMAPClient
import time
import subprocess

DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = ''
PASSWORD = ''
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 0
MAIL_CHECK_FREQ = 2
NOTIFY_ON_NO_INT_CONN = True
NOTIFY_IMAGE = '/home/chaitanya/Documents/Github/email-notifier/favicon.ico'


def notifyUser(emailCount):
    global NOTIFY_IMAGE
    Notify.init("Email Notifier")
    emailNotification = Notify.Notification.new("INIT", "INIT", NOTIFY_IMAGE)
    # emailNotification.show()
    if DEBUG:
        print("Notifying")
    checkTag = 'mail' if emailCount == 1 else 'mails'
    headTag = "Hey there! New " + checkTag + " for you"
    bodyTag = "You have " + str(emailCount) + " new " + checkTag + " in your mailbox @chavalichaithanyachinna"
    emailNotification.update(headTag, bodyTag, NOTIFY_IMAGE)
    emailNotification.show()
    time.sleep(5)
    Notify.uninit()

def startService():
    try:
        while True:
            try:
                gServer = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
                gServer.login(USERNAME, PASSWORD)

                if DEBUG:
                    print('Logged in as ' + USERNAME)
                    select_info = gServer.select_folder(MAILBOX)
                    print('%d messages in INBOX' % select_info[b'EXISTS'])

                folder_status = gServer.folder_status(MAILBOX, 'UNSEEN')
                newmails = int(folder_status[b'UNSEEN'])

                if DEBUG:
                    print("You have %d new emails" % newmails)

                if newmails > 0:
                    notifyUser(newmails)

                time.sleep(MAIL_CHECK_FREQ)
            except Exception as e:
                if NOTIFY_ON_NO_INT_CONN:
                    print(e)
                else:
                    pass
    except KeyboardInterrupt:
        print("Service being closed by user")

# http://ibiblio.org/g2swap/byteofpython/read/module-name.html
if __name__ == '__main__':
    startService()