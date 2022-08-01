#!/usr/bin/env python
# coding: utf-8

# In[244]:


def print_rangoli(size):
    
    import string
    d = string.ascii_lowercase
    
    a = [d[i] for i in range(n)]
    b = list(range(n))
    b = b[:-1]+b[::-1]
    for i in b:
        c = a[-(i+1):]
        d = c[::-1]+c[1:]
        print("-".join(d).center(n*4-3, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


# In[ ]:




