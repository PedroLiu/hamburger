class testingClass:
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
                'name':'更多',
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

    def getOrder(self):
        d = {
            "head":[ "编号", "时间", "状态", "食材", "操作" ],
            "data":[
                {'id':10000, 'time':"01:01", 'status':'preparing', 'meatpie': {'item': [{'num': 0, 'sid': 'meat1', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '肉饼'}, 'bread': {'item': [{'num': 0, 'sid': 'bread1', 'name': '松软面包'}, {'num': 0, 'sid': 'bread3', 'name': '面包3'}, {'num': 0, 'sid': 'bread4', 'name': '面包4'}], 'name': '面包'}, 'm4': {'item': [{'num': 0, 'sid': 'm41', 'name': '牛肉'}, {'num': 0, 'sid': 'm42', 'name': '鸡腿肉'}], 'name': '第四种'}, 'm5': {'item': [{'num': 0, 'sid': 'meat51', 'name': '牛肉'}, {'num': 0, 'sid': 'meat52', 'name': '鸡腿肉'}], 'name': '第五种'}, 'caca': {'item': [{'num': 0, 'sid': 'm31', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '第三种'}
                },
                {'id':2, 'time':"01:02", 'status':'s2', 'meatpie': {'item': [{'num': 0, 'sid': 'meat1', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '肉饼'}, 'bread': {'item': [{'num': 0, 'sid': 'bread1', 'name': '松软面包'}, {'num': 0, 'sid': 'bread3', 'name': '面包3'}, {'num': 0, 'sid': 'bread4', 'name': '面包4'}], 'name': '面包'}, 'm4': {'item': [{'num': 0, 'sid': 'm41', 'name': '牛肉'}, {'num': 0, 'sid': 'm42', 'name': '鸡腿肉'}], 'name': '第四种'}, 'm5': {'item': [{'num': 0, 'sid': 'meat51', 'name': '牛肉'}, {'num': 0, 'sid': 'meat52', 'name': '鸡腿肉'}], 'name': '第五种'}, 'caca': {'item': [{'num': 0, 'sid': 'm31', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '第三种'}
                },
                {'id':3, 'time':"03:02", 'status':'s3', 'meatpie': {'item': [{'num': 0, 'sid': 'meat1', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '肉饼'}, 'bread': {'item': [{'num': 0, 'sid': 'bread1', 'name': '松软面包'}, {'num': 0, 'sid': 'bread3', 'name': '面包3'}, {'num': 0, 'sid': 'bread4', 'name': '面包4'}], 'name': '面包'}, 'm4': {'item': [{'num': 0, 'sid': 'm41', 'name': '牛肉'}, {'num': 0, 'sid': 'm42', 'name': '鸡腿肉'}], 'name': '第四种'}, 'm5': {'item': [{'num': 0, 'sid': 'meat51', 'name': '牛肉'}, {'num': 0, 'sid': 'meat52', 'name': '鸡腿肉'}], 'name': '第五种'}, 'caca': {'item': [{'num': 0, 'sid': 'm31', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '第三种'}
                }
            ]
        }

        #print(d['data'][0]['meatpie']['name'])
        return d

