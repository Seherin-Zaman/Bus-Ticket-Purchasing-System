# Branch Name: ViewTicketSellingDetails

## Python File Name
- ViewTicketSellingDetails.py

## CSV File Name
- UserReceipts.csv

## Actor
- Admin

## Preconditions
- Actor must be logged in.
- UserReceipts.csv may or may not exist.

## Class
- ViewTicketSellingDetailsManager

## Methods
- ### __init__() - Initializes the path of the ticket receipts file (UserReceipts.csv).
- ### clear()    - Clears the terminal screen (Works on both Windows and Unix-based systems).
- ### pause()    - Pauses program execution until the admin presses Enter.
- ### ViewTicketSellingDetails() -
    - Clears the screen.
    - Displays a ticket sales report.
    - Reads ticket data from CSV.
    - Shows each ticket’s details in reverse order (latest first).

       Displays:
           Username,
           Ticket category,
           Top-up title,
           Price,
           Passenger class,
           Quantity,
           Start date,
           End date
      
    - Pauses after all records are shown.

## Responsibility
- This class allows the admin to view all ticket selling records stored in the UserReceipts.csv file.
- Ticket sales are displayed from latest to oldest in a readable receipt-style format.

## Main Flow
- Admin selects “View Ticket Selling Details” from the admin menu.
- Screen is cleared.
- System checks if UserReceipts.csv exists.
- If the file exists and contains data:
     -Ticket sales are displayed one by one (latest first).
- Admin presses Enter to return to the menu.

## Alternative Flow
- CSV file does not exist
    - Message: “No ticket sales yet.”
   - Admin is returned to menu.
     
- CSV file exists but is empty
    - Message: “No ticket sales yet.”
    - Admin is returned to menu.
