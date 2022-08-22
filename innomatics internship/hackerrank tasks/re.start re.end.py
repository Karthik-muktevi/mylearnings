#!/usr/bin/env python
# coding: utf-8

# In[6]:


import re
s = input()
k= input()
pattern = re.compile(k)
match = pattern.search(s)
if not match: print('(-1, -1)')
while match:
    print('({}, {})'.format(match.start(), match.end()-1))
    match = pattern.search(s, match.start()+1)


# In[ ]:




