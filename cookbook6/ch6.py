# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 14:48:07 2019

@author: peirong
"""


def ch6_1():
    '''
    6.1 读写 CSV 数据  
    '''
    import csv     
    print("\nch6_1: 读写 CSV 数据 ")
    
    with open('stocks.csv') as f:
        f_csv = csv.reader(f) 
        for row in f_csv: #row 会是一个列表
            print(row) #为了访问某个字段，你需要使用下标，如 row[0] 访问 Symbol， row[4] 访问 Change。
    
    #由于这种下标访问通常会引起混淆，你可以考虑使用命名元组
    print('Reading as namedtuples')
    from collections import namedtuple
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        Row = namedtuple('Row', next(f_csv))
        for r in f_csv: 
            # Process row
            print('    ', row)
             
    with open('stocks.csv') as f:
        f_csv = csv.DictReader(f)#将数据读取到一个字典序列中去
        for row in f_csv:
            print(row)
            
    headers = ['Symbol','Price','Date','Time','Change','Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
    ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
    ]
    with open('stock.csv','w') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)
        
    col_types = [str, float, str, str, float, int]
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            # Apply conversions to the row items
            row = tuple(convert(value) for convert, value in zip(col_types, row))
            print(row)
        
    print('Reading as dicts with type conversion')

    field_types = [ ('Price', float),
                    ('Change', float),
                    ('Volume', int) ]
    
    with open('stocks.csv') as f:
        for row in csv.DictReader(f):
            row.update((key, conversion(row[key])) 
                       for key, conversion in field_types)
            print(row)        
def main(): 
    for i in range(1,2):
        func = 'ch6_%d()'%(i)
        exec(func) 
        


if __name__ == "__main__":
    main()