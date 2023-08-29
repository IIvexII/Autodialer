import customtkinter as ctk
import tkinter as tk

from components.Sidebar import Sidebar
from lib.Webdriver import Webdriver
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure the app
        self._configuration()

        # initialize the webdriver
        self.webdriver = Webdriver()

        # create a widget
        sidebar = Sidebar(self, self.webdriver)

        # run the app
        self.mainloop()

    def _configuration(self) -> None:
        # theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # window configuration
        self.title("AutoDialer")
        self.geometry("800x400")
        self.resizable(False, False)
        self.iconbitmap("resources/favicon.ico")



if __name__ == "__main__":
    App()
