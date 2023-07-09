from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Returns 'welcome'"""
    return 'welcome'



@app.route('/welcome/back')
def welcome_back():
    """"Returns 'welcome back'"""
    return 'welcome back'


@app.route('/welcome/home')
def welcome_home():
    """"Returns 'welcome home, Scott'"""
    return 'welcome home, Scott'