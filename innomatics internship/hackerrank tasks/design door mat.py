#!/usr/bin/env python
# coding: utf-8

# In[229]:


x,y = map(int,input().split())
a = list(range(1,x+1,2))
a = a+a[::-1][1:]
for i in a:
    b='WELCOME' if i==x else '.|.'*i
    print(b.center(y,'-'))

