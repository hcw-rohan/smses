''' Config. Prob should use Environment variables instead :) '''
GOOGLE_CONFIG = dict(
    DEBUG=True,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USE_SSL=False,
    MAIL_USERNAME='',
    MAIL_PASSWORD=''
)

SLACK_CONFIG = dict(
    TOKEN='',
    CHANNEL='',
    USERNAME='',
    ICON=''
)

SMS_CONFIG = dict(
    TWILIO_SID='',
    TWILIO_TOKEN='',
    TWILIO_PHONE=''
)

# Recepients
EMAILS = ["noreply@someemail.com"]
MOBILES = ["+xxxxxxxxxxx"]
FROM = "noreply@someemail.com"

# Global Config
VALID_NUMBERS = {
    "+xxxxxxxxxx1": "Name",
    "+xxxxxxxxxx2": "Name"
}

#Web host IP Address
HOST_IP = ''
