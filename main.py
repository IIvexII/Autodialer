import customtkinter as ctk
import tkinter as tk

from components.Sidebar import Sidebar
from components.Main import Main
from lib.Webdriver import Webdriver

import csv

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure the app
        self._configuration()

        # initialize the webdriver
        self.webdriver = Webdriver()

        # create a widget
        sidebar = Sidebar(self, self.webdriver)

        # read csv file
        with open("data/data.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            # skip the header
            next(csv_reader)
            csv_data = [row for row in csv_reader]

        # add main 
        main = Main(self, self.webdriver, csv_data=csv_data)

        # run the app
        self.mainloop()

    def _configuration(self) -> None:
        # theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # window configuration
        self.title("AutoDialer")
        self.geometry("900x400")
        self.resizable(False, False)
        self.iconbitmap("resources/favicon.ico")



if __name__ == "__main__":
    App()
