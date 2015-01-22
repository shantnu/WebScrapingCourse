
# coding: utf-8

# In[4]:

import requests
from bs4 import BeautifulSoup


# In[5]:

r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")
data = r.text
soup = BeautifulSoup(data)


# In[ ]:

print r.text


# Print just the paragraph elements of the page:

# In[10]:

print soup('p')


# Print the image elements of the page:

# In[8]:

print soup('img')


# In[9]:

for link in soup.find_all('a'):
    print link


# In[7]:

for link in soup.find_all('a'):
    print link.get('href')


# In[7]:



