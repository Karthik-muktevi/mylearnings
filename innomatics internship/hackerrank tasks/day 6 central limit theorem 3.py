#!/usr/bin/env python
# coding: utf-8

# In[100]:


mean = 500
sd = 80
n = 100
z = 1.96

sd_e = sd/n**0.5
print(round(mean-sd_e*z,2))
print(round(mean+sd_e*z,2))


# In[ ]:




