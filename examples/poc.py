# write code for selinium to open google.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def init_webdriver():
    """
    This function will initialize the webdriver

    :return: driver<webdriver>
    """
    driver = webdriver.Edge("./webdriver/msedgedriver.exe")
    driver.get("https://my.openphone.com/login")

    return driver


def login(driver: webdriver):
    """
    This function will login to the openphone.com

    :return: None
    """
    # find by css selector
    email_input = driver.find_element_by_css_selector("input[placeholder='Email address...']")

    # type azamkhanfiverr@gmail.com
    email_input.send_keys("azamkhanfiverr@gmail.com")

    # 2nd button of the page
    continue_button = driver.find_elements_by_css_selector("button")[1]

    # click
    continue_button.click()

def call(number: str):
    # make a call
    driver.find_element_by_css_selector("#inbox-actions > span:nth-child(1) > button").click()
    # add delay
    driver.implicitly_wait(2)
    number_input = driver.find_element_by_css_selector("input[placeholder='Enter a name or phone number...']")
    number_input.send_keys(number)
    number_input.send_keys(Keys.ENTER)

def end_call():
    driver.find_element_by_css_selector("#main-container > div._13qfu1p0._1mwyz870 > div > div._190kk170 > div > div._190kk171 > div._1f7iyig0 > button:nth-child(4)").click()

def send_message(msg: str):
    textbox = driver.find_element_by_css_selector("div[role='textbox']")
    textbox.click()
    textbox.send_keys("Hey There!")
    textbox.send_keys(Keys.ENTER)
    
if __name__ == '__main__':
    driver = init_webdriver()
    driver.implicitly_wait(5)

    login(driver)

    # add a delay of 20 seconds
    driver.implicitly_wait(20)

    number = "(660) 562-0735"
    call(number)
    driver.implicitly_wait(3)
    end_call()
