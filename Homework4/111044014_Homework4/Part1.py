#!/usr/bin/env python
# coding: utf-8

# In[3]:
# Implemented by Ahmet ÖZYILMAZ


def optimalHotels(hotels):
    optimalPath = [int] * len(hotels)
    optimalStop = [int] * len(hotels)
    for i in range(0,len(hotels)):
        optimalStop[i] = 0
        optimalPath[i] = 0

    for i in range(1,len(hotels)): # takes O(i)
        optimalPath[i] = int(pow((200 - (hotels[i-1] - hotels[i])),2))
        for j in range(0,i-1):# takes O(i)
            optimalPath[j] = 0
            if optimalPath[j] + pow((200 - (hotels[i] - hotels[j])), 2) < optimalPath[i]:
                optimalPath[i] = (int) (optimalPath[j] + pow((200 - (hotels[i] - hotels[j])), 2))
                optimalStop[i] = j + 1
                
    print("Minimal Penalty :")
    print(optimalPath[len(hotels)- 1]) 
    finalPath = ""
    index = len(optimalStop)-1
    while(index >= 0):
        finalPath = str(index+1)+" "+str(finalPath)
        index = optimalStop[index]-1
    print(optimalStop)
    print("Stop at: ") 
    print(finalPath)
# n        n         n(n-1)
# ΣO(i) = O (Σi) = O ----- = O(n ^ 2)
# i=1    i=1            2

#
#
#
#
#

