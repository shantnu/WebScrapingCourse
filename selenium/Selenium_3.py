
# coding: utf-8

# In[8]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[9]:

driver = webdriver.Firefox()


# In[10]:

driver.get("http://pythonforengineers.com/articles/")


# In[11]:

elem = driver.find_element_by_name("s")


# **Note**: A minor change below: I added more blogs on reddit, and the current blog slipped off the 1st page.
# 
# Now, could have just clicked the second page of the search, but that would have required extensive changes.
# 
# So I'm just changing the search term from *reddit* to *build reddit*.

# In[12]:

elem.send_keys("build reddit")


# In[13]:

elem.send_keys(Keys.RETURN)


# In[14]:

link = driver.find_element_by_link_text("Build a Reddit Bot Part 1")


# In[15]:

link.click()


# In[16]:

driver.close()


# In[16]:



