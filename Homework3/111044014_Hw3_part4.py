#!/usr/bin/env python
# coding: utf-8

# In[1]:


def maxSubArray(array):
    n = len(array)
    if(n <= 2):
        return {0,0,0 * float("inf")}
    i = n
    j = 1
    TList = array[0] + array[n-1]
    s= n -1 
    t = 2
    sl = array[t]
    sr = array[s]
    while s > t:
        if sr >= sl:
            s -= 1
            if sr >= 0:
                TList + sr
                i = s + 1
                sr = array[s]
            else:
                sr = sr + array[s]
        else :
            t += 1
            if sl > 0:
                t+= sl
                j = t-1
                if t < len(array):
                    sl = array[t]
            else:
                sl = sl + array[t]
    return {i,j,TList}
                


# In[3]:


array  =[6,7,-6,7]
response = maxSubArray(array)
print(response)


# In[ ]:




