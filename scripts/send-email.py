#!/usr/bin/env python

import smtplib
from os import getenv
import time

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_HOST = getenv('SMTP_HOST')
SMTP_USER = getenv('SMTP_USER')
SMTP_PASSWORD = getenv('SMTP_PASSWORD')
SMTP_PORT = 587
FROM_ADDRESS =  getenv('FROM_ADDRESS')
ENV_NAME = getenv('ENV_NAME')

msg = MIMEMultipart('alternative')
msg['Subject'] = "[{}] Cron Job Failed - Refresh ECR Creds".format(ENV_NAME)
msg['From'] = FROM_ADDRESS
msg['To'] = getenv('TO_ADDRESSES')
TO_ADDRESSES = [address.strip() for address in getenv('TO_ADDRESSES').split(',')]

now = time.ctime()
html = "Refresh ECR creds cron job failed on {}. Check it out!".format(now)

mime_text = MIMEText(html, 'html')
msg.attach(mime_text)

try:
    print('Sending email...')
    s = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
    s.starttls()
    s.login(SMTP_USER, SMTP_PASSWORD)
    s.sendmail(FROM_ADDRESS, TO_ADDRESSES, msg.as_string())
    s.quit()
    print('Email sent!')
except Exception as e:
    print('Unable to sent email: {}'.format(e))
    raise e
