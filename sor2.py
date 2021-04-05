#!/usr/bin/env python
# coding=utf-8

#__author__:  Administrator
#__date__:  2017/8/14

lis = [1,5,6,3,620,45,14,90]

tmp = lis[0]
for i in lis[1:]:
    if i > tmp:
        tmp = i
    max = tmp
print(max)

