import customtkinter as ctk
from lib.Color import Color

class Status(ctk.CTkFrame):
    """
    A class for creating a status widget.
    """
    def __init__(self, parent: ctk.CTkLabel, title: str, default_text: str, x: str, y: str, gap: int = 0, text_color: str = Color.WHITE):
        """
        Creates a status widget.

        :param parent: ctk.CTkLabel (The parent of the widget)
        :param title: str (The title of the status widget)
        :param default_text: str (The default text of the status widget)
        :param text_color: str (The color of the text)
        :param x: str (The x coordinate of the widget)
        :param y: str (The y coordinate of the widget)
        """
        super().__init__(master=parent, fg_color=Color.TRANSPARENT, height=25)

        self.widget = self._create_status_widget(title=f"{title}:", text=default_text, x=x, y=y, gap=gap, text_color=text_color)

        # frame location configuration
        self.pack(side="top", fill="x", expand=False, pady=1)

    def success(self, text: str):
        """
        Updates the status of the given widget to success.

        :param text: str (The text of the status widget)

        :return: None
        """
        self.update(text=text.lower(), text_color=Color.GREEN)
    
    def error(self, text: str):
        """
        Updates the status of the given widget to error.

        :param text: str (The text of the status widget)

        :return: None
        """
        self.update(text=text.lower(), text_color=Color.RED)

    def warning(self, text: str):
        """
        Updates the status of the given widget to warning.

        :param text: str (The text of the status widget)

        :return: None
        """
        self.update(text=text.lower(), text_color=Color.YELLOW)

    def update(self, text: str, text_color: str = Color.WHITE):
        """
        Updates the status of the given widget.

        :param text: str (The text of the status widget)
        :param text_color: str (The color of the text)

        :return: None
        """
        self.widget.configure(text=f"[{text.lower()}]", text_color=text_color)

    def _create_status_widget(self, title: str, text: str, x: str, y: str, gap: int = 0, text_color: str = Color.WHITE):
        """
        Creates a status widget.

        :param title: str (The title of the status widget)
        :param text: str (The text of the status widget)
        :param text_color: str (The color of the text)
        :param x: str (The x coordinate of the widget)
        :param y: str (The y coordinate of the widget)

        :return: ctk.CTkLabel
        """
        # font configuration
        font = ctk.CTkFont(family="Arial", size=12, weight="bold")
        # create a title label
        title_label = ctk.CTkLabel(master=self, text=title, text_color=Color.WHITE, font=font)
        title_label.place(x=10, y=0)

        # create a status label
        status_label = ctk.CTkLabel(master=self, text=f"[{text.lower()}]", text_color=text_color, font=font)
        status_label.place(x=10 + gap, y=0)

        return status_label
