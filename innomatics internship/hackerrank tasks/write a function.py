#!/usr/bin/env python
# coding: utf-8

# In[7]:


def is_leap(year):
    
    
   
    if year%400==0:  
        return True
    elif year%4==0 and year%100!=0:
        return True
    else:
        return False
        
        
year = int(input())
print(is_leap(year))


# In[ ]:



