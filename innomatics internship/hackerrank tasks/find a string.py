#!/usr/bin/env python
# coding: utf-8

# In[63]:


def count_substring(string, sub_string):
    c=0
    n1=0
    n2=len(sub_string)
    for i in range(len(string)):
        if sub_string in string[n1:n2]:
            c+=1
        n1+=1
        n2+=1
    return c
string = input().strip()
sub_string = input().strip()

count = count_substring(string, sub_string)
print(count)


# In[ ]:




