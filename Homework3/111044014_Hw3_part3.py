#!/usr/bin/env python
# coding: utf-8

# In[21]:


def findaii(a,starti=0):
    if len(a) == 0:
        return []
    if len(a) == 1:
        if a[0] == starti:
            return [starti]
        else:
            return []
    else:
        n2=int(len(a)/2)
        
        left, right = a[:n2], a[n2:]
        
        return findaii(left, starti) + findaii(right, starti+n2)


# In[22]:


findaii([1,9,2,4,5,6,7,32,8] )

