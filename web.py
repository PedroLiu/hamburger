#!/usr/bin/python3

from flask import Flask, request, session, render_template, redirect, abort
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)


class priceDealer:
    # a json data, figure out how much every part should be charged
    price = {}

    def init(self, price):
        #initialize the price list
        self.price = price

    def calc(self, order):
        # calculate the price of an order
        return 0

class order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bread = db.Column(db.String(30))
    meatpie = db.Column(db.String(30))
    vegetable = db.Column(db.String(30))
    cheese = db.Column(db.String(30))
    sauce = db.Column(db.String(30))
    other = db.Column(db.String(30))
    status = db.Column(db.String(30))
    time = db.Column(db.String(30))


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
        #submit order and show paying page
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

    def showList(self):
        #show list
        return render_template('orderlist.html')



@app.route('/test/', methods=['GET', 'POST'])
def test():
    return render_template('test.html')


try:
    User.query.all()
except:
    db.create_all()

app.run(host = '0.0.0.0', port = 80, threaded=True)
