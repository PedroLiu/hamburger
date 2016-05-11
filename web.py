#!/usr/bin/python3
#coding=utf-8
from flask import Flask, request, session, render_template, redirect, abort, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from myData import *
from myClass import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)

# favicon
@app.route('/favicon.ico')
def favicon():
    return redirect('/static/favicon.ico')

# get menu data
@app.route('/api/getorder/', methods=['GET'])
def get_menu():
    data = myData().getMenu()
    return jsonify(data)

# post a new order
@app.route('/api/neworder/', methods=['POST'])
def new_order():
    print(request.json);
    return orderView().submitOrder();

# change state
@app.route('/api/shift/', methods=['POST'])
def shift_order():
    id, ori = request.json['id'], request.json['from']
    if (ori == 'cook' or ori == 'reception'):
        print('Order id', id, 'from', ori);
    else:
        print('From error !!!')
        abort(500)
    orderListView().shiftOrder(id = id, ori = ori)
    return '/' + ori + '/'

# index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = myData().getMenu())

# cook
@app.route('/cook/', methods=['GET'])
def cook_index():
    return orderListView().showList(status = 'payed')

# reception
@app.route('/reception/', methods=['GET'])
def reception_index():
    return orderListView().showList(status = 'cooked')

# for test!!!
@app.route('/test/', methods=['GET', 'POST'])
def test():
    return render_template('test.html')

if __name__ == '__main__':
    try:
        order.query.all()
    except:
        db.create_all()
    global priceDealerInstance
    priceDealerInstance = priceDealer({})

    #app.run(host = '0.0.0.0', port = 5000, threaded=True)
    app.run(host = '::', port = 5000, threaded=True)
