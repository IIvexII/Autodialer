import customtkinter as ctk
import tkinter as tk
from lib.Webdriver import Webdriver

from components.Slider import Slider
from components.Action import Action

class Main(ctk.CTkFrame):
    def __init__(self, parent, webdriver: Webdriver, csv_data: list):
        super().__init__(master=parent)
        
        self.pack(side="right", fill="both", expand=True)

        self.slider = Slider(self, csv_data=csv_data)

        self.action = Action(self, webdriver=webdriver, slider=self.slider)
