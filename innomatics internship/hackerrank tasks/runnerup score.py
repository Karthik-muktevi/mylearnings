#!/usr/bin/env python
# coding: utf-8

# In[49]:


n = int(input())
arr = list(map(int, input().split()))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
l1=[]
for x in arr:
    if x not in l1:
        l1.append(x)
print(l1[1])    


# In[ ]:




