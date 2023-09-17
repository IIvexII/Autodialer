from lib.Webdriver import Webdriver
from selenium.webdriver.common.keys import Keys

class OpenPhone:
    def __init__(self, webdriver: Webdriver):
        self.webdriver = webdriver

    def open(self):
        """
        This function will open the openphone.com

        :return: None
        """
        # open the website
        self.webdriver.open("https://my.openphone.com/login")

    def login(self):
        """
        This function will login to the openphone.com

        :return: None
        """
        # find by css selector
        email_input = self.webdriver.driver.find_element_by_css_selector("input[placeholder='Email address...']")

        # type azamkhanfiverr@gmail.com
        email_input.send_keys("azamkhanfiverr@gmail.com")

        # 2nd button of the page
        continue_button = self.webdriver.driver.find_elements_by_css_selector("button")[1]

        # click
        continue_button.click()
    def call(self, number: str):
        # make a call
        self.webdriver.driver.find_element_by_css_selector("#inbox-actions > span:nth-child(1) > button").click()
        # add delay for the call to be made
        self.webdriver.driver.implicitly_wait(2)

        # dial the number
        number_input = self.webdriver.driver.find_element_by_css_selector("input[placeholder='Enter a name or phone number...']")
        number_input.send_keys(number)

        # delay
        self.webdriver.driver.implicitly_wait(1)
        number_input.send_keys(Keys.ENTER)

    def end_call(self):
        # end the call
        self.webdriver.driver.find_element_by_css_selector("#main-container > div._13qfu1p0._1mwyz870 > div > div._190kk170 > div > div._190kk171 > div._1f7iyig0 > button:nth-child(4)").click()

    def send_message(self, contact_number: str, msg: str):
        contacts = self.webdriver.driver.find_elements_by_css_selector("span[color='textPrimary']")

        # check if the text is equal to (432) 803-1049 then click
        for contact in contacts:
            if contact.text == contact_number:
                contact.click()
                break
            
        textbox = self.webdriver.driver.find_element_by_css_selector("div[role='textbox']")
        textbox.click()
        textbox.send_keys(msg)
        textbox.send_keys(Keys.ENTER)