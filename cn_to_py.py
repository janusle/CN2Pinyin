#!/usr/bin/python
#coding=utf-8

# This program convert Chinese character to pinyin
# The dictionary file contains Chinese Unicode to Hanyu Pinyin mapping
# is from internet, named "uc-to-py.tbl" The author is stolfi
# The program is tested on Ubuntu9.04, MacOS X and SunOS
# author: Le Yan
import sys
pinyin_tbl = {}


#get the unicode of a Chinese character
def toHex(s):
    st=''
    for ch in s:
        st=st+hex(ord(ch)).replace("0x","")

    return st.upper()




#initialize the table of unicode to pinyin
def init():
    f = open('uc-to-py.tbl', 'r')
    for line in f:
      ls = line.split(" ")
      key = ls[0]
    #  value = ls[1]
      value=ls[1][1:-2].split(',')
      pinyin_tbl[key] = value




def querying(code):
    pinyin = pinyin_tbl[code][0][0:-1]
    return pinyin





#split the Chinese string and return a list
def splitChinese(st):
    l = list(unicode(st,'utf8'))
    return l





def chinese_to_pinyin(st):
    result=""
    l = splitChinese(st)
    i = 1
    for ch in l:
        if i == 1:
            result = querying(toHex(ch)).capitalize() + " "
            i = i + 1
        else:
            result = result + querying(toHex(ch))
    return result;



#Program starts here
init()
if len(sys.argv) < 2:
    print 'Please input the Chinese character: '
else:
    print chinese_to_pinyin(sys.argv[1])






