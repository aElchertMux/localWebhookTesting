# Need an environment to test webhooks locally?

It comes up sometimes where we want to not only *receieve* webhooks, but also programatically play with them.  

![Running ./run.sh](https://dl.dropbox.com/s/5r5wps4fbddktma/mux-localWebhookTesting.gif)

Here are a small set of scripts that:
* Connects ngrok to provide a public tunnel
* Starts a local Flask server to receive the webhooks
* Automatically opens the local ngrok GUI

## Requirements
* Python3 w/ Flask and requests installed
* [ngrok](https://ngrok.com) w/ auth key
