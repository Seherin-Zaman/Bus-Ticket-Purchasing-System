# Branch Name 
- ViewLoggedInUsers

## Python File Name
- ViewLoggedInUser.py

## CSV File Name
- LoggedInusers.csv

## Actor
- Admin

## Preconditions
- Admin must be logged in.
- LoggedInUsers.csv may or may not exit.

## Class
- ViewLoggedInUserManager

## Methods
- ### __init__()
    - Initializes the file path for storing logged-in user session data (LoggedInUsers.csv).
- ### clear()
    - Clears the terminal screen.
    - Compatible with Windows, macOS, and Linux operating systems.
- ### pause()
    - Pauses program execution until the admin presses Enter.
    - Improves readability and gives user control over screen navigation.
- ### ViewLoggedInUsers()
    - Clears the terminal screen.
    - Displays a heading for logged-in users.
    - Checks whether the logged-in users file exists.
    - Reads and displays the CSV file if available.
    - Pauses execution before returning to the admin menu.


## Responsibility
- This class allows the Admin to view all currently logged-in users by reading session data from the LoggedInUsers.csv file.

## Main Flow
- Admin selects “View Logged In Users” from the admin menu.
- The terminal screen is cleared.
- The system checks whether LoggedInUsers.csv exists.
- If the file exists:
    - Logged-in users are displayed in a tabular format.
    - Admin presses Enter to return to the admin menu.

 ## Postconditions
 - Logged-in users are displayed successfully (if any exist).
 - Admin is safely returned to the admin menu.
   
## Alternative Flow
- If LoggedInUsers.csv does not exist
   - System displays the message: “No active sessions.”
- Admin presses Enter to return to the admin menu.
