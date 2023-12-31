import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk

import threading
import time

from lib.Color import Color
from lib.Webdriver import Webdriver
from lib.OpenPhone import OpenPhone

from components.Status import Status

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent, webdriver: Webdriver):
        super().__init__(master=parent)

        # defining the attributes
        self.webdriver = webdriver  # holdes the webdriver  
        self.action_status = None     # holdes the widget that shows the status of the action
        self.webdriver_status = None  # holdes the widget that shows the status of the webdriver
        self.action = "waiting for action"
        self.openphone = OpenPhone(self.webdriver)

        # frame location configuration
        self.pack(side="left", fill="y", expand=False)

        # create widgets
        self.create_widgets()

        # check the statuses in the background
        threading.Thread(target=self.check_wedriver_status, daemon=True).start()
        threading.Thread(target=self.check_action_status, daemon=True).start()

    def create_widgets(self):
        """
        Creates the widgets of the sidebar.

        :return: None
        """
        # create a Action status widget
        self.action_status = Status(self, "Action", self.action, text_color=Color.GREEN, x=10,  y=10, gap=45)
        self.webdriver_status = Status(self, "Webdriver", "disconnected", text_color=Color.RED, x=10, y=40, gap=70)

        # create a Webdriver widget
        self.webdriver_widget = WebDriverWidget(self, x=10, y=70, connect_function=self.connect_webdriver, disconnect_function=self.disconnect_webdriver)
        
        # create a login button
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login, width=160, fg_color=Color.DARK_BLUE ,hover_color=Color.BLUE)
        self.login_button.place(x=10, y=240)

        # create a logo widget
        self.logo_widget = LogoWidget(self, x=10, y=290)

    def connect_webdriver(self):
        """
        Connects the webdriver.

        :return: None
        """
        # update the status of the action
        self.action = "connecting webdriver"

        try:
            # initialize the webdriver
            self.webdriver.connect()
        except Exception as e:
            self.webdriver_status.error("failed to connect")

    def disconnect_webdriver(self):
        """
        Disconnects the webdriver.

        :return: None
        """
        self.action = "destroying webdriver"
        try:
            # disconnect the webdriver
            self.webdriver.disconnect()
        except Exception as e:
            self.webdriver_status.error("disconnected")

    def login(self):
        """
        Logs in to the openphone.com

        :return: None
        """
        # update the status of the action
        self.action = "logging in"

        # open the openphone.com
        self.openphone.open()

        # login to the openphone.com
        self.openphone.login()

    def check_wedriver_status(self):
        """
        Checks the status of the webdriver.

        :return: None
        """
        # untill the app is running
        while True:
            color = Color.RED

            if self.webdriver.get_status() == "connected":
                color = Color.GREEN
            
            self.webdriver_status.update(text=self.webdriver.get_status(), text_color=color)

            time.sleep(1)

    def check_action_status(self):
        """
        Checks the status of the action.

        :return: None
        """
        # untill the app is running
        while True:
            if self.action != "waiting for action":
                self.action_status.info(text=self.action)
                time.sleep(2)

                # reset the action status
                self.action = "waiting for action"
            else:
                self.action_status.success(text=self.action)            
                time.sleep(1)


class WebDriverWidget(ctk.CTkFrame):
    def __init__(self, parent, x: int, y: int, connect_function: callable = None, disconnect_function: callable = None):
        super().__init__(master=parent, width=160, height=250)

        # frame location configuration
        self.place(x=x, y=y)

        # create widgets
        self.webdriver_label = ctk.CTkLabel(self, text="Webdriver", width=160, height=20)
        self.webdriver_label.pack(side="top", anchor="w", expand=False, pady=8)
        self.connect_button = ctk.CTkButton(self, command=connect_function,text="Connect", width=140, fg_color=Color.DARK_GREEN, hover_color=Color.GREEN)
        self.connect_button.pack(side="top", expand=False, pady=5)
        self.disconnect_button = ctk.CTkButton(self, command=disconnect_function,text="Disconnect",fg_color=Color.DARK_RED, hover_color=Color.RED, width=140)
        self.disconnect_button.pack(side="top", expand=False, pady=15)

class LogoWidget(ctk.CTkFrame):
    def __init__(self, parent, x: int, y: int):
        super().__init__(master=parent, width=160, height=250, fg_color=Color.TRANSPARENT)

        # frame location configuration
        self.place(x=x, y=y)

        # load the logo via pil
        self.logo_image = Image.open("resources/favicon.png")

        # create widgets
        self.logo = ctk.CTkImage(self.logo_image, size=(50,50))
        self.logo_label = ctk.CTkLabel(self, image=self.logo, text="", width=160, height=50)
        self.logo_label.pack(side="top", anchor="w", expand=False, pady=8)
        self.version_label = ctk.CTkLabel(self, text="AutoDialer v0.0.1", width=160, height=20)
        self.version_label.pack(side="top", anchor="w", expand=False, pady=8)