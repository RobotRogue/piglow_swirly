import sys, feedparser, winsound
#More info here: http://null-byte.wonderhowto.com/how-to/make-gmail-notifier-python-0132845/

newEmail=""
USERNAME="YOUR.GMAIL.ADDRESS@gmail.com"
PASSWORD="YOUR PASSWORD"
PROTO="https://"
SERVER="mail.google.com"
PATH="/gmail/feed/atom"

#We assign variables with values. Fill in your username and password
def mail(checker):
    email = int(feedparser.parse(
        PROTO + USERNAME + ":" + PASSWORD + "@" + SERVER + PATH
    )["feed"]["fullcount"])

#parses your account data and sends it to gmail
    #checks for mail
    if email > 0:
        newEmail = 1
    else:
        newEmail = 0


    #plays sound if email present
    if newEmail==1:
         winsound.Beep(440, 500)
         winsound.Beep(370, 500)
         winsound.Beep(392, 500)


#need to replace winsound.Beep with piglow functionality
#set the piglow functionality to pulse red when email is present (newEmail==1)
#consider also adding other glow colors for other states, extend functionality to more than email checker
