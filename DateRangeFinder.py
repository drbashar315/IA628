#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Assinment: In class date range filer
# SELECT * FROM cddata WHERE Date >= 2019-01-01 and Date <= 2019-01-20

import sys
import os
import json
import time
import datetime
import operator

f2 = open('output.txt', 'w')
f2.write('\n')
f2.close()
f2 = open('output.txt', 'a')

for root, dirs, files in os.walk('data'):
    # print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        print(fp)
        f = open(fp, 'r')
        for line in f:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
            k = payload['received'].split('T')[0]
            if k >= '2019-01-01' and k <= '2019-01-02':
                f2.write(line + '\n')


f2.close()

