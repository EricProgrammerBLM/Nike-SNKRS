from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import datetime, time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

#                                                  THEIR ARE 5 STEPS. FOLLOW THEM

Stop = 0 #STEP 1  -   MAKE THIS THE NUMBER ZERO 0

print ('You should have a NikeSNKRS Account already set up with your card information saved on their website...')
print ('Below you will be asked personal information specifically for the checkout page on NikeSNKRS website.')
email = input('Enter your Login Email for NikeSNKRS: ')
print (email)
password = input('Enter your Login Password for NikeSNKRS: ')
print (password)
TheCVV = input('Enter your CVV for the Card saved on your NikeSNKRS account: ')
print (TheCVV)
print ('Go Here: https://www.nike.com/launch?s=upcoming')
print ('Click on the upcoming shoe/sneaker you wish to purchase, copy the link and post it below.')
DaLink = input('Whats the link of the upcoming sneaker you wish to buy? Paste it Here: ')
print (DaLink)
print ('')
print ('This bot has a Schedule feature. Below you will be asked at which hour, minute and second of the day you would like the bot to start. This bot uses military time, 6:00PM = 18:00:00, and 10:00AM = 10:00:00. Be as specific as you want.')
Hour = int(input('Which hour of the day would you like this bot to start: '))
print (Hour)
Min = int(input('Which minute of the hour would you like this bot to start: '))
print (Min)
Sec = int(input('Which second of the minute would you like this bot to start: '))
print (Sec)

AddProxy = input('Do you have a Proxy: ')
if AddProxy == 'yes' or AddProxy == 'Yes':
    print ('Your proxy should look like this: 109.98.36.23:38474 - Basically enter the IP:PORT or HOST:PORT')
    PROXY = input('Enter your Proxy Here: ') # IP:PORT or HOST:PORT
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
else:
    print ('Continuing without Proxy...')
    driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.nike.com/launch/')

print ('Remember to Move the Mouse Around when this bot activates.') #STEP 3

#-------------------------Time-------------------------
def Schedule(hour1, min2, sec3):
    hour1 = int(hour1)
    min2 = int(min2)
    sec3 = int(sec3)
    today = datetime.datetime.now()
    Activate = (datetime.datetime(today.year, today.month, today.day, hour1, min2, sec3) - today).seconds     #STEP 3 CHOOSE THE TIME YOU WANT IT TO CONTINUE AT AFTER LAUNCHING THE BROWSER
#Uses Military Time 23, 25, 0 = 11:25:00PM                                                       #STEP 4 MAKE SURE YOUR NIKE CART IS COMPLETELY EMPTY
    print('Waiting for ' + str(datetime.timedelta(seconds=Activate)))
    time.sleep(Activate)
#Rest of the code will activate at the correct time that you set it

#Schedule() #Uncomment this

StartUp = input('Would you like this bot to start at the scheduled time? ')
if StartUp == 'yes' or StartUp == 'Yes':
    Schedule(Hour, Min, Sec)
else:
    print ('Scheduled timing not needed...continuing without')
    StartBot = input('Press the Enter Key when you are ready to run the bot.')


#Time will be placed here
#------------------------------------SNEAKER LINK GOES BELOW---------------------
driver.implicitly_wait(900)
driver.get(DaLink)   #THIS WAS CORRECT
#STEP 6    -     #GET THE LINK

#Get this link from the Nike SNKRS Website, under upcoming.
#Find the sneaker you plan to buy on release day and click on it.
#Copt that link and post it here


LowestSize = "//li[@data-qa='size-available']"
driver.find_element_by_xpath(LowestSize).click()
print ('Clicked on Sneaker Size. Move the mouse around so it DOESNT get stuck')
#Will choose the first size avaliable
#May need to add some code to make the picking process more specific


Buy = "//button[@data-qa='feed-buy-cta']"
wait = WebDriverWait(driver,3)
wait.until(EC.presence_of_element_located((By.XPATH, Buy)))

sleep(1) #Only have this here so it doesn't pick more than one size
#Can delete this to speed things up but it may grab a bigger size
driver.find_element_by_xpath(Buy).click()
#driver.find_element_by_xpath(Buy).click()
#driver.find_element_by_xpath(Buy).click()
#Will choose to add to the cart
print ('Clicked on Buy Button')

LoginPopUp = "//input[@placeholder='Email address']" #Need this xpath
wait = WebDriverWait(driver,900)
wait.until(EC.presence_of_element_located((By.XPATH, LoginPopUp)))

driver.find_element_by_name('emailAddress').send_keys(email)
driver.find_element_by_name('password').send_keys(password)
LoginButton = "//input[@value='LOG IN']"
driver.find_element_by_xpath(LoginButton).click()
print ('Logged In')

SaveNContinue = "//button[@data-qa='save-button']" #Need this xpath
wait = WebDriverWait(driver,500)
wait.until(EC.presence_of_element_located((By.XPATH, SaveNContinue)))

frame = driver.find_element_by_xpath("//iframe[@title='creditCardIframeForm']")
driver.switch_to_frame(frame)
#Switches inside the frame

CVV = "//input[@data-shortname='cvv']"
driver.find_element_by_xpath(CVV).send_keys(TheCVV)
print ('Entered CVV')

#driver.switch_to.default_content()
print ('Switches out the frame')

sleep(Stop)

SaveNContinue = "//button[@data-qa='save-button']"
driver.find_element_by_xpath(SaveNContinue).click() #May have to manually click Save & Continue Button
print ('Entered CVV and Checked Out')








