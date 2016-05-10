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
                        'price':1,
                        'pic':'t1.jpg'
                    },
                    {
                        'sid':'bread3',
                        'name':'面包3',
                        'price':3,
                        'pic':'t1.jpg'
                    },
                    {
                        'sid':'bread4',
                        'name':'面包4',
                        'price':4,
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
            },
            {
                'id':'caca',
                'name':'第三种',
                'item': [
                    {
                        'sid':'m31',
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
            },
        {
            'id':'m4',
            'name':'第四种',
            'item': [
                {
                    'sid':'m41',
                    'name':'牛肉',
                    'price':1,
                    'pic':'t1.jpg'
                },
                {
                    'sid':'m42',
                    'name':'鸡腿肉',
                    'price':2,
                    'pic':'t2.jpg'
                }
            ]
        },
        {
            'id':'m5',
            'name':'第五种',
            'item': [
                {
                    'sid':'meat51',
                    'name':'牛肉',
                    'price':1,
                    'pic':'t1.jpg'
                },
                {
                    'sid':'meat52',
                    'name':'鸡腿肉',
                    'price':2,
                    'pic':'t2.jpg'
                }
            ]
        }
        ]
        return data

    def getOrder(self):
        d = {
            "head":[ "编号", "时间", "状态", "内容", "操作" ],
            "data":[
                {'id':1, 'time':"01:01", 'status':'s1', 'meatpie': {'item': [{'num': 0, 'sid': 'meat1', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '肉饼'}, 'bread': {'item': [{'num': 0, 'sid': 'bread1', 'name': '松软面包'}, {'num': 0, 'sid': 'bread3', 'name': '面包3'}, {'num': 0, 'sid': 'bread4', 'name': '面包4'}], 'name': '面包'}, 'm4': {'item': [{'num': 0, 'sid': 'm41', 'name': '牛肉'}, {'num': 0, 'sid': 'm42', 'name': '鸡腿肉'}], 'name': '第四种'}, 'm5': {'item': [{'num': 0, 'sid': 'meat51', 'name': '牛肉'}, {'num': 0, 'sid': 'meat52', 'name': '鸡腿肉'}], 'name': '第五种'}, 'caca': {'item': [{'num': 0, 'sid': 'm31', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '第三种'}
                },
                {'id':2, 'time':"01:02", 'status':'s2', 'meatpie': {'item': [{'num': 0, 'sid': 'meat1', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '肉饼'}, 'bread': {'item': [{'num': 0, 'sid': 'bread1', 'name': '松软面包'}, {'num': 0, 'sid': 'bread3', 'name': '面包3'}, {'num': 0, 'sid': 'bread4', 'name': '面包4'}], 'name': '面包'}, 'm4': {'item': [{'num': 0, 'sid': 'm41', 'name': '牛肉'}, {'num': 0, 'sid': 'm42', 'name': '鸡腿肉'}], 'name': '第四种'}, 'm5': {'item': [{'num': 0, 'sid': 'meat51', 'name': '牛肉'}, {'num': 0, 'sid': 'meat52', 'name': '鸡腿肉'}], 'name': '第五种'}, 'caca': {'item': [{'num': 0, 'sid': 'm31', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '第三种'}
                },
                {'id':3, 'time':"03:02", 'status':'s3', 'meatpie': {'item': [{'num': 0, 'sid': 'meat1', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '肉饼'}, 'bread': {'item': [{'num': 0, 'sid': 'bread1', 'name': '松软面包'}, {'num': 0, 'sid': 'bread3', 'name': '面包3'}, {'num': 0, 'sid': 'bread4', 'name': '面包4'}], 'name': '面包'}, 'm4': {'item': [{'num': 0, 'sid': 'm41', 'name': '牛肉'}, {'num': 0, 'sid': 'm42', 'name': '鸡腿肉'}], 'name': '第四种'}, 'm5': {'item': [{'num': 0, 'sid': 'meat51', 'name': '牛肉'}, {'num': 0, 'sid': 'meat52', 'name': '鸡腿肉'}], 'name': '第五种'}, 'caca': {'item': [{'num': 0, 'sid': 'm31', 'name': '牛肉'}, {'num': 0, 'sid': 'meat2', 'name': '鸡腿肉'}], 'name': '第三种'}
                }
            ]
        }

        #print(d['data'][0]['meatpie']['name'])
        return d

