#!/usr/bin/env python
# coding: utf-8

# In[129]:


def print_formatted(number):
    
    l = len(bin(number)[2:])
    for i in range(1, number+1):
        decs = str(i)
        octs = oct(i)[2:]
        hexs = hex(i)[2:].upper()
        bins = bin(i)[2:]
        print(decs.rjust(l),octs.rjust(l),hexs.rjust(l),bins.rjust(l))
        

n = int(input())
print_formatted(n)


# In[ ]:




