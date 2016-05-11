from web import db

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
    data = db.Column(db.String(1500))
    status = db.Column(db.String(200))
    time = db.Column(db.String(200))


    def __init__(self, bread = '' , meatpie = '' , vegetable = '' , cheese = '', sauce = '', other = '' , status = '', time=  '', data = None):
        if data:
            self.data = str(data)
            self.status = 'prepaying'
            self.status = 'payed'
            self.time = datetime.utcnow()
        else:
            print('Order constructor is NONE !!!')
            abort(500)

    def __repr__(self):
        return '<Order %r>' % self.id

    def getPrice(self):
        global priceDealerInstance
        return priceDealerInstance.calc(self)

    def pay(self):
        if self.status != 'prepaying':
            print("Paying error!")
            abort(500)
        self.status = 'payed'
        db.session.commit()

    def cook(self):
        if self.status != 'payed':
            print("Cooking error!")
            abort(500)
        self.status = 'cooked'
        db.session.commit()

    def finish(self):
        if self.status != 'cooked':
            print("Finishing error!")
            abort(500)
        self.status = 'finished'
        db.session.commit()


    def getDetail(self):
        result = {
            'id': self.id,
            #'price': self.getPrice(),
            'status': self.status,
            'data': eval(self.data),
            'time': self.time
        }
        return result

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
        #return render_template('paying.html', detail = detail)
        #return render_template('index.html', data = myData().getMenu())
        return str(len(order.query.all()))

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
            if (ori == 'cook'):
                cur_order.cook()
            if (ori == 'reception'):
                cur_order.finish()
        else:
            print('ShiftOrder error: No such ORDER: ', id)
            abort(500)
