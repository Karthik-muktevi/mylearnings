#!/usr/bin/env python
# coding: utf-8

# In[63]:


a = [[input(),float(input())] for i in range(int(input()))]
b = sorted(set((j for i,j in a)))[1]
print('\n'.join(sorted(i for i,j in a if j==b)))


# In[ ]:




