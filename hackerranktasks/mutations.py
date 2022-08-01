#!/usr/bin/env python
# coding: utf-8

# In[99]:


def mutate_string(string, position, character):
    a = list(string)
    a[position]=character
    return ''.join(a)


s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)


# In[ ]:




