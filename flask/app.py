from flask_cors import CORS
from flask import request, Flask, make_response
from sel.sel import driver
from sel.soup import simmer
from takeout.takeout import box

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    driver.get('https://www.google.com/')
    return driver.current_url

@app.route('/incoming', methods=['POST'])
def incoming(): 
    data = request.get_json()
    driver.get(data['url'])
    data['html'] = driver.page_source
    return data

@app.route('/processing', methods=['POST'])
def processing():
    data = request.get_json()
    print(data['flavor'])
    return simmer(data, driver)

@app.route('/takeout', methods=['POST'])
def takeout():
    data = request.get_json()
    box(data)
    return data