#!/usr/bin/env python
# coding: utf-8

# In[194]:


def average(array):
    # your code goes here
    arr1 = set(arr)
    return sum(arr1)/len(arr1)
    


n = int(input())
arr = map(int,input().split())
result = average(arr)
print(result)


# In[ ]:




