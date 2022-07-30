#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
b =set(map(int,input().split()))
n = int(input())
for i in range(n):
    d =input().split()
    f =set(map(int,input().split()))
    if d[0] == 'intersection_update':
        b.intersection_update(f)
    elif d[0] == 'update':
        b.update(f)
    elif d[0] == 'symmetric_difference_update':
        b.symmetric_difference_update(f)
    elif d[0] == 'difference_update':
        b.difference_update(f)
    
print(sum(b))


# In[ ]:




