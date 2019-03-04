# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 08:19:12 2019

@author: wpr
"""
 

def ch2_1():
    '''
    2.1 使用多个界定符分割字符串
    一个字符串中的分隔符不固定需要使用re.split开灵活切割字符串
    
    区分捕获分组和非捕获分组
    '''

    print("\nch2_1: 使用多个界定符分割字符串")

    import  re
    line = '我,是中国;人,你是-哪国人'
    result = re.split(r'[ ;,-]\s*', line)
    print(result)
    fields = re.split(r'(;|,|\s|-)\s*', line)
    print(fields)
    values = fields[::2]
    print(values)
def ch2_2():
    '''
    2.2  在字符串的开头或者结尾处做文本匹配
    startswith和endswith
    必须使用tuple类型
    '''

    print("\nch2_2: 在字符串的开头或者结尾处做文本匹配")

    import  os
    filenames = os.listdir(".")
    md_file = [file for file in filenames if file.endswith((".py",".MD"))]
    print(md_file)

    https = ["https:","HTTPS:"]
    urls =["http://baidu.com","www.qq.com:80","https://github.com","ftp://mirror.aliyun.com"]
    https_url = [url for url in urls if url.startswith(tuple(https))]
    print(https_url)

    #使用正则
    import  re
    result=re.match(r"^(https:)","https://github.com")
    if result:
        print(result.groups())
    else:
        print("no result")


def ch2_3():
    '''
    2.3 利用Shell通配符做字符串匹配
    使用fnmatch模块中的fnmatch和fnmatchcase
    '''

    print("\nch2_3: 利用Shell通配符做字符串匹配")

    from fnmatch import fnmatch,fnmatchcase

    #fnmatch按照平台是否区分大小写，window不区分
    files = ["config.ini","data1.csv","data2.csv","ata_train.csv","README.md","CONTINUE.MD"]
    print(files)

    data_file = [file for file in files if fnmatch(file,"data*.csv")]
    print(data_file)

    #fnmatchcase 可以区分大小写
    print(files)
    data_file = [file for file in files if fnmatchcase(file, "*.MD")]
    print(data_file)


def ch2_4():
    '''
    2.4 文本模式的匹配和查找
    使用正则
    先将模式字符串预编译为模式对象
    findall() 方法会搜索文本并以列表形式返回所有的匹配
    '''

    print("\nch2_4: 文本模式的匹配和查找")

    text1 = "02/11/2017"
    text2 = "02/11/2017 tomorrow is 02/12/2017"

    import  re
    if re.match(r"\d+/\d+/\d+", text1):
        print("yes")
    else:
        print("no")

    date_p = re.compile(r"\d+/\d+/\d+")
    if date_p.match(text1):
        print("yes")
    else:
        print("no")

    result = date_p.findall(text2)
    print(result)

    #增加捕获组  多次匹配或者查找，建议先编译
    date_p = re.compile(r"(\d+)/(\d+)/(\d+)")
    result  = date_p.findall(text2)
    for month,day, year in result:
        print("{}-{}-{}".format(year,month,day))


def ch2_5():
    '''
    2.5 对字符串中的文本做查找和替换
    re.sub
    '''

    print("\nch2_5: 对字符串中的文本做查找和替换")

    text1 ="Today is 02/11/2017, 春节是02/26/2017"

    import re

    #先匹配，后替换 
    result = re.sub(r"(\d+)/(\d+)/(\d+)",r"\3-\1-\2", text1)
    print(result)

    data_p = re.compile(r"(\d+)/(\d+)/(\d+)")

    from calendar import  month_abbr

    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

    result,count = data_p.subn(change_date, text1)
    print("结果:",result, "\n总共替换:", count)



def ch2_6():
    '''
    2.6 以不区分大小写的方式对文本做检查和替换
    使用re.IGNORECASE
    
    类似于一个回调函数
    '''
    print("\nch2_6: 以不区分大小写的方式对文本做检查和替换")

    text = "UPPER PYTHON, lower python, Mixed Python"

    import  re
    result = re.findall(r"python", text, flags=re.IGNORECASE)
    print(result)

    #替换成相同的格式
    result = re.sub("python", "snake", text, flags=re.IGNORECASE)
    print(result)  #注意snake是全部小写

    def matchcase(word):
        def replace(m):
            text = m.group()
            if text.isupper():
                return word.upper()
            elif text.islower():
                return word.lower()
            elif text[0].isupper():
                return  word.capitalize()
            else:
                return word
        return  replace

    result = re.sub("python", matchcase("snake"), text, flags=re.IGNORECASE)
    print(result)

def ch2_7():
    '''
    2.7 最短匹配模式
    模式 r'n"(.*)n"' 的意图是匹配被双引号包含的文本。
    '''
    import re
    print("\nch2_7: 最短匹配模式")
    
    #需要匹配一对分隔符之间的文本的时候 (比如引号包含的字符串)。
    str_pat = re.compile(r'\"(.*)\"')
    text1 = 'Computer says "no."'
    result = str_pat.findall(text1)
    print(result)
    
    text2 = 'Computer says "no." Phone says "yes."'
    result = str_pat.findall(text2)
    print(result)

def ch2_8():
    '''
    2.8 多行匹配模式 
    '''
    import re
    print("\nch2_8: 多行匹配模式")
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = '''/* this is a
    multiline comment */
    '''
    result = comment.findall(text1)
    print(result)
    
    result = comment.findall(text2)
    print(result)
    
    comment = re.compile(r'/\*((?:.j\n)*?)\*/')
    print(comment.findall(text2))
    
    comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
    print(comment.findall(text2))
    
    
def ch2_9():
    '''
    2.9 将 Unicode 文本标准化 
    ''' 
    import unicodedata
    print("\nch2_9: 将 Unicode 文本标准化")
    s1 = 'Spicy Jalape\u00f1o'
    s2 = 'Spicy Jalapen\u0303o'
    print(s1 == s2)
    print(s1)
    t1 = unicodedata.normalize('NFC', s1)
    t2 = unicodedata.normalize('NFC', s2)
    print(t1 == t2)
    print(ascii(t1))
    t3 = unicodedata.normalize('NFD', s1)
    t4 = unicodedata.normalize('NFD', s2)
    print(t3 == t4)
    print(ascii(t3))
    
def main():

    for i in range(1,10):
        func = 'ch2_%d()'%(i)
        exec(func) 


if __name__ == "__main__":
    main()