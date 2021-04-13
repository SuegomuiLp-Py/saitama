#!/usr/bin/env python
# coding=utf-8

#__author__:  Administrator
#__date__:  2017/8/14

def enter():
    lis = []
    while 1:
        num = input('enter a num:')
        if num == 'q':
            return lis
        lis.append(int(num))
    return lis

def fallist(arg):
    tmplist = []
    if isinstance(arg,list):
        for i in arg:
            if isinstance(i,str):
                print('Error')
                return False
        flag = 1
        while flag:
            if not arg:
                break
            tmp = max(arg)
            tmplist.append(tmp)
            arg.remove(tmp)
        return tmplist

def raiselist(arg):
    tmplist = []

    if isinstance(arg, list):
        for i in arg:
            if isinstance(i,str):
                print('Error')
                return False
        flag = 1
        while flag:
            if not arg:
                break
            tmp = min(arg)
            tmplist.append(tmp)
            arg.remove(tmp)
        return tmplist

ret = enter()
rets = ret.copy()
a = raiselist(ret)
print(a)
b = fallist(rets)
print(b)