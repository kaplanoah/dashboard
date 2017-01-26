from flask import Flask, request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv, find_dotenv
from twilio import twiml

app = Flask(__name__)

load_dotenv(find_dotenv())

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), unique=True)
    created =  db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return '<Quote %s %s %s %r>' % (self.id, self.created, self.modified, self.text)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/jordan-quote', methods=['POST'])
def sms():
    number = request.form['From']
    quote_text = request.form['Body']

    db.session.add(Quote(quote_text))
    db.session.commit()

    # quote too long
    # quote not unique

    # resp = twiml.Response()
    # resp.message('received: %s' % message_body)

@app.route('/latest-quote', methods=['GET'])
def latest_quote():
    quote = Quote.query.order_by(Quote.created.desc()).first()

    if not quote:
        return jsonify(latest_quote=None)

    return jsonify(latest_quote=quote.text)

if __name__ == '__main__':
    app.run()
