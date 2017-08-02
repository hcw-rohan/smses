""" NotificationService object. Handles Google SMTP, Slack Notifications and SMS via Twilio """
from __future__ import print_function
from flask_mail import Mail, Message
from slackclient import SlackClient
from twilio.rest import Client

class NotificationService(object):
    """ Handle logic for Mount Bruno here """
    flask_app = ''
    google_config = ''
    slack_config = ''
    sms_config = ''

    mail = ''
    slack_client = ''
    sms_client = ''
    slack_channels = {}

    def __init__(self):
        """ Constructor """

    def init_google(self, flask_app, google_config):
        """ Initialise the google SMTP service """
        self.flask_app = flask_app
        self.google_config = google_config

        self.flask_app.config.update(self.google_config)
        self.mail = Mail(self.flask_app)

    def init_slack(self, slack_config):
        """ Initialise the slack Notification service """
        self.slack_config = slack_config
        self.slack_client = SlackClient(self.slack_config['TOKEN'])

        channels = self.list_channels()

        if channels:
            for channel in channels:
                for allowed_channel in self.slack_config['CHANNELS']:
                    if channel['name'] == allowed_channel:
                        self.slack_channels[channel['name']] = channel['id']
        else:
            print("Error: Channel not found")


    def init_sms(self, sms_config):
        """ Initialise Twilio SMS Service """
        self.sms_config = sms_config
        self.sms_client = Client(self.sms_config['TWILIO_SID'], self.sms_config['TWILIO_TOKEN'])

    def list_channels(self):
        """ list slack channels """
        channels_call = self.slack_client.api_call("channels.list")
        if channels_call.get('ok'):
            return channels_call['channels']
        return None

    def send_slack(self, message, channel):
        """ send slack message """
        self.slack_client.api_call(
            "chat.postMessage",
            channel=self.slack_channels[channel],
            text=message,
            username=self.slack_config['USERNAME'],
            icon_emoji=self.slack_config['ICON'])

    def send_email(self, body, sender, recipients):
        """ Send an email """
        msg = Message(body, sender=sender, recipients=recipients)
        self.mail.send(msg)

    def send_sms(self, body, recipient):
        """ Send sms via twilio. Can only send to one user at a time """
        self.sms_client.messages.create(
            to=recipient,
            from_=self.sms_config['TWILIO_PHONE'],
            body=body
        )
