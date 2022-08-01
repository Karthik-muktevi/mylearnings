#!/usr/bin/env python
# coding: utf-8

# In[96]:


def swap_case(s):
    a=''
    for i in s:
        if i.isupper()==True:
            a+=i.lower()
        elif i.islower()==True:
            a+=i.upper()
        else:
            a+=i
                 
    return a


s = input()
result = swap_case(s)
print(result)


# In[ ]:




