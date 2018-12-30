#!/usr/bin/env python
# coding: utf-8

# In[20]:


def AliceList(peopleListParam,recognitionsPairsParam,numOfpeopleToChoose,numberOfRecogContraint,numberOfNonContraintCount):
    peoples = list()
    recognitionsPairs = {str: list()}
    recognitionsDataWithCount = {str: (list(),int,int)}# first in recognition # un recogniton count
    recogList = list()
    dic = { str : (list(),int,int)}
    counter  = 0 
    
    peopleList = peopleListParam
    
    #print("Taken peoples : " + str(peopleList))
    
    for elem in peopleList:
        peoples.append(elem)
    
    recognitionsPairs = recognitionsPairsParam
    
    for rec in recognitionsPairs:
        recogList = list()
        counter = 0
        keyStr = str(rec)
        if recognitionsPairs[keyStr] is not  None:
            value = list(recognitionsPairs[rec])
            recogList.append(value)
            counter  = len(value)          
        if rec in recognitionsDataWithCount.keys():
            recogList.append(recognitionsDataWithCount[rec][0])                   
        dic[rec] = (recogList,counter,len(peoples) - counter)
        recognitionsDataWithCount.update(dic)                   

          
    while True:
        for recog in recognitionsDataWithCount:       
            counter+=1
        if recognitionsDataWithCount[recog][1] < numberOfRecogContraint or recognitionsDataWithCount[recog][2] < numberOfNonContraintCount :
            del recognitionsDataWithCount[recog] 
            #print("DELETEEEEDD")
            
        #print("Keys Count  " + str(len(recognitionsDataWithCount.keys())))
        if len(recognitionsDataWithCount.keys()) <= 1 + numOfpeopleToChoose :
            break
        if recognitionsDataWithCount.keys() == numOfpeopleToChoose:
            break
    print("****** Result ******")

    for recog in recognitionsDataWithCount:
        print("Key :")
        print(recognitionsDataWithCount[recog][0]) 
        print(recognitionsDataWithCount[recog][1]) 
        print(recognitionsDataWithCount[recog][2]) 
        print(" \n")
    #as a input takes couples who know each other
    #persons list
    
    return []
    
    #{'AA': 'BB', 'BB': 'CC', 'CC': 'DD', 'DD': 'EE', 'EE': 'FF', 'FF': 'GG'} 


# In[21]:


recognitionsPairs = {"AA":[ "BB","CC","DD","GG","CC"],"BB": ["CC","DD","EE","FF","GG"], "CC": ["DD"], "DD": ["EE"], "EE": ["FF"], "FF": ["GG"]}
peopleList = ["AA", "BB ", "CC ", "DD ", "EE","FF","GG","TT","PP","ZZ","XX","WW"]

AliceList(peopleList,recognitionsPairs,2,5,5)

