import customtkinter as ctk
import tkinter as tk
import os

from lib.Color import Color

class Slider(ctk.CTkFrame):
    def __init__(self, parent, csv_data: list):
        super().__init__(master=parent)

        self.data = csv_data

        # get last accessed index
        if not os.path.exists("data/last_accessed_index.txt"):
            self.index = 0
        else:
            with open("data/last_accessed_index.txt", "r") as file:
                data = file.read()
                # check if the file is empty
                if data == "":
                    self.index = 0
                else:
                    if int(data) > len(self.data) - 1:
                        self.index = 0
                    elif int(data) < 0:
                        self.index = 0
                    else:
                        self.index = int(data)
        
        # update the index in file
        with open("data/last_accessed_index.txt", "w") as file:
            file.write(str(self.index))

        # frame location configuration
        self.pack(side="top", fill="x", expand=False)

        # create slider widget
        self._create()

    def _create(self):
        # font configuration
        font_bold = ("Arial", 15, "bold")
        font = ("Arial", 15)

        ctk.CTkLabel(self, text="MX Number:", font=font_bold).place(x=40, y=10)
        self.mx_widget = ctk.CTkLabel(self, text=self.data[self.index][1], font=font)
        self.mx_widget.place(x=150, y=10)

        ctk.CTkLabel(self, text="Name:", font=font_bold).place(x=40, y=40)
        self.name_widget = ctk.CTkLabel(self, text=self.data[self.index][2], font=font)
        self.name_widget.place(x=100, y=40)

        ctk.CTkLabel(self, text="Phone Number:", font=font_bold).place(x=300, y=10)
        self.number_widget = ctk.CTkLabel(self, text=self.data[self.index][3], font=font)
        self.number_widget.place(x=430, y=10)

        ctk.CTkLabel(self, text="Operation Classification:", font=font_bold).place(x=40, y=70)
        self.opc_widget = ctk.CTkLabel(self, text=self.data[self.index][4], font=font)
        self.opc_widget.place(x=220, y=70)

        ctk.CTkLabel(self, text="Carrier Operation:", font=font_bold).place(x=40, y=100)
        self.co_widget = ctk.CTkLabel(self, text=self.data[self.index][5], font=font)
        self.co_widget.place(x=180, y=100)

        self.back_button_widget = ctk.CTkButton(self, text="<", fg_color=Color.BLUE, width=8,cursor="hand2")
        self.back_button_widget.place(x=250, y=140)
        self.back_button_widget.configure(command=self._back_button)

        self.next_button_widget = ctk.CTkButton(self, text=">", fg_color=Color.BLUE, width=8, cursor="hand2")
        self.next_button_widget.place(x=280, y=140)
        self.next_button_widget.configure(command=self._next_button)
    
    def _next_button(self):
        if self.index < len(self.data) - 1:
            self.index += 1
        self._update()
    
    def _back_button(self):
        if self.index > 0:
            self.index -= 1
        self._update()

    def _update(self):
        self.mx_widget.configure(text=self.data[self.index][1])
        self.name_widget.configure(text=self.data[self.index][2])
        self.number_widget.configure(text=self.data[self.index][3])
        self.opc_widget.configure(text=self.data[self.index][4])
        self.co_widget.configure(text=self.data[self.index][5])

        if self.index == 0:
            self.back_button_widget.configure(state=tk.DISABLED)
        else:
            self.back_button_widget.configure(state=tk.NORMAL)

        if self.index == len(self.data) - 1:
            self.next_button_widget.configure(state=tk.DISABLED)
        else:
            self.next_button_widget.configure(state=tk.NORMAL)

        # write to file
        with open("data/last_accessed_index.txt", "w") as file:
            file.write(str(self.index))

    def get_number(self) -> str:
        return self.data[self.index][3]