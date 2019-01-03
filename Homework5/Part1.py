#!/usr/bin/env python
# coding: utf-8

# In[7]:


# t1 = 1, w1 = 10
# t2 = 3, w2 = 2
# t3 = 5, w3 = 3
# First job1: 10.1 + 2.4 = 18
# First job 2: 10.4 + 2.3 = 46
# First job 3 Second =  1 third = 2 --> 5.3 + 6 . 10 + 9 . 2 = 88
# First job 1 Second =  2 third = 3 --> 1.10 + 4 .2 + 9 .3  = 41 

# If weight is higher we want to prioritize them.

# oguzhan baslangic
def sortByWeight(jobsList):
    return sorted(jobsList, key=lambda k: k['w'], reverse=True)

def minimizedSum(jobs):
    timer = 0
    weightedSum = 0
    order = []
    for j in jobs:
        timer += j.get('t')
        weightedSum += j.get('w') * timer
        order.append(j.get('jobIndex'))
    return weightedSum, order

def main():
    print('=== main start ===')
    jobs = [{'t': 1, 'w': 10, 'jobIndex': 0}, {'t': 3, 'w': 2, 'jobIndex': 1}, {'t': 5, 'w': 3, 'jobIndex': 2}]
    maxJobs = sortByWeight(jobs)
    minSum = minimizedSum(maxJobs)
    print(minSum)
    print('=== main end   ===')

main()



def findMinumumCost(jobs):
    cost = 0
    globalTime = 0
    for job in jobs:  
        if job != None:
            cost +=calculateCost(job,globalTime)
            t = job.get('t')
            globalTime+=t
            print("Proccessed Job Id " , str(job.get('jobIndex')))
            print("Job Time " + str(cost))

    print("\n\nMinimized Time is " + str(cost))
    return 0



