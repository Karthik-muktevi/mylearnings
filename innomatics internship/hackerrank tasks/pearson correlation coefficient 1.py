#!/usr/bin/env python
# coding: utf-8

# In[106]:


n = int(input())
x = list(map(float,input().split()))
y = list(map(float,input().split()))

mean_x=sum(x)/n
mean_y=sum(y)/n
    
sd_x= (sum([(i-mean_x)**2 for i in x])/n)**0.5 
sd_y= (sum([(i-mean_y)**2 for i in y])/n)**0.5
cov = sum([(x[i]-mean_x)*(y[i]-mean_y) for i in range(n)])      
corr = cov/(n*sd_x*sd_y)
print(round(corr,3))

