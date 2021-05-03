# -*- coding: utf-8 -*-
"""
TECHLEXA
"""
import datetime
now = datetime.datetime.now()
import random
coin = [ "Heads" , "Tails"]
great = ["Hello!","Its nice to meet you" , "It's a pleasure to meet you"]
print("Hi I am your own Techlexa")
que = "y"
print("These are the following commands I could do : \n1.Tell Time!!")
print("2.Do heads and tails ")
print("3.Greet you too!!")
while que == "y" :
    toss = random.choice(coin)
    dya = random.choice(great)
    a = int(input("Enter the command number : "))
    if a == 1 :
        now = datetime.datetime.now()
        print("current date and time is :")
        print(now.strftime("%d-%m-%y %H:%M:%S"))
    elif a== 2 :
        print(toss)
    elif a==3 :
        print(dya)
    else :
        print("Don't just prank me !!")
    que = input("Do u wish to continue ? y/n")

   
        
        
 
        
    
    

