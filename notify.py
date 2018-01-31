# import pynotify
# pynotify.init("Test")
# notice = pynotify.Notification(title, message)
# notice.show()
# import subprocess
# subprocess.Popen(['notify-send', 'Title', 'Message'])
from gi.repository import Notify

# One time initialization of libnotify
Notify.init("My Program Name")

# Create the notification object
summary = "Wake up!"
body = "Meeting at 3PM!"
notification = Notify.Notification.new(
    summary,
    body, # Optional
)

# Actually show on screen
notification.show()