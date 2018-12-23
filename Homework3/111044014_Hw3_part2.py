#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
def TakeAStamp(stampNum):
    takedStamp = 0
    if(stampNum <= 0):
        return 0,0
    if 0 == (stampNum % 3):
        takedStamp = random.randint(1, 2)
        stampNum-= takedStamp
    else :
         while (stampNum%3) != 0:
            takedStamp+=1
            stampNum -= 1
    return stampNum,takedStamp
def TakeInput():
    while True:
        order = int(input("Please Enter Number of will take stamp"))
        if order < 3 and order > 0:
            break
        else:
            print("Please enter 1 or 2")
    return order

def PlayerMove(stampNum):
    move = TakeInput()
    stampNum -= move   
    print("Last ", stampNum,"Stamp")
    if stampNum < 0:
        stampNum = 0
    return int(stampNum),move         
#Main Method For Game
def OnePileNIMPlay(numberOfStamp):
     while numberOfStamp > 0:
        #for player 1
        response = PlayerMove(numberOfStamp)
        numberOfStamp = response[0]
        print("Player 1 took ",response[1])
        if numberOfStamp >= 1 | numberOfStamp <= 2:
            print("Player 1 is won ********************")
            break
        #for player2
        response = TakeAStamp(numberOfStamp)
        numberOfStamp= response[0]
        print("Computer took ",response[1])
        print("Last ", numberOfStamp,"Stamp")
        if numberOfStamp >= 1 | numberOfStamp <= 2:
            print("Computer is won")


# In[2]:


OnePileNIMPlay(20)

