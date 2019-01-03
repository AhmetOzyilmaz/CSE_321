#!/usr/bin/env python
# coding: utf-8

# In[6]:


def createCost(ny, sf):
    return [{'loc': 'NY', 'cost': ny}, {'loc': 'SF', 'cost': sf}]

def getNY(lst):
    return lst[0]

def getSF(lst):
    return lst[1]

def main():
    # arrays first element is for month1, second element is for month2, ...
    costByMonth = [
    createCost(1, 50),
    createCost(3, 20),
    createCost(20, 2),
    createCost(30, 4)
  ]

    print(costByMonth)

  # ny = getNY(costByMonth[0])
  # sf = getSF(costByMonth[1])
  
    currentLocation = ''
    relocationCost = 10
    result = []
    costSum = 0
    for index, cost in enumerate(costByMonth):
        ny = getNY(cost)
        sf = getSF(cost)

        if currentLocation == '':
            if sf.get('cost') < ny.get('cost'):
                currentLocation = 'sf'
            else:
                currentLocation = 'ny'

        if currentLocation == 'ny':
            if sf.get('cost') + relocationCost < ny.get('cost'):
                result.append('sf')
                costSum += (sf.get('cost') + relocationCost)
                currentLocation = 'sf'
            else :
                result.append('ny')
                costSum += (ny.get('cost'))
        elif currentLocation == 'sf':
            if ny.get('cost') + relocationCost < sf.get('cost'):
                result('ny')
                costSum += (ny.get('cost') + relocationCost)
                currentLocation = 'ny'
            else:
                result.append('sf')
                costSum += (sf.get('cost'))
        else:
            print("don't know current location: ", currentLocation)
  
    print(result)
    print(costSum)

main()

def inCorrectAlgorithm(n,N,S):
    for i in range(1,n):
        if N[i] < S[i]:
            print("NY in Month i")
        else:
            print("SF in Month i")

