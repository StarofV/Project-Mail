import smtplib
import sys

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("your email here", "the pass of your email here") 
    
def mailer(email, message):
    server.sendmail("Your email here", email, message)
    server.quit()
    print("Job done, program done.")
mailer(sys.argv[1], sys.argv[2])
