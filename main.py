import customtkinter as ctk
import tkinter as tk

# import color
from lib.Color import Color

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # theme configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # window configuration
        self.title("AutoDialer")
        self.geometry("600x400")
        self.resizable(False, False)
        self.iconbitmap("resources/favicon.ico")

        # create a widget
        sidebar = Sidebar(self)
        
        # run the app
        self.mainloop()

class Sidebar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, width=180)

        # defining the attributes
        self.action_status = None
        self.action_status_x = 10
        self.action_status_y = 10

        self.webdriver_status = None
        self.webdriver_status_x = 10
        self.webdriver_status_y = 30

        # frame configuration
        self.pack(side="left", fill="y", expand=False)

        # create widgets
        self.create_widgets()


    def create_widgets(self):
        """
        Creates the widgets of the sidebar.

        :return: None
        """
        # create a Action status widget
        self.action_status = self._create_status_widget(
            title="Action",
            text="[wating for cue]",
            font_color=Color.GREEN, 
            x=self.action_status_x, 
            y=self.action_status_y
        )
        # create a Webdriver status widget
        self.webdriver_status = self._create_status_widget(
            title="Webdriver",
            text="[disconnected]", 
            font_color=Color.RED, 
            x=self.webdriver_status_x, 
            y=self.webdriver_status_y
        )
    
    def _create_status_widget(self, title: str,text: str, font_color: str = Color.WHITE, x: int = 0, y: int = 0):
        """
        (Private) Creates a status widget with a title and text.
        
        :param title: str (The title of the status widget)
        :param text: str (The text of the status widget)
        :param font_color: str (The color of the text)
        :param x: int (The x position of the status widget)
        :param y: int (The y position of the status widget)

        :return: ctk.CTkLabel
        """
        font = ctk.CTkFont(family="Arial", size=12, weight="bold")

        title_widget = ctk.CTkLabel(self, text=f"{title}: ", font=font)
        title_widget.place(x=x, y=y)

        status_widget = ctk.CTkLabel(self, text=text, font=font, text_color=font_color)
        status_widget.place(x=len(title) * (x-1), y=y)

        return status_widget
    
    def update_status(self, widget: ctk.CTkLabel, text: str, font_color: str = Color.WHITE):
        """
        Updates the status of the given widget.

        :param text: str (The text of the status widget)
        :param font_color: str (The color of the text)

        :return: None
        """

        widget.configure(text=text, text_color=font_color)

if __name__ == "__main__":
    App()
