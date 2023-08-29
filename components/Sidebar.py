import customtkinter as ctk
import tkinter as tk
import threading
import time

from lib.Color import Color
from lib.Webdriver import Webdriver
from components.Status import Status

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, width=180)

        # defining the attributes
        self.webdriver = Webdriver()  # holdes the webdriver  
        self.action_status = None     # holdes the widget that shows the status of the action
        self.webdriver_status = None  # holdes the widget that shows the status of the webdriver

        # frame location configuration
        self.pack(side="left", fill="y", expand=False)

        # create widgets
        self.create_widgets()

        # check the status of the webdriver in the background
        threading.Thread(target=self.check_wedriver_status, daemon=True).start()

    def create_widgets(self):
        """
        Creates the widgets of the sidebar.

        :return: None
        """
        # create a Action status widget
        self.action_status = Status(self, "Action", "wating for action", text_color=Color.GREEN, x=10,  y=10, gap=45)
        self.webdriver_status = Status(self, "Webdriver", "disconnected", text_color=Color.RED, x=10, y=30, gap=70)

        # create a Webdriver widget
        self.webdriver_widget = WebDriverWidget(self, x=10, y=70, connect_function=self.connect_webdriver, disconnect_function=self.disconnect_webdriver)

    def connect_webdriver(self):
        """
        Connects the webdriver.

        :return: None
        """
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
        try:
            # disconnect the webdriver
            self.webdriver.disconnect()
        except Exception as e:
            print(e)
            self.webdriver_status.error("disconnected")

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