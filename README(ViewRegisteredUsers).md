# Branch Name
- ViewRegisteredUsers

## Python File Name
- ViewRegisteredUser.py

## Actor
- Admin

## Preconditions
- Admin must be logged in to the system.
- RegisteredUsers.csv may or may not exist.

## Class
- ViewRegisteredUserManager

## Methods
- __init__()
    - Initializes the file path for storing registered user data (RegisteredUsers.csv).
- clear()
    - Clears the terminal screen.
    - Compatible with Windows, macOS, and Linux.
- pause()
    - Pauses program execution until the admin presses Enter.
    - Improves readability and user control.
- ViewRegisteredUsers()
    - Clears the terminal screen.
    - Displays a heading for registered users.
    - Checks whether the registered users file exists.
    - Reads and displays user data from the CSV file if available.
    - Displays appropriate messages if no users exist.
    - Pauses execution before returning to the admin menu.
 
## Responsibility
- This class allows the Admin to view all registered users by reading user data from the RegisteredUsers.csv file.

## Main Flow
- Admin selects “View Registered Users” from the admin menu.
- The terminal screen is cleared.
- The system checks whether RegisteredUsers.csv exists.
- If the file exists and contains data:
   - Registered users are displayed in a tabular format.
- Admin presses Enter to return to the admin menu.

## Postconditions
- Registered users are displayed successfully (if any exist).
- Admin is returned to the admin menu.

## Alternative Flow
- If CSV file does not exist
  - System displays the message: “No registered users found.”
- Admin presses Enter to return to the admin menu.

- If CSV file exists but is empty
   -System displays the message:“No users yet.”
- Admin presses Enter to return to the admin
