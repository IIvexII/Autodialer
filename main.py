import customtkinter as ctk
import tkinter as tk

from components.Sidebar import Sidebar

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



if __name__ == "__main__":
    App()
