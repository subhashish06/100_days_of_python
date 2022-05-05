"""
Program: Flight Club Notification Manager
Author: Subhashish Dhar
Date: 05/09/2021
"""

import os
from smtplib import SMTP
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
password = os.environ.get("GMAIL_PASSWORD")


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    @staticmethod
    def send_message(body):
        """sends the SMS"""
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid="MG54120b03f06cf5eb081beceab90432c3",
            body=body,
            to="+919739983563",
        )
        return message.status

    @staticmethod
    def send_email(email, body):
        """sends the email"""
        with SMTP("smtp.gmail.com") as mail:
            mail.starttls()
            mail.login(user="subbu.pybot@gmail.com", password=password)
            mail.sendmail(from_addr="subbu.pybot@gmail.com", to_addrs=[email], msg=body)
