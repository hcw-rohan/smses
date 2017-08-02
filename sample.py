#!/usr/bin/env python
""" Get an SMS, spam the slack channel and emails accounts """

from __future__ import print_function
import config
from lib import NotificationService
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

#Setup flask
APP = Flask(__name__)

#Listen for SMS from Twilio
@APP.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """ An SMS was sent so do some stuff """

    #grab the number and message
    from_number = request.values.get('From', None)
    from_message = request.values.get('Body', None)

    #create response object for twilio
    response = MessagingResponse()

    #make sure the number is valid and message is valid
    if from_number in config.VALID_NUMBERS:

        #find a code word in the message
        if from_message.find("MYCODE") != -1:
            message(from_message)
        else:
            print('Error: Invalid SMS Code')
            response.message('Error: Invalid SMS Code')
            return str(response)
    else:
        print('Error: Invalid Phone Number')
        response.message('Error: Invalid Phone Number')
        return str(response)

    response.message('Message sent successfully')
    return str(response)

def message(from_message):
    """ send message out to all the targets """
    # Init Email
    message_service = NotificationService()
    message_service.init_google(APP, config.GOOGLE_CONFIG)

    #Init Slack
    message_service.init_slack(config.SLACK_CONFIG)

    #Init SMS
    message_service.init_sms(config.SMS_CONFIG)

    #Strip the code from the SMS
    body = from_message[7:]

    #Send Slack Notification (message, channel)
    message_service.send_slack(body, "general")

    #Send Email
    with APP.app_context():
        message_service.send_email(body, config.FROM, config.EMAILS)

    #Send SMS
    #You must loop through all the numbers and do a seperate twilio request for each
    for number in config.MOBILES:
        message_service.send_sms(body, number)

    return 'OK'

# Remove debug param in production
if __name__ == "__main__":
    APP.run(debug=True, host=config.HOST_IP)
