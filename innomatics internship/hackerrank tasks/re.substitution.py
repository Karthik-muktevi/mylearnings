#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

a = int(input())

for i in range(0,a):
    txt = input()
    txt = re.sub(r"\ \&\&\ "," and ",txt)
    txt = re.sub(r"\ \|\|\ "," or ",txt)
    txt = re.sub(r"\ \&\&\ "," and ",txt)
    txt = re.sub(r"\ \|\|\ "," or ",txt)
   
    print(txt)


# In[ ]:




