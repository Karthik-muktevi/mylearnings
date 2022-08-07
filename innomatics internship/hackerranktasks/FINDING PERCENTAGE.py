#!/usr/bin/env python
# coding: utf-8

# In[142]:


n  =int(input())
marks ={}
for j in range(n):
    a,*b = input().split()
    b = list(map(float,b))
    marks[a] = b
        
query_name = input()
        
for i in marks:
    if query_name ==i:
        print(format(sum(marks[query_name])/3,'.2f'))

