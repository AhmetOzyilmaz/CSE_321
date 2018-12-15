#!/usr/bin/env python
# coding: utf-8

# In[1]:


def checkpattern(pat, s, patdef):
    madestr = ''.join([patdef[pc] for pc in pat])
    return madestr == s

def removeknownpattern(s, pat, patdef):
    for p in pat:
        pr = patdef[p]
        if pr:
            if s.startswith(pr):
                s = s[len(pr):]
            else:
                return s
        else:
            return s


# In[2]:


def findpattern(s, pat):
    patdef = {}
    up = []
    for c in pat:
        if not c in patdef: 
            patdef[c] = None
            up.append(c)
    
    result = findpatternrec(s, pat, patdef, up)
    if result:
        return True, result
    else:
        return False, None

def findpatternrec(s, pat, patdef, up):
    if up:
        selpattern = up[0]
        restup = up[1:]
        strrest = removeknownpattern(s, pat, patdef)
        
        for i in range(len(strrest)):
            assume = strrest[:i+1]
            patdefassume = patdef.copy()
            patdefassume[selpattern] = assume
            
            r = findpatternrec(s, pat, patdefassume, restup)
            if r:
                return r
    else:
        if checkpattern(pat, s, patdef):
            return patdef
        else:
            None
        
        


# In[5]:


#found, patdef = findpattern('tobeornottobe', 'ABCDAB')
found, patdef = findpattern('dwlxuqfuedwldwlfuesmlsmldwlfuesmlsmlxuq', 'BDZBBZFFBZFFD')
if found:
    print("Yes pattenr is correct", patdef)
else:
    print("Pattenr is not correct")

