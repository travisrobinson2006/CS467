import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import contact_info

#Travis Robinson
#Centaurus
#CS467
#Oregon State University

#function used for sending emails; will ensure we're alerted if there's some type of error
def send_message_helper(sender,recipient,message_subject,message_text):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['subject'] = message_subject

    body = message_text
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, contact_info.SECRET_CODE)
    text = msg.as_string()
    server.sendmail(sender, recipient, text)
    server.quit()

def send_error_message(message):
    for recipient_email in contact_info.RECEIVING_EMAILS:
        send_message_helper(contact_info.SENDING_EMAIL,recipient_email,"ERROR IN CS467: MAY REQUIRE ATTENTION",message)