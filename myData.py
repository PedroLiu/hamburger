#!/usr/bin/python3
#coding=utf-8

import random
from database import db, menu, category
class myData:
    def getMenu(self):
        data = [
            {
                'id':'bread',
                'name':'面包',
                'item': [
                    {
                        'sid':'bread1',
                        'name':'松软面包',
                        'price':2,
                        'pic':'bread1.jpg'
                    },
                    {
                        'sid':'bread2',
                        'name':'白面包',
                        'price':2,
                        'pic':'bread2.jpg'
                    },
                    {
                        'sid':'bread3',
                        'name':'巨菜叶',
                        'price':1,
                        'pic':'bread3.jpg'
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
                        'price':5,
                        'pic':'meat1.jpg'
                    },
                    {
                        'sid':'meat2',
                        'name':'鸡腿肉',
                        'price':3,
                        'pic':'meat2.jpg'
                    },
                    {
                        'sid':'meat3',
                        'name':'鳕鱼肉',
                        'price':4,
                        'pic':'meat3.jpg'
                    },
                    {
                        'sid':'meat4',
                        'name':'虾肉',
                        'price':4,
                        'pic':'meat4.jpg'
                    }
                ]
            },
            {
                'id':'vegetable',
                'name':'蔬菜',
                'item': [
                    {
                        'sid':'veg1',
                        'name':'生菜',
                        'price':1,
                        'pic':'veg1.jpg'
                    },
                    {
                        'sid':'veg2',
                        'name':'番茄',
                        'price':2,
                        'pic':'veg2.jpg'
                    },
                    {
                        'sid':'veg3',
                        'name':'辣椒圈',
                        'price':1,
                        'pic':'veg3.jpg'
                    },
                    {
                        'sid':'veg4',
                        'name':'洋葱',
                        'price':2,
                        'pic':'veg4.jpg'
                    }
                ]
            },
            {
                'id':'cheese',
                'name':'芝士',
                'item': [
                    {
                        'sid':'cheese1',
                        'name':'黄芝士',
                        'price':2,
                        'pic':'cheese1.jpg'
                    },
                    {
                        'sid':'cheese2',
                        'name':'白芝士',
                        'price':2,
                        'pic':'cheese2.jpg'
                    },
                    {
                        'sid':'cheese3',
                        'name':'芝士条',
                        'price':2,
                        'pic':'cheese3.jpg'
                    }
                ]
            },
            {
                'id':'sauce',
                'name':'酱料',
                'item': [
                    {
                        'sid':'sauce1',
                        'name':'芥末酱',
                        'price':1,
                        'pic':'sauce1.jpg'
                    },
                    {
                        'sid':'sauce2',
                        'name':'蛋黄酱',
                        'price':1,
                        'pic':'sauce2.jpg'
                    },
                    {
                        'sid':'sauce3',
                        'name':'烧烤酱',
                        'price':1,
                        'pic':'sauce3.jpg'
                    },
                    {
                        'sid':'sauce4',
                        'name':'香辣酱',
                        'price':1,
                        'pic':'sauce4.jpg'
                    },
                    {
                        'sid':'sauce5',
                        'name':'千岛酱',
                        'price':1,
                        'pic':'sauce5.jpg'
                    },
                    {
                        'sid':'sauce6',
                        'name':'番茄酱',
                        'price':1,
                        'pic':'sauce6.jpg'
                    }
                ]
            },
            {
                'id':'other',
                'name':'其他',
                'item': [
                    {
                        'sid':'bacon',
                        'name':'培根',
                        'price':3,
                        'pic':'bacon.jpg'
                    },
                    {
                        'sid':'Avogadro',
                        'name':'牛油果泥',
                        'price':3,
                        'pic':'Avogadro.jpg'
                    },
                    {
                        'sid':'cornchip',
                        'name':'玉米脆片',
                        'price':2,
                        'pic':'cornchip.jpg'
                    },
                    {
                        'sid':'friedmushroom',
                        'name':'香煎蘑菇',
                        'price':1,
                        'pic':'friedmushroom.jpg'
                    },
                    {
                        'sid':'omelette',
                        'name':'煎蛋',
                        'price':1,
                        'pic':'omelette.jpg'
                    }
                ]
            }
        ]
        return data

if (__name__ == '__main__'):
    d = myData()
    db.create_all()
    data = d.getMenu()
    for item in data:
        c = category()
        c.id = item['id']
        c.name = item['name']
        db.session.add(c)
        db.session.commit()
        for dish in item['item']:
            d = menu()
            d.cid= item['id']
            d.CName = item['name']
            d.sid = dish['sid']
            d.name = dish['name']
            d.unit = dish['price']
            d.pic = dish['pic']
            d.cal = random.randint(0,100)
            d.pro = random.randint(0,100)
            d.fat = random.randint(0,100)
            d.car = random.randint(0,100)
            d.vid = 'None'
            db.session.add(d)
            db.session.commit()
