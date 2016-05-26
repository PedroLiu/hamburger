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
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.String(30))
    name = db.Column(db.String(30))

class vari(db.Model):
    __tablename__ = 'vari'
    id = db.Column(db.Integer, primary_key=True)
    sid = db.Column(db.String(30))
    sname = db.Column(db.String(30))
    name = db.Column(db.String(30))
    cal = db.Column(db.Integer)
    pro = db.Column(db.Integer)
    fat = db.Column(db.Integer)
    car = db.Column(db.Integer)

    @classmethod
    def getall(self):
        ret = []
        varis = self.query.all()
        for v in varis:
            thisvari = {
                'id': v.id,
                'name': v.name,
                'cal': int(v.cal),
                'pro': int(v.pro),
                'fat': int(v.fat),
                'car': int(v.car),
            }
            ret.append(thisvari)
        return ret

class menu(db.Model):
    __tablename__ = 'menu'
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.String(30))
    CName = db.Column(db.String(30))
    sid = db.Column(db.String(30))
    name = db.Column(db.String(30))
    unit = db.Column(db.Integer)
    pic = db.Column(db.String(100))

    @classmethod
    def showmenu(self):
        result = []
        allcategory = category.query.all()
        for c in allcategory:
            dishes = self.query.filter_by(cid = c.cid).all()
            r = {
                "id": c.cid,
                "name": c.name,
                "item": [],
            }
            for d in dishes:
                thisitem = {
                    'sid': d.sid,
                    'name': d.name,
                    'unit': int(d.unit),
                    'pic': d.pic,
                    'vari': [],
                }
                varis = vari.query.filter_by(sid = d.sid).all()
                for v in varis:
                    thisvari = {
                        'id': v.id,
                        'name': v.name,
                        'cal': int(v.cal),
                        'pro': int(v.pro),
                        'fat': int(v.fat),
                        'car': int(v.car),
                    }
                    thisitem['vari'].append(thisvari)
                r['item'].append(thisitem)
            result.append(r)
        return result
