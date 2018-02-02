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


# One time initialization of libnotify
Notify.init("Email Notifier")

# Create the notification object
summary = "New email"
body = "you have new emails"
image = "/home/chaitanya/Documents/Github/email-notifier/favicon.ico"
notification = Notify.Notification.new(summary,
    body, image
)
# image = GdkPixbuf.Pixbuf.new_from_file("/home/chaitanya/Documents/Github/email-notifier/favicon.ico")
# notification.set_icon_from_pixbuf(image)
# notification.set_image_from_pixbuf(image)
# Actually show on screen
notification.show()