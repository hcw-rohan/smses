# SMSES Notification system

Send out a message via SMS, Email and Slack. It began as a way to send messages out quickly in an area with no mobile reception but satellite internet.

## Getting Started

You should know a little bit of python and be happy playing around on a web server. Knowing a bit of bash would be helpful too.

### Prerequisites

- Python
- Flask
- A Slack account
- A Gmail account (or other mail server)
- A Twilio account http://twilio.com/ with an approved mobile number that can accept SMS
- A web server eg. https://www.digitalocean.com/


### Installing

First thing you'll need to do, is install Flask. Open up your CLI and enter

```
pip install Flask
```

In a shared environment, you should probably install this inside virtualenv. More info here http://flask.pocoo.org/docs/0.12/installation/

You'll also want to install the Twilio helper library

```
pip install twilio
```

The sample.py gives you a base demo on how to send messages to each target.

You should open up the config.py and enter your info. Yes this should be moved to environment variables or some other storage, but you smart people can figure that out :)

## Running

Simply run the script

```
python sample.py
```

On a production server, you'll probably want to create a cron that runs the script on boot. To do this:

```
crontab -e
```

Then

```
@reboot /smses_path/sample.py
```

Make sure your sample starts with the following line

```
#!/usr/bin/env python
```

With the service running, you can now SMS your Twilio number either from a phone or Twilio's web console and it will relay the message to the numbers, email addresses and slack channel listed in the config.

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Flask](http://flask.pocoo.org/)
* [Twilio](https://www.twilio.com/)
* [Slack](https://slack.com/)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Rohan Latimer** - *Initial work* - [HighCountryWeb](https://highcountryweb.com.au)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* None right now 