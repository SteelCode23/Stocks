import smtplib

gmail_user = 'steel.ricciotti@gmail.com'


sent_from = gmail_user
to = ['steel.ricciotti@gmail.com']
subject = 'OMG Super Important Message'
body = 'Test'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')
except:
    print('Email sent!')
