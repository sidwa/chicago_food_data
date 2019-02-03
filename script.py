#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt


def readfile(filename):
	"""
		Reads data from a csv file to create a pandas dataframe

		:param filename: name of file to be imported

		:return: pandas dataframe containing the data of the given file.
	"""
	data = pd.read_csv(filename, delimiter=',', low_memory=False)
	return data


data = readfile("food_dat.csv")
data = data.drop("Location", axis = 1)
data = data.drop("State", axis = 1)
data = data.drop("City", axis = 1)

	


# In[42]:


print(data.shape)
print(data[data["Inspection Type"] == "Complaint"].shape[0])





# In[57]:


d = data[data["Inspection Type"] == "Complaint"].groupby("Facility Type").count().sort_values(["DBA Name"], ascending=False)

# get top ten most complaint prone eating places.
top_comp = d.index.get_level_values("Facility Type")[0:10]
top_comp


# In[71]:


y = []
for eat_type in top_comp:
    print(eat_type)
    app = data[(data["Inspection Type"] == "Complaint") & (data["Facility Type"] == eat_type) & (data["Results"] == "Fail")].count() /     data[(data["Inspection Type"] == "Complaint") & (data["Facility Type"] == eat_type)].count()
    y.append(app["Address"])

#data["Inspection Type"]


# In[86]:


plt.figure(figsize=(15,10))
plt.xticks(range(1,11), top_comp)
plt.ylabel("Inspection fails per Inspection due to complaints")
plt.xlabel("Eatery place type")
plt.plot(range(1,11), y)
plt.savefig("complain_plot.png")


# In[87]:


d = data[data["Inspection Type"] != "Complaint"].groupby("Facility Type").count().sort_values(["DBA Name"], ascending=False)

# get top ten most complaint prone eating places.
top_comp = d.index.get_level_values("Facility Type")[0:10]
top_comp


# In[88]:


y = []
for eat_type in top_comp:
    print(eat_type)
    app = data[(data["Inspection Type"] != "Complaint") & (data["Facility Type"] == eat_type) & (data["Results"] == "Fail")].count() /     data[(data["Inspection Type"] == "Complaint") & (data["Facility Type"] == eat_type)].count()
    y.append(app["Address"])


# In[89]:


plt.figure(figsize=(25,10))
plt.xticks(range(1,11), top_comp)
plt.ylabel("Inspection fails per Inspection due to complaints")
plt.xlabel("Eatery place type")
plt.plot(range(1,11), y)
plt.savefig("non_complaint.png")


# In[ ]:




