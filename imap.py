#!/usr/bin/env python

# Author: Josef Florian Sedlmeier
# 2013/06/04
# Beschreibung: Einfaches Skript zum verbinden an einen IMAP-Server.
# Auslesen der letzen fuenf Nachrichten (Betreff, Absender), der Anzahl
# aller Nachrichten im Ordner und der Anzahl aller ungelesenen Nachrichten.

import imaplib
import email

# Zugangsdaten Gmail-Server
username = '' # you Gmail Username
password = '' # your pw
mailbox = 'INBOX' # inbox is default
mailserver = 'imap.gmail.com'
port = 993

# Verbidung zum mailserver herstellen
mail = imaplib.IMAP4_SSL(mailserver,port)

# Gmail benoetigt ssl. Fuer Zugriff auf einen Server ohne SSL die folgende
# Methode benutzen:
# mail = imaplib.IMAP4(mailserver,port)

# login mit den oben eingetragenen Zugangsdaten
mail.login(username,password)

# Ordner asuwaehlen
mail.select(mailbox)

# infos abholen
data = str(mail.status(mailbox, '(MESSAGES UNSEEN)'))
tokens = data.split()

# Die 5 letzten mails ausgeben
print
print tokens[2].replace('(',''),tokens[3] 
print tokens[4],tokens[5].replace(')\'])','')
print
# print 'Last Mails'

######################################################################################################################
# Der Folgende Codeblock ist von StackOverflow 
# http://stackoverflow.com/questions/7314942/python-imaplib-to-get-gmail-inbox-subjects-titles-and-sender-name
# und wurde leicht angepasst um den Beduerfnissen gerecht zu werden

#typ, data = mail.search(None, 'ALL')
#ids = data[0]
#id_list = ids.split()
#get the most recent email id
#latest_email_id = int( id_list[-1] )

#....^other code is the same as above except need to import email module
#mail.select('inbox')
#typ, data = mail.search(None, 'ALL')
#ids = data[0]
#id_list = ids.split()
#get the most recent email id
#latest_email_id = int( id_list[-1] )
#
#iterate through 15 messages in decending order starting with latest_email_id
#the '-1' dictates reverse looping order
#for i in range( latest_email_id, latest_email_id-5, -1 ):
#    typ, data = mail.fetch( i, '(RFC822)' )
#
#    for response_part in data:
#       if isinstance(response_part, tuple):
#           msg = email.message_from_string(response_part[1])
#           varSubject = msg['subject']
#           varFrom = msg['from']
#
#    #remove the brackets around the sender email address
#    varFrom = varFrom.replace('<', '')
#    varFrom = varFrom.replace('>', '')
#
#    #add ellipsis (...) if subject length is greater than 35 characters
#    if len( varSubject ) > 35:
#       varSubject = varSubject[0:32] + '...'
#
#    print '[' + varFrom.split()[-1] + '] ' + varSubject

######################################################################################################################

# mailbox schliessen
mail.close()

# abmelden vom server
mail.logout()

