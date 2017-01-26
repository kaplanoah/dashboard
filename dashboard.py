from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv, find_dotenv
from twilio import twiml

app = Flask(__name__)

load_dotenv(find_dotenv())

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

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

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=True)

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '<Quote %r>' % self.text

if __name__ == '__main__':
    app.run()
