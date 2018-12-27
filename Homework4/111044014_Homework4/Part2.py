#!/usr/bin/env python
# coding: utf-8

# In[77]:


dictionaryList = ["one","wa","itwas","itw","it","was","the","best","of","times"]

        
def main(string):
    size = len(string)
    dynamicList = [""] * size    
    print("Array Size: " + str (size)) 
    correctList = [] 
    
    for i in range(1,size):
        index = 1
        for j in range (i-1,size):          
            dynamicList[j] = string[:j]
            if(IsValid(dynamicList[j])):
                print("This is Valid Word : " + dynamicList[j])
                correctList.append(dynamicList[j])
                string = string[j:]  
                print(string)
        
    print("Dynamic List :")
    print(dynamicList)
    print("Result List :" )
    print(correctList)

    return "True"

def IsValid(str):
    return str in dictionaryList


# In[78]:


main("itwasthebestoftimesitwas")

