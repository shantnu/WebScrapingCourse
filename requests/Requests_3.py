
# coding: utf-8

# In[4]:

import requests
from bs4 import BeautifulSoup
import re
import os


# In[5]:

r = requests.get("http://pythonforengineers.com/pythonforengineersbook/")
data = r.text
soup = BeautifulSoup(data)


# ------------------
# 
# **A note for this actually running this code**
# 
# Listen up, folks.
# 
# After I made the video, my website(based on Wordpress) updated, and suddenly the links changed.
# 
# Suddenly, the links no longer had *http:* in front of it. I'm assuming, that Wordpress, in it's infinite wisdom, adds it for us.
# 
# Anyway, so I had to update the code for this change. This is actually good practice for real life, as real websites are updated all the time, and you'll have to update your scripts if you want to keep scraping them.
# 
# ----------------
# 

# In[6]:

for link in soup.find_all('img'):
    
    image = link.get("src")
    
    # This is the new code I added 
    if not image.startswith("http"):
        image = "http:" + image 
    print image
    
    try:
        r2 = requests.get(image)

        basename, filename = os.path.split(image)

        with open(filename, "wb") as out_file:
            out_file.write(r2.content)
    except:
        pass
