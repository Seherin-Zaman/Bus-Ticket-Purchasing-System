# FinalPythonProject
## This is a final python project of Foundation of Computer Programming module. In this project, I need to make Bus Ticket app using data from csv file.

## System Users
## This system has two types of users:
- **User** - can browse and buy tickets, view purchased tickets and timetable.
- **Admin** - view confidential data (Regiestered Users, LoggedIn users, selling details), change, add timetable, bus details, price.

### User Interface can
- Puchase ticket
- View Purchased ticket
- View Timetable

### Admin Interface can
- View Registered users
- View LoggedIn users
- View Ticket sellung details
- Change Timetable
- - Change price
- Add timetable
- Change price
- Add bus details

## To run User Interface
- ### run Menu.py

## To run Admin Interface
- ### run AdminAccessOfApp.py
  
## User Interface
## Actor
- User

### Use Case 1 - Authentication
-  Description: User selects a option(login, register and exit) from the pre login menu.
-  Outcome    : If a user is not registered, he would not be able to login. Also if the user does not provide correct login deatils, he would not be able to logged in.

### Use Case 2 - User selects an option from menu
- Description: User selects an option(Purchase Ticket, View Purchased Ticket, View Bus Timetable) from the main menu.
-  Outcome    : Creates object for revelent classes and run methods to execute select option. If the provided option number is not in the system, it will ask for it again.

### Use Case 3 - User selects Purchase Ticket
-  Description: User selects purchase ticket.
-  Outcome    : List of categories of tickets will appear.

### Use Case 4 - User selects category
-  Description: User sees and selects any one category from category titles.
-  Outcome    : Selected category will be stored and based on it other topups will be appear. If the provided category number is not in the system, it will ask for it. again.

### Use Case 5 - User sees description
 -  Description: Description of the selected category will be appeared.
 -  Outcome    :  User can see the description of the selected category.

### Use Case 6- User selects Topup Title
-  Description : User sees and selects Topup Title.
-  outcome     : Selected Topup Title will be stored and based on it other topups will be appeared. If the provided Topup title number is not in the system, it will ask for it. 

### Use Case 7 - Display Topups
-  Description : Different Topups (Topup Description, Topup Price, Topup Entitlement Value, Topup Entitlement Type, Topup Entitlement Unit, Topup Entilement Quantity, Topup Entitlement Start Date, Topup Entitlement End Date, Topup Passenger Class ID, Topup Passenger Class Name, Topup Passenger Class Quantity) will appear.
-  Outcome     : Topups of selected Topup Title will appear.

### Use Case 8 - Purchase Ticket
-  Description: Take input from user to confirm the purchase.
-  Outcome    : If yes, the purchase is confirmed. Else options will re appear.

### Use Case 9 - View Purchase Ticket
-  Description: User selects View Purchase Ticket.
-  Outcome    : All purchased tickets by user will appear ( from latest to oldest).

### Use Case 10 - View Bus TimeTable
-  Description: User selects Bus TimeTable. 
-  Outcome    : User can see bus timetable.

### Use Case 11 - User Types Bus Number.
-  Description: User provides a Bus number.
-  Outcome    : If the bus number is not in the timetable, it will ask for correct registered bus number.


### Use Case 11 - Exit
- Description: User selects exit.
- Outcome: User will be logged out.
  

## Admin Interface
## Actor
- Admin

### Use Case 1 - Authentication
- ### Description: Username: @dmin@ and Password: 27@@&@@13Admin needs to login first with fixed login details.
- ### Outcome    : If admin does not provide correct login details, program will ask for it again until it gives correct details.

### Use Case 2 - Admin selects an option from menu
-  Description: Options(View RegsisteredUsers, View LoggedInUsers, View TicketSellingDetails, Change Bus TimeTable. Add Bus TimeTables, Change Price, Add Bus Details) will appear. If the user types option number which is not in the menu, the admin needs to type again until gives correct one.
-  Outcome    : Admin selcts an option. Objects will be created and methods of revelent classes will be run to execute the option.

 ### Use Case 3 - Admin selects View RegisteredUsers
-  Description: Admin selects to see registered users.
-  Outcome    : List of registered users will be appeared by reading csv file.

### Use Case 4 - Admin selects View LoggedInUsers
-  Description: Admin selects to see logged in users.
-  Outcome    : List of logged in users will be appeared by reading csv file.

### Use Case 5 - Admin selects View TicketSellingDetails.
-  Description: Admin selects to see sold ticket deatils.
-  Outcome    : List of sold ticket details will be appeared by reading csv file.

### Use Case 6 - Admin selects Change Bus TimeTable.
-  Description:
   -  Bus Timetable will be changed if the admin confirms the change. If not, it will go back to menu.
   -  If admin does not provide correct registered bus number it will ask again until the admin provides correct one.
-  Outcome    : Admin can change bus timetable successfully.

### Use Case 7 - Admin selects Add Bus TimeTable.
-  Description:
   -  Bus Timetable will be added if the admin confirms the change. If not, it will go back to menu.
   -  Admin needs to provide Bus Number, Stop and Time.
   - If time is not integer and formatted, it will ask for it again until it gives correct time.
-  Outcome:
-  If the admin confirms, the changes will be saved and add to csv file.
-  Else it will ask whether the admin wants to add another.
    -  If yes, it will again ask details.
    -  Else it will go back to menu.

### Use Case 8 - Admin selects Change Price.
-  Description:
  -  Topup Titles, ID and price will appear.
  - Admin needs to provide ID. If ID is invalid, the program will ask for it again.
  -  After selecting ID, the admin needs to provide price in pence.
-  Outcome:
   -  If admin confirms, it will be saved. Else it will discard and go back.

### Use Case 9 - Admin selects Add Bus Details.
-  Description:
   -  List od headers from csv file will appear.
   -  Admin will select heading and add value.
   -  If adding finish, admin needs to type done.
-  Outcome: New Bus details will be added.

### Use Case 10 - Exit
-  Description: Admin selects exit.
-  Outcome: Admin will be logged out.

## Testing
-  Multiple testing is done which is documented on github repository.
  
## Review
- Could have made authentication system strong by adding function to check password strength.
- Could have made customer class and store all object in a list.
- Could have added more options in user interface.
- Could have used graphical design.
- Could have handled multiple admin.
- Could have made admin password stronger.
- Could have showcase tickets based on vaidity by termining the invalid ones.
  
