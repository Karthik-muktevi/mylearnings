#!/usr/bin/env python
# coding: utf-8

# In[222]:


n = int(input())
s = set(map(int, input().split()))
a= int(input())
for i in range(a):
    b= input().split()
    if b[0] =='pop':
        s.pop()
    elif b[0]=='remove':
        s.remove(int(b[1]))
    elif b[0]=='discard':
        s.discard(int(b[1]))
print(sum(s))


# In[ ]:




