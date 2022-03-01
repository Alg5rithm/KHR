# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 17:28:19 2022

@author: fud37
"""

li = list(map(int, input().split()))

answer = [1,2,3,4,5]

def change(li, a, b):
    temp = li[a]
    li[a] = li[b]
    li[b] = temp
def printNumber(li):
    for i in range(5):
        print(li[i], end= ' ')
    print()
    
flag = 0
while True :
    if li[0] > li[1]:
        change(li, 0, 1)
        printNumber(li)
    
    if li[1] > li[2]:
        change(li, 1, 2)
        printNumber(li)
    
    if li[2] > li[3] :
        change(li, 2, 3)
        printNumber(li)
    
    if li[3] > li[4]:
        change(li, 3,4)
        printNumber(li)

    if answer == li : 
        break
