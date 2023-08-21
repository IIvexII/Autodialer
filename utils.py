from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# this this function in a way that it will run in the background change the value of the driver

def init_webdriver():
    """
    This function will initialize the webdriver

    :return: driver<webdriver>
    """
    # initialize the webdriver
    driver = webdriver.Edge("./webdriver/msedgedriver.exe")
    # hide the browser
    driver.minimize_window()
    # open the website
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

def call(driver, number: str):
    # make a call
    driver.find_element_by_css_selector("#inbox-actions > span:nth-child(1) > button").click()
    # add delay
    driver.implicitly_wait(2)
    number_input = driver.find_element_by_css_selector("input[placeholder='Enter a name or phone number...']")
    number_input.send_keys(number)
    number_input.send_keys(Keys.ENTER)

    # delay
    driver.implicitly_wait(3)

    try:
        allow_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Allow']"))
        )
        allow_button.click()
    except Exception as e:
        print("Error handling microphone permission:", e)

def end_call(driver):
    driver.find_element_by_css_selector("#main-container > div._13qfu1p0._1mwyz870 > div > div._190kk170 > div > div._190kk171 > div._1f7iyig0 > button:nth-child(4)").click()

def send_message(driver, msg: str):
    textbox = driver.find_element_by_css_selector("div[role='textbox']")
    textbox.click()
    textbox.send_keys("Hey There!")
    textbox.send_keys(Keys.ENTER)
