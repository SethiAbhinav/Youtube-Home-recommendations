#IMPORTS
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from getpass4 import getpass
import pandas as pd
import pyautogui
import time

URL = 'https://www.youtube.com/'

email = input("Enter email id you want to login with : ")

change = 'y'
while change == 'y' :
    password = getpass(prompt = "Enter the password : ", char = "*", mnbe = False)  # text to display, password will be displayed in '*', mnbe -> may not be empty

    choice = input("Do you want to see the password entered?(y/n) ")
    if choice =='y' or choice == 'Y':
        print(password)
        change = input("Do you wish to change the password?")
        
        if change == 'y' or change == 'Y':
            change = 'y'
    else:
        break


# Remove usb error and devtools listening error
chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initialize driver
driver = webdriver.Chrome("C:/Users/abhin/Desktop/chromedriver.exe", options = chrome_options)

# Open link
driver.get(URL)

# Wait for chrome to open and load the site
time.sleep(5)

# Locate and click on "SIGN IN"
button = driver.find_element_by_link_text("SIGN IN")
button.click()

# Wait for next page to load
time.sleep(2)

# Enter email id
pyautogui.typewrite(email,interval=0.01)
time.sleep(1)

# Locate and click on 'Next'
next_ = driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span')
next_.click()

# Wait
time.sleep(3)

# Enter password
pyautogui.typewrite(password,interval=0.01)
time.sleep(1)

# Click 'Next'
next_ = driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span')
next_.click()

# Logged in, wait for your account to load
time.sleep(5)
print("Logged in")

# Using beautiful soup to retrieve data
print("Collecting data...")
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')

# Create lists to store data
video_title = []
channel_name = []
channel_link = []
vid_links =[]

name = ''           # channel name
href = ''           # channel link
vid_link = ''       # video link

for a in soup.findAll('yt-formatted-string', attrs={'id':'video-title'}):
    video_title.append(a.text)
print('Retrieved Video Titles')


thumbnails = driver.find_elements_by_xpath('//*[@id="thumbnail"]')
for thumbnail in thumbnails[:-1]:
    vid_link = thumbnail.get_attribute('href')
    vid_links.append(vid_link)
print('Retrieved Video links')


for a in soup.findAll('div', attrs={'id':'meta','class':'style-scope ytd-rich-grid-media'}):
    name = a.find('a',href = True, attrs = {'class':'yt-simple-endpoint style-scope yt-formatted-string'})
    channel_name.append(name.text)
    # print(channel_name)
print('Rtrieved Channel Names')


avatar_links = driver.find_elements_by_id('avatar-link')
for link in avatar_links:
    href = link.get_attribute('href')
    channel_link.append(href)
print('Retrieved Channel links')

print("\nData Procured!")

# make a dataframe
df = pd.DataFrame({'Video name':video_title, 'Video link':vid_links, 'Channel Name':channel_name, 'Channel link':channel_link})

# convert to csv
try:
    df.to_csv('yt_recommendations.csv', index = False, encoding = 'utf-8')
    print("Data updated in 'yt_recommendations.csv'")
except:
    print("Unsuccessful!")



driver.quit()
