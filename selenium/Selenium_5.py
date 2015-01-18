
# coding: utf-8

# In[21]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# The file below must exist. If not, comment it out and add password manually.
# Look at config_skel.py on how to add password
from config_bot import *


# In[22]:

driver = webdriver.Firefox()
driver.get("http://www.reddit.com/r/Python/")


# In[23]:

elem = driver.find_element_by_name("user")
elem.send_keys(REDDIT_USERNAME)


# In[24]:

elem = driver.find_element_by_name("passwd")
elem.send_keys(REDDIT_PASS)


# In[25]:

button = driver.find_element_by_name("rem")
button.click()


# In[26]:

button = driver.find_element_by_xpath("//*[(contains(text(), 'login'))]")
button.click()


# In[27]:

driver.close()


# In[ ]:



