from twilio.rest import Client
import os

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_TOKEN")
client = Client(account_sid, auth_token)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def send_message(self, body):
        message = client.messages.create(
            messaging_service_sid='MG54120b03f06cf5eb081beceab90432c3',
            body=body,
            to='+919739983563'
        )
        return message.status
