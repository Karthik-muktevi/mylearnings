#!/usr/bin/env python
# coding: utf-8

# In[5]:


import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
match = re.findall(r'(?<=[' + c + '])([' + v + ']{2,})(?=[' + c + '])', input(), flags=re.I)
print('\n'.join(match or ['-1']))


# In[ ]:




