import customtkinter as ctk
import tkinter as tk

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

        # run the app
        self.mainloop()

if __name__ == "__main__":
    App()
