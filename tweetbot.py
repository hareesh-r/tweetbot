import os
try:
    from selenium import webdriver
except:
    os.system("pip install selenium")
    from selenium import webdriver

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system("pip install webdriver_manager")
    from webdriver_manager.chrome import ChromeDriverManager
    
import random

username = input("Enter your username : \t").strip()
password = input("Enter your password : \t").strip()
tweet = input("Enter your tweet : \t").strip()

"""
Soon the proper namings will be updated
"""
try:
    def dotweet():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        driver.set_window_size(720, 1080)

        driver.get(r'https://twitter.com/compose/tweet')

        
        driver.implicitly_wait(15)

        LoginCredentials = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        
 
        LoginCredentials.send_keys(username)
     
        passWordBox = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        
        passWordBox.send_keys(password)

        loginButton = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
        loginButton[0].click()


        tweetBox = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        
        tweetBox.send_keys(tweet+str(random.randint(1,100000000)))
        
        tweetButton = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div[3]/div/div')
        tweetButton[0].click()
    

        print('Tweet Successful...!!')

        driver.close()

        dotweet()

    dotweet()
    
except:
    print('Tweet Failed')
    exit()
