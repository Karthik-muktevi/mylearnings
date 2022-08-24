#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.linear_model import LinearRegression

p = list(map(int, input().split()))
m, n = p[0], p[1]

data = [list(float(x) for x in input().split()) for i in range(n)]

x = [[item[i] for i in range(m)] for item in data]
y = [item[-1] for item in data]
lr = LinearRegression()
lr.fit(x, y)
a = lr.intercept_
b = lr.coef_

for i in range(int(input())):
    d = list(map(float, input().split()))
    b_ = [b[j]*d[j] for j in range(m)]
    print(a+sum(b_))

