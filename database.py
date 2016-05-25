#coding=utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456790'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(3000))
    status = db.Column(db.String(200))
    time = db.Column(db.String(200))


    def __init__(self, bread = '' , meatpie = '' , vegetable = '' , cheese = '', sauce = '', other = '' , status = '', time=  '', data = None):
        if data:
            self.data = str(data)
            self.status = 'prepaying'
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


class category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))

class menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.String(100))
    CName = db.Column(db.String(100))
    sid = db.Column(db.String(100))
    name = db.Column(db.String(100))
    unit = db.Column(db.String(100))
    pic = db.Column(db.String(100))
    cal = db.Column(db.String(100))
    pro = db.Column(db.String(100))
    fat = db.Column(db.String(100))
    car = db.Column(db.String(100))
    vid = db.Column(db.String(100))

    @classmethod
    def showmenu(self):
        result = []
        allcategory = category.query.all()
        for c in allcategory:
            dishes = self.query.filter_by(cid = c.id).all()
            r = {
                "id": c.id,
                "name": c.name,
                "item": [],
            }
            for d in dishes:
                thisitem = {
                    'sid': d.sid,
                    'name': d.name,
                    'unit': int(d.unit),
                    'pic': d.pic,
                    'cal': d.cal,
                    'pro': d.pro,
                    'fat': d.fat,
                    'car': d.car,
                }
                r['item'].append(thisitem)
            result.append(r)
        return result
