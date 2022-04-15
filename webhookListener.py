from flask import Flask, request, abort
import pprint

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        pprint.pprint(request.data)
        return 'success', 200
    else:
        abort(400)
        
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5005)