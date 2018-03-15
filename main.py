import smtplib
import json
import sys

with open('creds.json', 'r') as f:
    config = json.load(f)
	
user_email = config['login']['email']
user_password = config['login']['password']

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(user_email, user_password) 


def mailer(email, message):
	server.sendmail(user_email, email, message[1:-1])
	server.quit()
	print("Job has successfully finished.")
user_message = str(input("Input what to send for specified email(use quoutation marks): "))
mailer(sys.argv[1], user_message)
