#!/usr/bin/env python
# coding: utf-8

# In[133]:


def minion_game(string):
    
    v = 'AEIOU'
    p1 = 0
    p2 = 0
    for i,c in enumerate(string):
        if c in v:
            p2+=len(string) -i
        else:
            p1 +=len(string)-i

    if p1==p2:
        print('Draw')
    elif p1>p2:
        print('Stuart', p1)
    else:
        print('Kevin', p2)
    



s = input()
minion_game(s)


# In[ ]:




