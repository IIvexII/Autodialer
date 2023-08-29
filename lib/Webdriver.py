from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
# use threading to run the webdriver in the background
import threading

class Webdriver:
    def __init__(self):
        self.driver = None
        self.status = "disconnected"

    def connect(self):
        """
        This function will connect the webdriver

        :return: None
        """
        # initialize the webdriver in the background
        threading.Thread(target=self._init_webdriver, daemon=True).start()

    def disconnect(self):
        """
        This function will disconnect the webdriver

        :return: None
        """
        if self.driver is None:
            return
        try:
            # close the driver
            self.driver.close()
        except:
            pass

        # set the driver to None
        self.driver = None
    
    def _init_webdriver(self):
        """
        This function will initialize the webdriver

        :return: None
        """
        
        # configure the webdriver
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        edge_options.add_argument("headless")
        edge_options.add_argument("disable-gpu")

        try:
            # initialize the webdriver
            self.driver = Edge(executable_path='./webdriver/msedgedriver.exe', options=edge_options)
        except Exception as e:
            self.status = "failed to connect"

    def get_status(self):
        """
        This function will return the status of the webdriver

        :return: status<str>
        """
        if self.status == "failed to connect" and self.driver is None:
            return self.status

        # check if the driver is None
        if self.driver is None:
            self.status = "disconnected"
            return self.status

        # check if the driver is not None
        elif self.driver is not None:
            try:
                self.driver.title

                self.status = "connected"
                return self.status
            except:
                self.status = "disconnected"
                return self.status
