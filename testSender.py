import requests, json

webhookURL = 'http://b569-73-187-212-93.ngrok.io'

data = {'name': 'adam', 'dogs': ['conway', 'hank']}

r = requests.post(webhookURL, data=json.dumps(data), headers={'Content-type': 'application/json'})
print(r.text)