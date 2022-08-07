#!/usr/bin/env python
# coding: utf-8

# In[200]:


a,b = list(map(int,input().split()))
c= list(map(int,input().split()))
d =  set(map(int,input().split()))
e = set(map(int,input().split()))
happiness = 0
for i in c:
    if i in d:
        happiness+=1
    elif i in e:
        happiness-=1
    else:
        happiness = happiness
print(happiness)


# In[ ]:




