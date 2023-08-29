from lib.Webdriver import Webdriver


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