# Autodialer

## Building Executable

```bash
pyinstaller --noconfirm --onedir --windowed --add-data "C:/Users/<user>/AppData/Local/Programs/Python/Python311/Lib/site-packages/customtkinter;customtkinter/"  "C:/Users/<user>/OneDrive/Documents/GitHub/Autodialer/main.py"
```

## Eliciting Requirements
- The user should be able to login to their OpenPhone account automatically (with OTP).
- It should be able to read the csv file for the clients details and should be able to go thourgh the client list via next and back buttons.
- He should be able to call the client that is currently selected for the conversation
- He should be able to end the call.
- He should be able to send messages to currently selected clients.
- The program should run smoothly without getting stuck.
- It should display appropriate error/info messages to tell the user about the current state of the program.

## User Stories

### User Authentication:

- As a user, I want to log in automatically to my OpenPhone account with or without OTP.

### Client Management:

- As a user, I want to import a CSV file containing client details.
- As a user, I want to view a list of clients with their names and contact information.
- As a user, I want to navigate through the client list using "next" and "back" buttons.

### Communication:

- As a user, I want to call the currently selected client by clicking a "Call" button.
- As a user, I want to end the ongoing call by clicking an "End Call" button.
- As a user, I want to send messages to the currently selected client using a messaging interface.

### User Interface:

- As a user, I want the program to display clear error messages if a call cannot be initiated.
- As a user, I want to receive info messages when a call has been successfully initiated.
- As a user, I want to be informed about any issues with sending messages to clients.

### Smooth Operation:

- As a user, I want the program to respond promptly when I click buttons or perform actions.
- As a user, I want to use the application without it getting stuck or freezing.

### Feedback and Confirmation:

- As a user, I want to see a confirmation message when a call ends successfully.
- As a user, I want to receive feedback when a message has been sent to a client.


### Error Handling:

- As a user, I want the program to display an error message if there's a problem reading the CSV file.
- As a user, I want to know if there's an issue with the OpenPhone API connection.
