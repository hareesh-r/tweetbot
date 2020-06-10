from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager

import random

go=input()
baba='your password here'
"""
Soon the proper namings will be updated
"""
try:
    def dotweet():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        
        driver.set_window_size(720, 1080)

        driver.get(r'https://twitter.com/compose/tweet')

        
        driver.implicitly_wait(15)

        passWordBox = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        
 
        passWordBox.send_keys('Your user name here')
     
        passWordBox1 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        
        passWordBox1.send_keys(baba)

        nextButton = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/form/div/div[3]/div/div')
        nextButton[0].click()

        passWordBox1 = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[3]/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        
        passWordBox1.send_keys(r'#CancelAUExamsTN #cancelfinalyearexams #canceljntuexams #CancelTNExamsPromoteStudents #cancelexams #Annauniversityexamcancel #examscancelkaro #'+str(random.randint(1,100000000)))
        
        nextButton = driver.find_elements_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div[3]/div/div')
        nextButton[0].click()
    

        print('Tweet Successful...!!')

        driver.close()

        dotweet()
    dotweet()
except:
    print('Tweet Failed')
    exit()
