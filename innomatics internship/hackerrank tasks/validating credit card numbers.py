#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
a = int(input())
for i in range(a):
    b = input(r'').strip()
    
    if not re.match(r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$',b):
        print('Invalid')
    else:
        if re.search(r'(\d)\1\1\1', re.sub(r'-', '', b)):
            print('Invalid')
        else:
            print('Valid')

