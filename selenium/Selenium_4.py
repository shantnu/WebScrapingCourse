
# coding: utf-8

# In[1]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# In[2]:

def get_code(driver):
    '''
    Function to get the code from pre blocks, and write to a file
    '''
    
    code = ""
    
    for code_block in driver.find_elements_by_tag_name("pre"):
        code += code_block.text
    
    with open("code.txt", "a") as f:
        f.write(code)
    


# In[3]:

driver = webdriver.Firefox()


# In[4]:

driver.get("http://pythonforengineers.com/articles/")


# In[5]:

elem = driver.find_element_by_name("s")


# **Note**: A minor change below: I added more blogs on reddit, and the current blog slipped off the 1st page.
# 
# Now, could have just clicked the second page of the search, but that would have required extensive changes.
# 
# So I'm just changing the search term from *reddit* to *build reddit*.
# 

# In[6]:

elem.send_keys("build reddit")


# In[7]:

elem.send_keys(Keys.RETURN)


# In[8]:

link = driver.find_element_by_link_text("Build a Reddit Bot Part 1")


# In[9]:

link.click()


# In[10]:

get_code(driver)


# In[11]:

while True:
    try:
        link = driver.find_element_by_link_text("Next Part")
        link.click()
        get_code(driver)
    except:
        break


# In[12]:

driver.close()


# In[12]:



