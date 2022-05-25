# Created by Ken Yeung

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
import time
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoSuchElementException
import os
import math
from tabulate import tabulate
from datetime import datetime
from selenium.webdriver.common.by import By

os.system('mode con: cols=60 lines=21')

ac_field = '//*[@id="loginForm"]/div/div[1]/div/label/input'
pw_field = '//*[@id="loginForm"]/div/div[2]/div/label/input'
login_btn = '//*[@id="loginForm"]/div/div[3]/button'
phone_verify_field = '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input'
verify_btn = '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[2]/button'
later_save_info = '//*[@id="react-root"]/section/main/div/div/div/div/button'

home_icon = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[6]/span'

open_the_dialog = '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a'
dialog = 'body > div.RnEpo.Yx5HN > div > div > div > div.isgrP > ul > div'
follow_btn = "//button[@class='sqdOP  L3NKy   y3zKF     '][.='追蹤']"

def getDuration(then, now, interval = "default"):

    # Returns a duration as specified by variable interval
    # Functions, except totalDuration, returns [quotient, remainder]

    duration = now - then # For build-in functions
    duration_in_s = duration.total_seconds() 

    def years():
      return divmod(duration_in_s, 31536000) # Seconds in a year=31536000.

    def days(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 86400) # Seconds in a day = 86400

    def hours(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 3600) # Seconds in an hour = 3600

    def minutes(seconds = None):
      return divmod(seconds if seconds != None else duration_in_s, 60) # Seconds in a minute = 60

    def seconds(seconds = None):
      if seconds != None:
        return divmod(seconds, 1)   
      return duration_in_s

    def totalDuration():
        y = years()
        d = days(y[1]) # Use remainder to calculate next variable
        h = hours(d[1])
        m = minutes(h[1])
        s = seconds(m[1])

        return "{} Days {} Hours {} Mins {} Sec".format(int(d[0]), int(h[0]), int(m[0]), int(s[0]))

    return {
        'years': int(years()[0]),
        'days': int(days()[0]),
        'hours': int(hours()[0]),
        'minutes': int(minutes()[0]),
        'seconds': int(seconds()),
        'default': totalDuration()
    }[interval]

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

##################
class remote:
    tab=open("pg.txt", "r").read()
    x, y=tab.split(",")


    def attach_to_session(executor_url, session_id):
        original_execute = WebDriver.execute
        def new_command_execute(self, command, params=None):
            if command == "newSession":
                # Mock the response
                return {'success': 0, 'value': None, 'sessionId': session_id}
            else:
                return original_execute(self, command, params)
        # Patch the function before creating the driver object
        WebDriver.execute = new_command_execute
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
        driver.session_id = session_id
        # Replace the patched function with original function
        WebDriver.execute = original_execute
        return driver

    dr = attach_to_session(x,y)
################################################################################    
def login(ac, pswd):
    driver.find_element(by=By.XPATH, value=ac_field).send_keys(ac)
    driver.find_element(by=By.XPATH, value=pw_field).send_keys(pswd)

    try:
        driver.find_element(by=By.XPATH, value=later_save_info).click()
    except:
        _verify_field = driver.find_element(by=By.XPATH, value=phone_verify_field)
        isVerify = _verify_field.get_attribute('aria-label') == '安全驗證碼'

        if isVerify:
            verify = input('Your verify number: ')
            _verify_field.send_keys(verify)
            driver.find_element(by=By.XPATH, value=verify_btn).click()
            countdown(6)
            driver.find_element(by=By.XPATH, value=later_save_info).click()
#################################################################################
def checkloading(webid):
    try:
        countdown(6)
        driver.find_element(by=By.XPATH, value=webid)
        pass
    except NoSuchElementException:
        driver.refresh()
        print("Refreshing...")
        return(checkloading(webid))
#################################################################################
def open_dialog():
    try:
        driver.find_element(by=By.XPATH, value=open_the_dialog).click()
        pass
    except NoSuchElementException:
        driver.get("https://www.instagram.com/"+ user+ "/")
        checkloading(open_the_dialog)
        return(open_dialog())
#################################################################################
def ask(n):
    if n in ["Y", "y", "Yes", "yes"]:
        return(follow())
    elif n in ["N", "n", "No", "no"]:
        return()
    else:
        print(f"{bcolors.FAIL}Please type the fucking correct option.{bcolors.ENDC}")
        n= input()
        return(ask(n))
#################################################################################
def countdown(t):
    for x in range(t, 0, -1):
        # clear()
        print("Loading..."+str(x))
        time.sleep(1)
#################################################################################
#################################################################################
def count(t):
    global then
    for q in range(t,0,-1):
        headers = ["Followed", "Next"]
        data = [( "    " + str(numfollow)+"/"+str(bal), f"      {bcolors.OKGREEN}"+str(q)+f"{bcolors.ENDC}")]
        clear()
        print(then.strftime("Start in: %d/%m | %X"))
        print(tabulate(data, headers=headers, tablefmt="grid"))
        time.sleep(1)
#################################################################################
numfollow=0
#numlike=0
bal = 0
def follow():
    global numfollow
    #global numlike
    global bal
    #global then

    while True:
        times = 100
        try:
            val = int(times)
            if val < 0:
                continue
            break
        except ValueError:
            clear()
            print(f"{bcolors.FAIL}{bcolors.UNDERLINE}Type a fucking correct answer!!{bcolors.ENDC}")
        
    loop=math.ceil(math.sqrt(val))
    bal = bal+loop*loop

    driver.get("https://www.instagram.com/"+ user+ "/")

    checkloading('//*[@id="react-root"]/section/main/div/header/section/div[1]/h2')

    open_dialog()
    for z in range(10):

        FList = driver.find_element(by=By.CSS_SELECTOR, value=dialog)
        print("Dialog found")
        numberOfFollowersInList = len(FList.find_elements(by=By.XPATH, value=follow_btn))
        print("All Can Follow")
        print(numberOfFollowersInList)

        FList.click()
        actionChain = webdriver.ActionChains(driver)
        time.sleep(random.randint(2,4))

        while (numberOfFollowersInList < loop):
            FList.click()
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            numberOfFollowersInList = len(FList.find_elements(by=By.XPATH, value=follow_btn))
            time.sleep(0.4)
            actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()            
            time.sleep(2)

        for x in range(loop): #loop
            driver.find_element(by=By.XPATH, value=follow_btn).click()
            numfollow=numfollow+1
            now = datetime.now()
            with open("records.txt", "w", encoding="utf-8") as file:
                headers = ["耗時", "追蹤總數"]
                data = [(str(getDuration(then, now)), str(numfollow)+"/"+str(bal))]
                file.write(str(tabulate(data, headers=headers, tablefmt="grid")))
            count(60 * 5)##!!

        count(60 * 3)##!!
    
    print(now.strftime("End in: %d/%m | %X"))
    print("耗時: "+getDuration(then, now))

    n = "Yes" #input(f"{bcolors.WARNING}{bcolors.UNDERLINE}Continue Follow?(Yes/No): {bcolors.ENDC}")
    ask(n)
##################################################################################

if __name__ == "__main__":

    with open("info.txt", "r", encoding="utf-8") as data:
        for x, line in enumerate(data):
            if x == 0:
                ac=line.split("=")[-1]
            if x == 1:
                pswd=line.split("=")[-1]
            if x == 2:
                user=line.split("=")[-1]

    clear = lambda: os.system('cls')
    options = Options()
    options.add_argument("window-size=1150,1000")
    driver=webdriver.Chrome(options=options, executable_path=r'chrome/chromedriver.exe')
    driver.implicitly_wait(9)
    driver.get("https://www.instagram.com/")
    ###(Record)######
    url = driver.command_executor._url 
    session_id = driver.session_id
    with open("pg.txt", "w") as menu:
        menu.write(url+","+session_id)
    print("Session recorded~!")

    try:
        print("Loading...")
        checkloading(ac_field)
        login(ac, pswd)
        print("Logging in...")
    except NoSuchElementException:
        pass

    checkloading(home_icon)
    clear()
    then = datetime.now()
    follow()
    driver = remote.dr
    driver.quit
    exit()
    input()