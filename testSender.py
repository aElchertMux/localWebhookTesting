import requests, json, os

# the ngrok server must be running to catch the webhookURL
rawData = requests.get("http://127.0.0.1:4040/api/tunnels")
r_unicode = rawData.content.decode("utf-8")
r_json = json.loads(r_unicode)
webhookURL = r_json['tunnels'][0]['public_url']

# sample webhook body
data = {'name': 'adam', 'dogs': ['conway', 'hank']}

r = requests.post(webhookURL, data=json.dumps(data), headers={'Content-type': 'application/json'})
print(r.text)