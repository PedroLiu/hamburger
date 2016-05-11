#!/usr/bin/python3
#coding=utf-8
from flask import Flask, request, session, render_template, redirect, abort, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
from mytest import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)


class priceDealer:
    # a json data, figure out how much every part should be charged
    price = {}

    def __init__(self, price):
        #initialize the price list
        self.price = price

    def calc(self, order):
        # calculate the price of an order
        return 0

class order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bread = db.Column(db.String(200))
    meatpie = db.Column(db.String(200))
    vegetable = db.Column(db.String(200))
    cheese = db.Column(db.String(200))
    sauce = db.Column(db.String(200))
    other = db.Column(db.String(200))
    status = db.Column(db.String(200))
    time = db.Column(db.String(200))


    def __init__(self, bread = '' , meatpie = '' , vegetable = '' , cheese = '', sauce = '', other = '' , status = '', time=  ''):
        self.bread = ''
        self.meatpie = ''
        self.vegetable = ''
        self.cheese = ''
        self.sauce = ''
        self.other = ''
        self.status = ''
        self.time = ''

    def __repr__(self):
        return '<Order %r>' % self.id

    def getOrder(self):
        try:
            self.bread = request.form['bread']
            self.meatpie = request.form['meatpie']
            self.vegetable = request.form['vegetable']
            self.cheese = request.form['cheese']
            self.sauce = request.form['sauce']
            self.other = request.form['other']
            self.status = 'prepaying'
            self.time = datetime.utcnow()
        except:
            abort(500)

    def getPrice(self):
        global priceDealerInstance
        return priceDealerInstance.calc(self)

    def pay(self):
        if self.status != 'prepaying':
            abort(500)
            self.status = 'payed'
            db.session.commit()

    def cook(self):
        if self.status != 'payed':
            abort(500)
            self.status = 'cooking'
            db.session.commit()

    def deliver(self):
        if self.status != 'cooking':
            abort(500)
            self.status = 'delivering'
            db.session.commit()

    def finish(self):
        if self.status != 'delivering':
            abort(500)
            self.status = 'finished'
            db.session.commit()


    def getDetail(self):
        result = {
            'id': self.id,
            'bread': self.bread,
            'meatpie': self.meatpie,
            'vegetable': self.vegetable,
            'cheese': self.cheese,
            'sauce': self.sauce,
            'other': self.other,
            'price': self.getPrice(),
            'status': self.status,
        }
        return result

class orderView:

    def showMenu(self):
        # show the menu
        return render_template('menu.html')

    def submitOrder(self):
        # submit order and show paying page
        newOrder = order()
        newOrder.getOrder()
        db.session.add(newOrder)
        db.session.commit()
        detail = newOrder.getDetail()
        session['myOrder'] = newOrder.id
        return render_template('paying.html', detail = detail)

    def pay(self):
        #pay an order
        if session.get('myOrder', None) == None:
            abort(500)
            myOrder = order.query.filter_by(id = session['myOrder']).first()
            myOrder.pay()
            detail = myOrder.getDetail()
            return render_template('payed.html', detail = detail)

    def finish(self):
        #finish an order
        if session.get('myOrder', None) == None:
            abort(500)
            myOrder = order.query.filter_by(id = session['myOrder']).first()
            myOrder.finish()
            detail = myOrder.getDetail()
            return render_template('finished.html', detail = detail)




class orderListView:

    def showPayedList(self):
        #show list
        orders = order.query.filter_by(status='payed').all()
        result = []
        for item in orders:
            result.append(item.getDetail())

        return result

    def showCookedList(self):
        #show list
        orders = order.query.filter_by(status='cooked').all()
        result = []
        for item in orders:
            result.append(item.getDetail())

        return result


# get menu data
@app.route('/api/getorder/', methods=['GET'])
def get_menu():
    # get menu data from database
    data = testingClass().menu()
    # return a json
    return jsonify(data)

# post a new order
@app.route('/api/neworder/', methods=['POST'])
def new_order():
    # show the request for testing
    print(request.json);
    for k in request.json:
        print(k, '=', request.json[k])
    #return jsonify(request.json)
    # back to menu
    return '/'

# change state
@app.route('/api/shift/', methods=['POST'])
def shift_order():
    print(request.json);
    if (request.json['from'] == 'cook'):
        print('cook has done ', request.json['id']);
    elif (request.json['from'] == 'reception'):
        print('reception has send ', request.json['id']);
    else:
        print('Error !!!')
        abort(500)
    return '/' + request.json['from'] + '/'

# index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = testingClass().getMenu())

# cook
@app.route('/cook/', methods=['GET'])
def cook_index():
    #return render_template('cook.html', cook = True, data = testingClass().getOrder())
    return render_template('cook.html', cook = True, data = testingClass().getOrder())

# reception
@app.route('/reception/', methods=['GET'])
def reception_index():
    return render_template('cook.html', reception = True, data = testingClass().getOrder())

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

    app.run(host = '0.0.0.0', port = 5000, threaded=True)
