import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
from time import sleep

df = pd.read_csv('relative file path to csv with columns of [title][company][emails]')

sender_email = ''
sender_password = ''

for row in df.itertuples():
    recipient_email = row.emails
    
    #overwrite here to manually set email (eg. recipient_email = abc@gmail.com)
    
    company = row.company
    job_title = row.title.capitalize()
    
    print(row.emails + ' ' + company + ' ' + job_title)

    subject = "Application for {} position at {}".format(job_title,company)
    body = """
    """.format(job_title, company)
    
    with open("resume path", "rb") as attachment:
        # Add the attachment to the message
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {os.path.basename('resume file name')}")

    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email
    html_part = MIMEText(body)
    message.attach(html_part)
    message.attach(part)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)
    try:
        server.sendmail(sender_email, recipient_email, message.as_string())
    except:
        print("Error on this one")
        pass
        
    sleep(2)
server.quit()
