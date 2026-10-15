# Branch Name: Menu
## Python File Name: 
- AdminMenu.py (Admin Interface)
- Menu.py (Customer Interface)

# AdminMenu.py
## Actor
- # Admin 
  
## Preconditions
- Admin is logged in

## Class: AdminMenu

## Methods
- ### clear()     – Clears the terminal screen
- ### pause()     – Pauses execution until user input
- ### loading()   – Displays a loading animation
- ### show_menu() - Displays menu, handles input, executes relevant methods, and manages errors

## Main Flow
- Admin menu is displayed.
- Admin selects an option by entering an option number.
- The system executes the relevant functionality.
- Menu reappears until admin exits.
  
## Menu Options
- View Registered Users
- View Logged In Uers
- View Ticket Selling Details
- Change Bus TimeTable
- Add New Bus TimeTable
- Change Ticket Price
- Add New Details In Main Bus Details File
- Exit Admin Panel

## Trigger
- Admin enters an option number via keyboard input.

## Postconditions
- Selected admin operation is executed successfully.
- Control returns to admin menu unless exit is selected.

## Alternative Flow
- Invalid input shows an error message and re-prompts the admin.
- Dictionary-based menu handling can be implemented to improve scalability.
 
    

