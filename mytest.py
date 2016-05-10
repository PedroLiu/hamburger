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
