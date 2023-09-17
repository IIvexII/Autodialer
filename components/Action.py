import customtkinter as ctk
import tkinter as tk

from lib.Color import Color
from lib.Webdriver import Webdriver
from components.Slider import Slider
from lib.OpenPhone import OpenPhone

class Action(ctk.CTkFrame):
    def __init__(self, parent, webdriver: Webdriver, slider: Slider):
        super().__init__(master=parent)
        
        self.openphone = OpenPhone(webdriver=webdriver)
        self.slider = slider

        # pack the frame
        self.pack(side="left", fill="both", expand=True)

        # create widgets
        ctk.CTkButton(self, text="Call", command=self._call, fg_color=Color.DARK_GREEN, hover_color=Color.GREEN).place(x=40, y=10)
        ctk.CTkButton(self, text="End Call", command=self._end_call, fg_color=Color.DARK_RED, hover_color=Color.RED).place(x=40, y=50)

        # message box to send message 
        self.message_box = ctk.CTkTextbox(self, width=420, height=160)
        self.message_box.place(x=220, y=0)

        # send message button
        ctk.CTkButton(self, text="Send", command=self._send_message, fg_color=Color.DARK_BLUE, hover_color=Color.BLUE).place(x=40, y=130)
    
    def _call(self):
        # get the number
        number = self.slider.get_number()
        # call the number
        self.openphone.call(number=number)
    
    def _end_call(self):
        self.openphone.end_call()

    def _send_message(self):
        # get the number
        number = self.slider.get_number()
        # get the message
        message = self.message_box.get("0.0", tk.END)
        # send the message
        self.openphone.send_message(contact_number=number, msg=message)