#!/usr/bin/env python
# coding: utf-8

# In[10]:


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def combines_Arrays(TwoDimensionalArray):  
    combinedList = []
    for array in TwoDimensionalArray:
        for element in array:
            combinedList.append(element)
    return merge_sort(combinedList)    
        


# In[11]:


#driver Codes
rows = 3
columns = 5
bigArray = [[random.randint(1, 1000) for x in range(columns)] for y in range(rows)]
print(bigArray)
arr =  combines_Arrays(bigArray)
print(arr)

main(bigArray)

