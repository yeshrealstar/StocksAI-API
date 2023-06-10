from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

# libraries for bse
import bsedata
from bsedata import bse

@app.route('/')
@cross_origin()
def home():
    return 'Hello, World!'

@app.route('/about')
@cross_origin()
def about():
    return 'About'

@app.route('/login',methods=['GET','POST'])
@cross_origin()
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

@app.route('/getTop3')
def gettop3():
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
    b = bse.BSE(update_codes = True)
    tg = b.topGainers()
    trending = [[o['securityID'], b.verifyScripCode(o['scripCode'])] for o in tg[:3]]
    res = {
        "trending": trending
        }
    return res


