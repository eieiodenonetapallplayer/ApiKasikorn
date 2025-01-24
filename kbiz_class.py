import selenium
from selenium import webdriver

class Kbiz:
    def __init__(self):
        super().__init__()
    
    def check(self, username, password, amount):
        try:
            browser = webdriver.Chrome()
            browser.get('https://kbiz.kasikornbank.com/authen/login.jsp?lang=th')
            browser.implicitly_wait(10)
            browser.find_element('xpath', "//input[@name='userName']").send_keys(username)
            browser.implicitly_wait(10)
            browser.find_element('xpath', "//input[@name='password']").send_keys(password)
            browser.implicitly_wait(10)
            browser.find_element('xpath', "//a[@id='loginBtn']").click()
            browser.implicitly_wait(10)
            browser.find_element('xpath', "//a[@class='a-center pointer']").click()
            browser.implicitly_wait(10)
            browser.find_element('xpath', "//a[@class='btn btn-small hv-icon searchBtn btn-dark-blue']").click()
            browser.implicitly_wait(10)
            deposit_element = browser.find_element('xpath',"//div[@class='bottom']//div[@class='list'][3]//p[contains(text(), 'ฝาก (บาท)')]/following-sibling::p/span")
            deposit_amount = deposit_element.text
        except selenium.common.exceptions.NoSuchElementException:
           return '0'
        else:
            if str(amount) in deposit_amount:
                return '1'
            else:
                return '0'

