from flask import Flask, request, render_template
from twilio import twiml

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jordan-quote', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('received: %s' % message_body)
    return str(resp)

if __name__ == '__main__':
    app.run()