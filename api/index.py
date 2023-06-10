from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/login')
def login():
    # takes user, password
    # returns {status}
    res = {
        "status": "logged success!"
        }
    return res

@app.route('/register')
def register():
    # takes user, password, retype
    # returns {status}
    res = {
        "status": "Registered success!"
        }
    return res

@app.route('/getStreak')
def getstreak():
    # takes user
    # returns {streak}
    res = {
        "strea": "streak information"
        }
    return res

@app.route('/addTop3')
def addtop3():
    # takes user, top3
    # returns {status }
    res = {
        "status": "Top3 added successfully!"
        }
    return res

@app.route('/changeTop3')
def changetop3():
    # takes user, top3
    # returns {status }
    res = {
        "status": "Top3 changed successfully!"
        }
    return res

@app.route('/getDetails')
def getdetails():
    # takes stock_id
    # returns { details }
    res = {
        "details": "details information"
        }
    return res

@app.route('/getTrending')
def gettrending():
    # takes nothing
    # returns { trending stocks }
    res = {
        "trending": "trending stock information"
        }
    return res



