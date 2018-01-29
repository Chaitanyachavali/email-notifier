# import pynotify
# pynotify.init("Test")
# notice = pynotify.Notification(title, message)
# notice.show()
import subprocess
subprocess.Popen(['notify-send', 'Title', 'Message'])