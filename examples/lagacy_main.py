import time
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from selenium.webdriver.common.keys import Keys
import pandas as pd

import sys
sys.path.insert(0, "./lib")
from utils import init_webdriver, login, call, end_call, send_message

driver = None
otp_verified = False
large_logo = None
descriptionLable = None
titleLabel = None
otp_input = None
error_message = None
verify_button = None
otpLabel = None
logo_label = None
i = 0

def connect(status_lable: ttk.Label):
    global driver

    status_lable.config(text="Connecting...", foreground="orange")

    # run init_webdriver in a separate thread
    def init_webdriver_thread():
        global driver
        driver = init_webdriver()
        login(driver)
        otp_verified = False

        update_col2()

    threading.Thread(target=init_webdriver_thread).start()

def disconnect():
    global driver
    if driver is not None:
        print(driver)
        driver.quit()
        driver = None
    
def disable_or_enable_disconnect_button(disconnect_button: ttk.Button):
    global driver

    while True:
        # delay for 1 second
        time.sleep(1)
        if driver is None:
            disconnect_button.config(state="disabled")
        else:
            disconnect_button.config(state="normal")


def check_driver(status_lable: ttk.Label):
    global driver

    while True:
        # delay for 1 second
        time.sleep(1)

        if driver is not None:
            try:
                driver.title
                status_lable.config(text="Connected!", foreground="green")

            except Exception as e:
                status_lable.config(text="Disconnected!", foreground="red")
                driver.quit()
                driver = None
        else:
            if status_lable.cget("text") != "Connecting...":
                status_lable.config(text="Disconnected!", foreground="red")

def otp_code_verify(otp_code: str):
    # type of code
    global driver
    code = driver.find_element_by_css_selector("input[name='code']")
    code.send_keys(otp_code)
    code.send_keys(Keys.ENTER)

    threading.Thread(target=otp_code_verification_thread).start()

def otp_code_verification_thread():
    global driver
    global otp_verified

    # delay 1s

    while True:
        time.sleep(2)

        try:
            _ = driver.find_element_by_css_selector("input[name='code']")
            if _ is None:
                otp_verified = True
                update_col2()
                print("OTP Verified!")
                break
            else:
                otp_verified = False
                update_col2()
                print("OTP Not Verified!")
        except:
            otp_verified = True
            update_col2()
            print("OTP Verified!")
            break

if __name__ == "__main__":
    windows = tk.Tk()
    windows.title("AutoDialer")
    windows.geometry("600x400")
    windows.resizable(False, False)
    windows.iconphoto(True, tk.PhotoImage(file="resources/favicon.png"))

    # split the window into two parts left and right usign grid with 1 and 2 weight
    windows.grid_columnconfigure(0, weight=3)
    windows.grid_columnconfigure(1, weight=1)
    windows.grid_columnconfigure(2, weight=3)

    # verticle line between 2 columns using frame
    verticle_line = ttk.Frame(windows, width=2, height=400, relief="sunken")
    verticle_line.grid(row=0, column=0, sticky="ns")


    # Add Status 
    ttk.Label(windows, text="Status:").place(x=4, y=10)
    status_lable = ttk.Label(windows, text="Disconnected", foreground="red")
    status_lable.place(x=42, y=10)

    # add button "connect now"
    connect_button = ttk.Button(windows, text="Connect Now", width=15, cursor="hand2")
    connect_button.place(x=5, y=70)
    connect_button.config(command=lambda: connect(status_lable))

    # add button "disconnect"
    disconnect_button = ttk.Button(windows, text="Disconnect", width=15, cursor="hand2")
    disconnect_button.place(x=5, y=120)
    disconnect_button.config(command=lambda: disconnect())

    threading.Thread(target=disable_or_enable_disconnect_button, args=[disconnect_button]).start()

    # add icon favicon.png and the version number
    ttk.Label(windows, text="AutoDialer v0.0.1").place(x=5, y=380)

    # add image logo.png
    logo = tk.PhotoImage(file="resources/favicon.png")
    small_logo_label = ttk.Label(windows, image=logo)
    small_logo_label.place(x=25, y=320)

    # run in the background
    threading.Thread(target=check_driver, args=[status_lable]).start()
    if (driver is not None) and (otp_verified is False):
        threading.Thread(target=otp_code_verification_thread).start()

    def update_col2():
        global driver
        global otp_verified
        global large_logo
        global titleLabel
        global otp_input
        global error_message
        global verify_button
        global otpLabel
        global logo_label

        if driver is None:
            # reset the components
            if logo_label is not None:
                logo_label.destroy()
            if titleLabel is not None:
                titleLabel.destroy()
            if otp_input is not None:
                otp_input.destroy()
            if error_message is not None:
                error_message.destroy()
            if verify_button is not None:
                verify_button.destroy()
            if otpLabel is not None:
                otpLabel.destroy()
            
            # add title in the middle of the window
            TitleStyle = ttk.Style ()
            TitleStyle.configure("Title.TLabel", font = ('','36','normal'))
            titleLabel = ttk.Label(windows, text="AutoDialer", style='Title.TLabel')
            titleLabel.place(x=240, y=50)

            # add large icon in the middle
            large_logo = tk.PhotoImage(file="resources/dialer.png")
            large_logo = large_logo.subsample(3, 3)
            logo_label = ttk.Label(windows, image=large_logo)
            # change dimensions
            logo_label.place(x=250, y=150)

        elif not otp_verified:
            # reset the components
            if logo_label is not None:
                logo_label.destroy()
                logo_label = None
            if titleLabel is not None:
                titleLabel.destroy()
                titleLabel = None
            if otp_input is not None:
                otp_input.destroy()
                otp_input = None
            if error_message is not None:
                error_message.destroy()
                error_message = None
            if verify_button is not None:
                verify_button.destroy()
                verify_button = None
            if otpLabel is not None:
                otpLabel.destroy()
                otpLabel = None
            # add input field for number
            TitleStyle = ttk.Style ()
            TitleStyle.configure("Title.TLabel", font = ('','16','bold'))
            otpLabel = ttk.Label(windows, text="OTP Verification", style='Title.TLabel')
            otpLabel.place(x=240, y=50)

            otp_input = ttk.Entry(windows,font=('','16','normal') ,width=15)
            otp_input.place(x=240, y=100)
            def validate_input(P):
                if P.isdigit() and len(P) <= 6:
                    return True
                else:
                    return False
            validation = windows.register(validate_input)

            otp_input.config(validate="key", validatecommand=(validation, "%P"))

            # add error message at the bottom of the window like a toster
            error_message = ttk.Label(windows, text="", foreground="red")
            error_message.place(x=240, y=130)
            # add button "verify"
            verify_button = ttk.Button(windows, text="✅ Verify", width=15, cursor="hand2")
            verify_button.place(x=280, y=150)
            verify_button.config(command=lambda: otp_code_verify(otp_input.get()))

        else:
            # reset the components
            if logo_label is not None:
                logo_label.destroy()
            if titleLabel is not None:
                titleLabel.destroy()
            if otp_input is not None:
                otp_input.destroy()
            if error_message is not None:
                error_message.destroy()
            if verify_button is not None:
                verify_button.destroy()
            if otpLabel is not None:
                otpLabel.destroy()
            # add input field for number
            data = pd.read_csv("./data.csv")
            rows = len(data)

            # add label for title and values of the following fields
            # MX Number, Name, Phone Number, Operation Classification, Carrier Operation
            boldStyle = ttk.Style ()
            boldStyle.configure("Bold.TLabel", font = ('','9','bold'))

            def update_label_data(i):
                ttk.Label(windows, text="MX Number:", style="Bold.TLabel").place(x=150, y=10)
                ttk.Label(windows, text=data["mx_number"][i]).place(x=230, y=10)

                ttk.Label(windows, text="Phone Number:", style="Bold.TLabel").place(x=330, y=10)
                ttk.Label(windows, text=data["phone"][i]).place(x=430, y=10)

                ttk.Label(windows, text="Name:", style="Bold.TLabel").place(x=150, y=40)
                ttk.Label(windows, text=data["legal_name"][i]).place(x=190, y=40)

                ttk.Label(windows, text="Operation Classification:", style="Bold.TLabel").place(x=150, y=70)
                ttk.Label(windows, text=data["oper_classification"][i]).place(x=300, y=70)

                ttk.Label(windows, text="Carrier Operation:", style="Bold.TLabel").place(x=150, y=100)
                ttk.Label(windows, text=data["carrier_oper"][i]).place(x=260, y=100)
            
            update_label_data(i)
            callBtnStyle = ttk.Style ()
            callBtnStyle.configure("Call.TButton", background="green")
            # add button to call
            call_button = ttk.Button(windows, text="Call", style="Call.TButton", width=15, cursor="hand2")
            call_button.place(x=150, y=130)      
            call_button.config(command=lambda: call(driver, data["phone"][i]))

            endCallStyle = ttk.Style ()
            endCallStyle.configure("EndCall.TButton", background="red")
            # add button to end call
            end_call_button = ttk.Button(windows, text="End Call", style="EndCall.TButton", width=15, cursor="hand2")
            end_call_button.place(x=280, y=130)  
            end_call_button.config(command=lambda: end_call(driver))
            
            # add button for back record
            back_button = ttk.Button(windows, text="<", width=5, cursor="hand2")
            back_button.place(x=500, y=130)
            # subtract 1 from if i is greater than 0
            def back_record():
                global i
                if i > 0:
                    i -= 1
                    update_label_data(i)
            back_button.config(command=back_record) 

            # add button to for next record
            next_button = ttk.Button(windows, text=">", width=5, cursor="hand2")
            next_button.place(x=540, y=130)
            # add 1 to i if i is less than rows
            def next_record():
                global i
                if i < rows-1:
                    i += 1
                    update_label_data(i)
            next_button.config(command=next_record)

            # add large text box for message
            ttk.Label(windows, text="Message").place(x=150, y=180)
            message_input = ScrolledText(windows, wrap=tk.WORD, width=50, height=5)
            message_input.place(x=150, y=200)
            

            # add button to send message
            send_message_button = ttk.Button(windows, text="Send Message", width=15, cursor="hand2")
            send_message_button.place(x=150, y=300)
            send_message_button.config(command=lambda: send_message(driver, data["phone"][i], message_input.get("1.0", tk.END)))

    update_col2()

    windows.mainloop()