# write code for selinium to open google.com
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options


# options = Options()
# print(dir(options))  
# options.capabilities["args"] = ["--disable-user-media-security", "--use-fake-ui-for-media-stream"]
# options.use_chromium = True
# # options.add_argument("headless")
# options.add_argument("disable-gpu")
# # options.add_argument("--disable-user-media-security")
# options.add_argument("use-fake-ui-for-media-stream")


driver = webdriver.Edge("./webdriver/msedgedriver.exe", )
driver.get("https://my.openphone.com/login")

# # find by css selector
email_input = driver.find_element_by_css_selector("input[placeholder='Email address...']")

# type azamkhanfiverr@gmail.com
email_input.send_keys("azamkhanfiverr@gmail.com")

# 2nd button of the page
continue_button = driver.find_elements_by_css_selector("button")[1]

# click
continue_button.click()

# code = driver.find_element_by_css_selector("input[name='code']")
# code.send_keys("123456")
# code.send_keys(Keys.ENTER)

# alert = None

# while alert is None:
#     try:
#         alert = driver.find_element_by_css_selector("div[role='alert']")
#         if alert is not None:
#             print(alert.text)
#             break
#     except:
#         pass

contacts = driver.find_elements_by_css_selector("span[color='textPrimary']")

# check if the text is equal to (432) 803-1049 then click
for contact in contacts:
    if contact.text == "(432) 803-1049":
        contact.click()
        break
    