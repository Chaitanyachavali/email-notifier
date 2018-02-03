#!/usr/bin/env python3

# import pynotify
# pynotify.init("Test")
# notice = pynotify.Notification(title, message)
# notice.show()
# import subprocess
# subprocess.Popen(['notify-send', 'Title', 'Message'])

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf
import time
Notify.init("Email Notifier")
summary = "New email"
body = "you have new emails"
image = "/home/chaitanya/Documents/Github/email-notifier/favicon.ico"
emailNotification = Notify.Notification.new(summary,
    body, image
)
# emailNotification.show()
# time.sleep(5)
i=0
while True:
	i=i+1
	emailNotification.update(str(i), "new", image)
	emailNotification.show()
	time.sleep(5)