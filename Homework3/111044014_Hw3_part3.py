#!/usr/bin/env python
# coding: utf-8

# In[1]:


def divideAndConquer(a,globalIndex=0):
    if len(a) == 0:
        return []
    if len(a) == 1:
        if a[0] == globalIndex:
            return [globalIndex]
        else:
            return []
    else:
        n2=int(len(a)/2)
        
        left, right = a[:n2], a[n2:]
        
        return divideAndConquer(left, globalIndex) + divideAndConquer(right, globalIndex+n2)

