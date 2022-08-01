#!/usr/bin/env python
# coding: utf-8

# In[220]:


def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string), k):
  
        x = string[i:i+k]
        b = set()
        for j in x:
            if j not in b:
                b.add(j)
                print(j,end='')
        print()

string, k = input(), int(input())
merge_the_tools(string, k)


# In[ ]:




