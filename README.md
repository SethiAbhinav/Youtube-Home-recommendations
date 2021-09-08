# Youtube-Home-recommendations
**A bot logs into my Youtube account and scrapes my recommendations. A web scraping project I had done on 12th July, 2021.**

# Requirements:
[Chromedriver](https://chromedriver.chromium.org/)

**Python:**
```python
#IMPORTS
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from getpass4 import getpass
import pandas as pd
import pyautogui
import time
```

# Project details:

**Idea:**

I wanted to scrape my recommendations for a future project wherein I would check how my recommendations have changed over time (maybe the demographic I watch has changed or the overall categories I watch have changed, and thought that would be a fun analysis to do).


**Process:** 
- I started by taking the input of the user's email id and password (in the normal form seen when you login to any website). (Used the `getpass4` library)
- Next, I opened a new browser using `selenium` and `chromedriver` and sent a get request to youtube.
- Once youtube loaded, I coded the bot to sign up with the input taken earlier using `pyautogui` (had to add delay using `time`).
- Once the bot has logged in, using `BeautifulSoup` it scrapes through the home page, looking for particular html tags which give it these data:
  
  
  1)Video name 
  
  
  2)Video link


  3)Channel Name
  
  
  4)Channel link
- Now, all of this data is stored in a `pandas` dataframe.
- Finally, this dataframe is converted to a csv file and stored on the system. 


**After project thoughts:**
- The data can be scraped and stored on different dates using the dates as the name of each file.
- The data procured, in itself, could be helpful as it can help me find a video let's say of which I forgot the title, but remember a word or two or say I want to know which channel I watched it on, a quick search in the excel file would give me the result. 
