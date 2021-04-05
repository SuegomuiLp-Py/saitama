#!/usr/bin/env python
# coding=utf-8

#__author__:  Administrator
#__date__:  2017/8/14

lis = [1,5,6,3,620,45,14,90]
def maxnum(arg):
    tmp = arg[0]
    for i in arg[1:]:
        if i > tmp:
            tmp = i
        max = tmp
    return max

def minnum(arg):
    tmp = arg[0]
    for i in arg[1:]:
        if i < tmp:
            tmp = i
        min = tmp
    return min

a=maxnum(lis)
b=minnum(lis)
print(a)
print(b)

# def getmax(arg):
#     ret = max(arg)
#     print(ret)
