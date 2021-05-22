# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:07:49 2020

@author: TechClub
"""

""" Program for Memory Game
Program displays one by one 8 Numbers for 10 Sec.
User needs to memorize the numbers as well as sequence,
Then User needs to enter those numbers"""

from random import randint as r
import time
import sys

num1=0
num2=0
num3=0
num4=0
num5=0
num6=0
num7=0
num8=0
prevNum=0
done=0


num=r(1,100)
if prevNum != num:
    prevNum=num
    num1=num
    print(num1)
    time.sleep(1)
    
while done==0:
    num=r(1,100)
    if prevNum != num:
        prevNum=num
        num2=num
        done=1
        print(num2)
        time.sleep(1)

while done==1:
    num=r(1,100)
    if prevNum != num:
        prevNum=num
        num3=num
        done=2 
        print(num3)
        time.sleep(1)
        
while done==2:
    num=r(1,100)
    if prevNum != num:
        prevNum=num
        num4=num
        done=3 
        print(num4)
        time.sleep(1)
        
while done==3:
    num=r(1,100)
    if prevNum != num:
        prevNum=num
        num5=num
        done=4 
        print(num5)
        time.sleep(1)
        
while done==4:
    num=r(1,100)
    if prevNum != num:
        prevNum=num
        num6=num
        done=5 
        print(num6)
        time.sleep(1)
        
while done==5:
    num=r(1,100)
    if prevNum != num:
        prevNum=num
        num7=num
        done=6 
        print(num7)
        time.sleep(1)
        
while done==6:
    num=r(1,100)
    if prevNum != num:
        prevNum=num
        num8=num
        done=7 
        sys.stdout.write(str(num8))
        time.sleep(1)
        
sys.stdout.flush()