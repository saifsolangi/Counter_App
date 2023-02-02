from flask import Flask, render_template, request
from numerize import numerize

# initializing app
app = Flask(__name__)

database = {'count':0}


@app.route('/')
def home():
    return render_template('index.html', number = numerize.numerize(database['count']))

@app.route('/increment')
def increment():
    if database['count']>=0:
        database['count'] +=1
    return render_template('index.html', number = numerize.numerize(database['count']))

@app.route('/decrement')
def decrement():
    if database['count']>=1:
        database['count'] -=1
    return render_template('index.html', number = numerize.numerize(database['count']))

app.run()