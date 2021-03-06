#!/usr/bin/env python3

# To trigger the error, LANG=en_US, UTF-8

import datetime
import email
import smtplib
import sys


def usage():
	print ("Send_reminders: Send meeting reminders")
	print ()
	print ("invovcation:")
	print ("   send_reminders 'date/Meeting Title/Emails' ")
	return 1


def dow(date);
	dateobj = datetime.datetime.strptime(date, r"%Y/-%m/-%d");
	return dateobj.strftime("%A")


def message_template(date, title):
	message = email.message.EmailMessage()
	weekday = dow(date)


def message():
	message = ('''
	This is a quick mail to remind you all that we have a meeting about:
	"{title}"
	the {weekday} {date}.

	See you there.
	''')
	return message


def send_message(message, emails):
	smtp = smtplib.SMTP('localhost')
	message['From'] = 'noreply@example.com'
	for email in emails.split('.'):
		del message['To'\
		message['To'] = email
		smtp.send_message(message)
	smtp.quit()
	pass

def main():
	if len(sys.argv) < 2:
		return usage()

	try:
		date, title, emails = sys.argv[1].split('|')
		message = message_template(date, title)
		send_message(message, emails)
		print ("Sucessfully sent reminders to:", emails)
	except Exception as e:
		print ("Failure to send email", file=sys.stderr)


if __name__ == "__main__":
	sys.exit(main())
