# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 10:56:42 2019

@author: wpr
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
 
def ch1_1():
    '''
    1.1 解压序列赋值给多个变量
    '''
    print("\nch1_1解压序列赋值给多个变量:")
    data = ["hello", "ch1", ["*","_"],(-6,1,4)]
    _,a,[_,b],(_,middle,_) = data
    
    print(a+b+str(middle))

def ch1_2():
    '''
    1.2 解压可迭代对象赋值给多个变量
    星号表示可变长元组的序列
    想解压一些元素然后丢弃他们，可以使用*_
    '''
    print("\nch1_2:解压可迭代对象赋值给多个变量")
    
    recored = ('Dave', '123','456',4,6)
    head,*_ = recored
    print(head)
   
def ch1_3():
    '''
    1.3 保留最后N个元素
    使用yield表达式的生成器函数 将搜索过程代码和使用搜索结果代码解偶
    '''
    from collections import deque
    print("\nch1_3:解压可迭代对象赋值给多个变量")
    
    def search(lines,pattern,history = 5):
        previous_lines = deque(maxlen = history)
        for li in lines:
            if pattern in li:
                yield li,previous_lines
            previous_lines.append(li)
    with open(r'ch1_3.txt') as f:
        for line, previous in search(f, 'Python', 5):
            for pline in previous:
                print(pline, end =' ')
            print(line, end = ' ')
            print(' ' * 20)

def ch1_4():
    '''
    1.4 查找最大或最小的N个元素
    heapq模块函数 nlargest()和nsmallest()
    '''
    import heapq
    print("\nch1_4:查找最大或最小的N个元素")
    nums = [1,5,2,6,-2,5,6,1,54,12]
    print(heapq.nlargest(3,nums))
    print(heapq.nsmallest(3,nums))
    portfolio = [
   {'name': 'IBM', 'shares': 100, 'price': 91.1},
   {'name': 'AAPL', 'shares': 50, 'price': 543.22},
   {'name': 'FB', 'shares': 200, 'price': 21.09},
   {'name': 'HPQ', 'shares': 35, 'price': 31.75},
   {'name': 'YHOO', 'shares': 45, 'price': 16.35},
   {'name': 'ACME', 'shares': 75, 'price': 115.65}
   ]
   # 以price的值进行比较
   #cheap = heapq.nsmallest(3,portfolio,key = lambda s: s['price'])
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    
    print(cheap)
    print(expensive) 
        
def ch1_5():
    '''
    1.5 实现一个优先队列
    
    '''
    import heapq
    print("\nch1_5:实现一个优先队列")
    
    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0
            
        def push(self, item, priority):
            heapq.heappush(self._queue,(-priority,self._index,item))
            self._index += 1
            
        def pop(self):
            return heapq.heappop(self._queue)[-1]
            
    q = PriorityQueue()
    q.push('1',1)
    q.push('10',10)
    q.push('100',100)
    q.push('25',25)
    q.push('double 100',100)
    q.push('10',10)
    q.push('30',30)

    for i in range(5):
        print(q.pop())     
        
def ch1_6():
    '''
    1.6 字典中的键映射多个值
    defaultdict可以使得代码更加简洁
    '''
    from collections import defaultdict
    print("\nch1_6:字典中的键映射多个值")
    
    
    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['a'].append(3)
    d['b'].append(4)    
    
    print(d)
    
def ch1_7():
    '''
    1.7 字典排序 
    保持元素被插入的顺序 
    '''
    from collections import OrderedDict
    print("\nch1_7:字典排序")
    
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    
    for key in d:
        print(key, d[key])
    
    print(d)

def ch1_8():
    '''
    1.8 字典的运算
    注意 zip 函数创建的是只能访问一次的迭代器
    prices_and_names = zip(prices.values(),prices.key())
    print(min(prices_and_names))
    '''
    print("\nch1_8： 字典的运算")
    scores = {'name1': 34, 'name2':45, 'name3': 98, 'name4':34, 'name5': 66, "name6":90, "name7":90}
    min_score = min(zip(scores.values(),scores.keys()))
    max_score = max(zip(scores.values(),scores.keys()))
    scores_sorted = sorted(zip(scores.values(), scores.keys()),reverse=True)

    print(min_score,max_score)
    print(scores_sorted)

def ch1_9():
    '''
    1.9 查找两字典的相同点
    
    '''
    print("\nch1_9： 查找两字典的相同点")
    a={'x':1,'y':2,'z':3}
    b={'w':100,'x':50,'y':2}

    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items()& b.items())

def ch1_10():
    '''
    1.10 删除序列相同元素并保持顺序
    
    '''
    print("\nch1_10： 删除序列相同元素并保持顺序")
    
    def dedupe(items):
        seen = set()
        for item in items:
            if item not in seen:
                yield item
                seen.add(item)
    a = [1,5,2,1,9,1,5,10]
    print(list(dedupe(a)))
    
def ch1_11():
    '''
    1.11 命名切片
    
    '''
    print("\nch1_11： 命名切片")    
    a = slice(5, 50, 2)    
    s = 'HelloWorld'
    a.indices(len(s))
    print(a)    
    for i in range(*a.indices(len(s))):
        print(s[i])

def ch1_12():
    '''
    1.12 序列中次数出现最多的元素
    使用collections 中的Counter
    '''
    print("\nch1_12： 序列中次数出现最多的元素") 
    from collections import  Counter

    scores_one = [99,89,87,76,98,76,89,92,89,67,59,78,98,92,90,85,56]
    scores_two = [100,89,56,98,78,97,96,99,94,93,91,90]
    one_same_top_three = Counter(scores_one).most_common(3)
    print(one_same_top_three)

    #Counter可以使用各种数学运算操作
    all_same_top_three = ( Counter(scores_one) + Counter(scores_two) ).most_common(5)
    print(all_same_top_three)

def ch1_13():
    '''
    1.13 通过公共键对字典列表排序
    使用operator中的itemgetter得到字典的值
    '''

    print("\nch1_13: 通过公共键对字典列表排序")

    from operator import  itemgetter

    rows = [
        {'fname':'A','lname':'B','uid': 1001},
        {'fname':'B','lname':'C','uid': 1003},
        {'fname':'E','lname':'D','uid': 1002},
        {'fname':'A','lname':'F','uid': 1010},
    ]

    rows_by_uid_and_fname =sorted(rows, key=itemgetter('uid','fname'))

    print(rows_by_uid_and_fname,'\n')

    #使用lambda 如果考虑性能使用itemgetter
    rows_by_uid = sorted(rows, key=lambda s:s['uid'], reverse=True)
    print(rows_by_uid,'\n')

    print(  max(rows, key=itemgetter('uid')) )

def ch1_14():
    '''
    1.14 对不原生支持比较操作的对象排序
    sorted 传入key参数
    '''
    print("\nch1_14: 对不原生支持比较操作的对象排序")

    from operator import  attrgetter  #属性提取

    class User:
        def __init__(self,user_id):
            self.user_id = user_id
        def __repr__(self):
            return 'User({})'.format(self.user_id)

    users = [User(1),User(2),User(3),User(100)]
    users_by_user_id= sorted(users, key=lambda s:s.user_id, reverse=True)

    print(users_by_user_id)

    users_by_user_id= sorted(users, key=attrgetter('user_id'), reverse=True)
    print(users_by_user_id)

    print(max(users, key=attrgetter('user_id')))
    
    
def ch1_15():
    '''
    1.15 根据字段将记录分组
    使用itertools.groupby
    '''

    print("\nch1_15: 根据字段将记录分组")

    from operator import  itemgetter
    from itertools import  groupby

    rows = [
        {'cost': 190, 'date': '07/02/2016'},
        {'cost': 100, 'date':'07/01/2016'},
        {'cost': 10, 'date':'07/18/2016'},
        {'cost': 89, 'date':'07/10/2016'},
        {'cost': 78, 'date':'07/10/2016'},
        {'cost': 1000, 'date':'07/01/2016'}
    ]

    #先按时间排序
    rows.sort(key=itemgetter('date'))

    #分组
    for date, items in groupby(rows,key=itemgetter('date')):
        print(date)
        for i in items:
            print(i)

    #如果不排序，使用一键多值字典
    from collections import  defaultdict

    dict = defaultdict(list)
    for row in rows:
        dict[row['date']].append(row)
    print('\n defaultdict:')
    print(dict['07/01/2016'])

def ch1_16():
    '''
    1.16 筛选序列中的元素
    使用列表推导式和生成器表达式，或者使用itemtools.compress
    '''
    import math
    print("\nch1_16: 筛选序列中的元素")
    mylist=[1,4,-6,9,-7,-5,99,100,-1]
    list1=[n for n in mylist if n > 0]
    print(list1)

    list2 = [math.sqrt(n) for n in mylist if n > 0]
    for i in list2:
        print(i)

    def is_int(val):
        try:
            x = int(val)
            return True
        except ValueError:
            return False
    mylist=['1','2','3','4','-','N/A','5']

    list3 = list(filter(is_int, mylist))
    print(list3)

    numbers = [
        '1',
        '2',
        '3',
        '4'
    ]

    counts=[4,100,9,0]

    from itertools import compress
 
    restult=list(compress(numbers, [n > 5 for n in counts]))
    print(restult)

def ch1_17():
    '''
    1.17 从字典中提取子集
    利用字典推导式

    '''

    print("\nch1_17: 从字典中提取子集")
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55
    }

    p1 = {key:value for key, value in prices.items() if value > 200}
    print(p1)

def ch1_18():
    '''
    1.18 将名称映射到序列的元素中
    使用collections.namedtuple（命名元组)
    命名元组不可变，使用_replace替换元素
    '''

    print("\nch1_18: 将名称映射到序列的元素中")

    from collections import  namedtuple
    Subscriber = namedtuple('Subscriber',['addr','joined'])
    sub = Subscriber('xxx@xx.com','2016-01-01')
    print(sub, sub.addr, sub.joined)

    #替换字典的作用
    s = Subscriber('1@1.com','2016-01-02')
    #命名元组不可变，使用_replace替换元素
    s = s._replace(addr='2@2.com')
    print(s)

def ch1_19():
    '''
    1.19 同时对数据做转换和换算
    '''

    print("\nch1_19: 同时对数据做转换和换算")

    nums = [1,2,3,4,5]
    s = sum(x*x for x in nums)
    print(s)

    import  os
    files = os.listdir('.') # 打开当前目录下的文件夹
    print(files)
    if any(name.endswith(".py") for name in files): # 查看后缀名
        print('Yes')
    else:
        print('No')

def ch1_20():
    '''
    1.20 将多个映射合并为单个映射
    使用collections ChainMap解决
    '''

    print("\nch1_20: 将多个映射合并为单个映射")

    from collections import ChainMap

    a={'x':1,'z':4}
    b={'y':2,'z':3}

    c = ChainMap(a,b) #使用原始的字典
    print(c['x'],c['y'],c['z'])

    print(list(c.keys()),list(c.values()))

    #用新建字典代替
    merged = dict(b)
    merged.update(a)
    print(merged['x'],merged['y'],merged['z'])


def main():
    ch1_1()
    ch1_2()
    ch1_3()
    ch1_4()
    ch1_5()
    ch1_6()
    ch1_7()
    ch1_8()
    ch1_9()
    ch1_10()
    ch1_11()
    ch1_12()
    ch1_13()
    ch1_14()
    ch1_15()    
    ch1_16()    
    ch1_17() 
    ch1_18()
    ch1_19()
    ch1_20()
if __name__ == "__main__":
    main()
    




































































































