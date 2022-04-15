# Need an environment to test webhooks locally?

It comes up sometimes where we want to not only *receieve* webhooks, but also programatically play with them.  

![Running ./run.sh](https://dl.dropboxusercontent.com/s/sjrl59pp84aqsqm/mux-localWebhookTesting.gif)

Here are a small set of scripts that:
* Connects ngrok to provide a public tunnel
* Starts a local Flask server to receive the webhooks
* Automatically opens the local ngrok GUI

## Requirements
* Python3 w/ Flask and requests installed
* [ngrok](https://ngrok.com) w/ auth key

# How to use
* Run the `run.sh` file 

## webhookListener.py

This has a simple route at base URL which accepts GET and POST requests. Flask uses the class "request" for the response it receives as the webhook receiver. You can find all the available methods [here](https://tedboy.github.io/flask/generated/generated/flask.Request.html) to play with. 

## testSender.py

Want to send a quick test webhook? Just fill in the webhook URL from the NGROK window. 