#!/usr/bin/env python
# coding: utf-8

# In[3]:


regex_pattern = r"[/.,]"

import re
print("\n".join(re.split(regex_pattern, input())))


# In[ ]:




