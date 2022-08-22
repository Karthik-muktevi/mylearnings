#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

for i in range(int(input())):
    match = re.findall(r':?.(#[a-fA-f0-9]{6}|#[a-fA-F0-9]{3})',input())
    if match:
        print(*match,sep='\n')


# In[ ]:




