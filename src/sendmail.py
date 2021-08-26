import smtplib
from email.message import EmailMessage

def SendMail(sender, content):
    # Compose a message
    msg = EmailMessage()
    msg['Subject'] = 'Feedback'
    msg['From'] = 'Lending Co.'
    msg['To'] = 'edenroserisma13@gmail.com'
    msg.set_content(str(content + '\n From: ' + sender))


    # Establish Connection
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('edenrosefr@gmail.com', '@edenrose_0_FR')

    # Send mail
    server.send_message(msg)
    return

