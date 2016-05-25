#!/usr/bin/python3
#coding=utf-8

from flask import Flask, request, session, render_template, redirect, abort, jsonify
from datetime import datetime
from myData import *
from database import db, order, menu, category
import flask_admin as admin
from flask_admin.contrib import sqla

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'

class priceDealer:
    # a json data, figure out how much every part should be charged
    price = {}

    def __init__(self, price):
        #initialize the price list
        self.price = price

    def calc(self, order):
        # calculate the price of an order
        return 0



class orderView:

    def showMenu(self):
        # show the menu
        return render_template('menu.html')

    def submitOrder(self):
        # submit order and show paying page
        newOrder = order(data = request.json)
        db.session.add(newOrder)
        db.session.commit()
        #detail = newOrder.getDetail()
        #session['myOrder'] = newOrder.id
        o = order.query[len(order.query.all())-1]
        return render_template('paying.html', content = eval(o.data), id = o.id, time = o.time, )

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

    def __init__(self, head = None):
        self.head = [ "编号", "时间", "状态", "食材", "操作" ]

    def showList(self, status = ''):
        if (status == 'cooked' or status == 'payed' ):
            #show list
            orders = order.query.filter_by(status = status).all()
            result = {
                'head': self.head,
                'data': [],
            }
            for item in orders:
                result['data'].append(item.getDetail())
                print(result)
            if (status == 'cooked'):
                return render_template('cook.html', reception = True, data = result)
            if (status == 'payed'):
                return render_template('cook.html', cook = True, data = result)
        else:
            print('ShowList error: No such status: ', status)
            abort(500)

    def shiftOrder(self, id, ori):
        # change order status
        cur_order = order.query.filter_by(id = id).first()
        if cur_order:
            if (ori == 'pay'):
                cur_order.pay()
            if (ori == 'cook'):
                cur_order.cook()
            if (ori == 'reception'):
                cur_order.finish()
        else:
            print('ShiftOrder error: No such ORDER: ', id)
            abort(500)



class OrderAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['id', 'data', 'status', 'time']

class MenuAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['id', 'cid', 'CName', 'sid', 'name', 'cal', 'pro', 'fat', 'car', 'vid']

class CategoryAdmin(sqla.ModelView):
    column_display_pk = True
    form_columns = ['id', 'name']

admin = admin.Admin(app, name='麦德劳营养师御用页面', template_mode='bootstrap3')
#admin.add_view(OrderAdmin(order, db.session))
admin.add_view(MenuAdmin(menu, db.session))
#admin.add_view(CategoryAdmin(category, db.session))

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
    if (ori == 'pay' or ori == 'cook' or ori == 'reception'):
        print('Order id', id, 'from', ori);
    else:
        print('From error !!!')
        abort(500)
    orderListView().shiftOrder(id = id, ori = ori)
    if (ori == 'pay'):
        return '/'
    return '/' + ori + '/'

# index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', data = menu().showmenu())

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
    return render_template('test.html', data = menu().showmenu())

if __name__ == '__main__':
    try:
        order.query.all()
    except:
        db.create_all()
    global priceDealerInstance
    priceDealerInstance = priceDealer({})
    app.run(host = '::', port = 5000, threaded=True, debug = True)
