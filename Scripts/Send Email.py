import smtplib

def send_email(user, pwd, recipient, subject, body):


    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")


FROM='ashokapostman@gmail.com'
TO=email_sender
message=emai_
subject="LALALLA"

server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server_ssl.ehlo() # optional, called by login()
server_ssl.login('ashokapostman@gmail.com','DIBYENDU1997')  
# ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
server_ssl.sendmail(FROM, TO, message)
#server_ssl.quit()
server_ssl.close()
print('successfully sent the mail')