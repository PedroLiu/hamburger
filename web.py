#!/usr/bin/python3

from flask import Flask, request, session, render_template, redirect, abort, jsonify
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

    def showList(self):
        #show list
        return render_template('orderlist.html')

class testingClass:
    def getorder(self):
        data = [
            {
                'id':'bread',
                'name':'面包',
                'item': [
                    {
                        'sid':'bread1',
                        'name':'松软面包',
                        'price':1,
                        'pic':'t1.jpg'
                    },
                    {
                        'sid':'bread2',
                        'name':'白面包',
                        'price':2,
                        'pic':'t2.jpg'
                    }
                ]
            },

            {
                'id':'meatpie',
                'name':'肉饼',
                'item': [
                    {
                        'sid':'meat1',
                        'name':'牛肉',
                        'price':1,
                        'pic':'t1.jpg'
                    },
                    {
                        'sid':'meat2',
                        'name':'鸡腿肉',
                        'price':2,
                        'pic':'t2.jpg'
                    }
                ]
            }
        ]
        return data


    def menu(self):
        d = {
            'cate': ['bread', 'meatpie', 'vegetable', 'cheese', 'sauce', 'other'],
            'bread': [ u'松软面包', u'白面包', u'巨菜叶' ],
            'meatpie': [ '牛肉', '鸡腿肉', '鳕鱼肉', '虾肉' ],
            'vegetable': [ '生菜', '收菜' ],
            'cheese': [ 'ch1', 'ch2' ],
            'sauce': [ 's1', 'asf' ],
            'other': [ 'o1', '02', 'o3' ],
            'bye': [
                '着急吃不了(热)豆腐哟~',
                '打把炉石就给您端上来了~',
                '请皇上稍等，微臣这就去安排~',
                '能不能给我一首歌的时间？'
            ]
        }
        return d

# get menu data
@app.route('/api/getorder', methods=['GET'])
def get_menu():
    # get menu data from database
    data = testingClass().menu()
    # return a json
    return jsonify(data)

# post a new order
@app.route('/api/neworder', methods=['POST'])
def new_order():
    # show the request for testing
    for k,v in request.form.items():
        print(k, '=', request.form[k])
    # back to menu
    return redirect('/')

# index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = testingClass().getorder())

# cook
@app.route('/cook', methods=['GET'])
def cook_index():
    return render_template('cook.html', data = testingClass().getorder())

# for test!!!
@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')

try:
    User.query.all()
except:
    db.create_all()

app.run(host = '0.0.0.0', port = 5000, threaded=True)
