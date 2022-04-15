import requests, json

webhookURL = ''

data = {'name': 'adam', 'dogs': ['conway', 'hank']}

r = requests.post(webhookURL, data=json.dumps(data), headers={'Content-type': 'application/json'})
print(r.text)