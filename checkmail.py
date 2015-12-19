#!/usr/bin/env python
#Code found on Adafruit.com @ https://learn.adafruit.com/raspberry-pi-e-mail-notifier-using-leds/overview

from imapclient import IMAPClient
from PyGlow import PyGlow
import time

#Set DEBUG to False if you want nothing logged to the console.
DEBUG = True

HOSTNAME = 'imap.gmail.com'
USERNAME = 'your username here'
PASSWORD = 'your password here'
MAILBOX = 'Inbox'

NEWMAIL_OFFSET = 0   # my unread messages never goes to zero, yours might
MAIL_CHECK_FREQ = 60 # check mail every 60 seconds

#PyGlow Global Variables:
b = 128
s = 1000
pyglow = PyGlow(brightness=int(b), speed=int(s), pulse=True)


def loop():
    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)

    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])

    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])

    if DEBUG:
        print "You have", newmails, "new emails!"

    if newmails > NEWMAIL_OFFSET:
        pyglow.color(6)
    else:
        pyglow.all(0)

    time.sleep(MAIL_CHECK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()


#The PyGlow() object can accept four optional parameters:

# brightness=None - sets default brightness level (value: number from 0 and 255)
# speed=None - sets default pulsing speed in milliseconds (value: number > 0)
# pulse=None - enables pulsing by default (value: True or False)
# pulse_dir=None - sets default pulsation direction (value: UP, DOWN, BOTH)

#In order to be able to use PyGlow module, the PyGlow() class must be imported:
#from PyGlow import PyGlow

#Then it's possible to instantiate the PyGlow() object:
#pyglow = PyGlow()
