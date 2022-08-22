#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
for i in range(int(input())):
    uid = input()
    uid = ''.join(sorted(uid)) 
    try:
        assert re.search(r'[A-Z]{2}', uid)
        assert re.search(r'\d{3}', uid)
        assert re.search(r'[a-zA-Z0-9]', uid)
        assert not re.search(r'(.)\1', uid)
        len(uid) ==10
    except:
        print('Invalid')
    else:
        print('Valid')


# In[ ]:




