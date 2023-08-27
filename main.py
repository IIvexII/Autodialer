import customtkinter as ctk
import tkinter as tk

from lib.Color import Color
from components.Status import Status

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # configure the app
        self._configuration()

        # create a widget
        sidebar = Sidebar(self)
        
        # run the app
        self.mainloop()

    def _configuration(self) -> None:
        # theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # window configuration
        self.title("AutoDialer")
        self.geometry("600x400")
        self.resizable(False, False)
        self.iconbitmap("resources/favicon.ico")


class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, width=180)

        # defining the attributes
        self.action_status = None
        self.webdriver_status = None

        # frame location configuration
        self.pack(side="left", fill="y", expand=False)

        # create widgets
        self.create_widgets()


    def create_widgets(self):
        """
        Creates the widgets of the sidebar.

        :return: None
        """
        # create a Action status widget
        self.action_status = Status(self, "Action", "wating for cue", text_color=Color.GREEN, x=10,  y=10, gap=45)
        self.webdriver_status = Status(self, "Webdriver", "disconnected", text_color=Color.RED, x=10, y=30, gap=70)

        # Webdriver Connect and Disconnect Buttons
        self.connect_button = ctk.CTkButton(self, text="Connect", width=120)
        self.connect_button.pack(side="top", expand=False, pady=3)
        self.disconnect_button = ctk.CTkButton(self, text="Disconnect",fg_color=Color.RED, width=120)
        self.disconnect_button.pack(side="top", expand=False, pady=3)

if __name__ == "__main__":
    App()
