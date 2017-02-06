
# coding: utf-8
# In[5]:
import arcpy, sys, os
from arcpy import env

# In[6]:
env.workspace = './Exercise02/'

# In[7]:
fcs = arcpy.ListFeatureClasses()

# In[10]:
i = 1
for fc in fcs:
    print 'feature {0}: {1}'.format(i, fc)
    i = i + 1

# In[ ]:
input()
