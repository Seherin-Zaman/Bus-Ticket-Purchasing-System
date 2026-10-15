# ---------- ADMIN MENU ----------
import pandas as pd          # used to work with CSV files
import os                    # used for clearing screen
import time                  # used for delays (sleep)



# ---------- imported classes ---------
from ViewRegisteredUser import ViewRegisteredUserManager               # Shows registered users
from ViewLoggedInUser import ViewLoggedInUserManager                   # Shows logged-in users
from ViewTicketSellingDetails import ViewTicketSellingDetailsManager   # Shows ticket receipts
from ChangeBusTimeTable import ChangeBusTimeTableManager               # Changes bus timetable
from AddBusTimeTable import AddBusTimeTable                            # Adds new timetable
from ChangePrice import ChangePriceManager                             # Changes ticket price
from AddBusDetails import BusDetailsManager                            # Adds details to main bus file


# ---------- class for s=saving csv file in variables ----------
class AdminMenu:
    def __init__(self):
        pass
        
        
# ---------- clear() method to wipe the terminal ----------
    def clear(self):
        # Clear terminal screen (Windows / Mac / Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
# ---------- method for the pause effect ----------
    def pause(self):
        # Wait for admin before continuing
        input("\nPress Enter to continue...")
        

# ---------- method for loading effect ----------      
    def loading(self, text):
        for i in range(3):                   #appears 3 timess
            print(f"{text} {'.'*(i+1)}")     # print statement
            time.sleep(0.2)                  # to delay
            self.clear()                     # to clear terminal

        

    # ---------- MENU LOOP ----------
    def show_menu(self):
        ValidInput = True      # Keeps the menu running

        while ValidInput:      # Loop forever until Exit chosen
            self.clear()       # Clear screen before showing menu
            print("""
🛠  ADMIN DASHBOARD
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1.  View Registered Users
2.  View Logged In Users
3.  View Ticket Selling Details
4.  Change Bus TimeTable
5.  Add New Bus TimeTable
6.  Change Ticket Price
7.  Add New Details In Main Bus Details File
0.  Exit Admin Panel
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

            choice = input("Select an option: ").strip()      # Take admin choice
            
            

            # ----- OPTION 1 -----
            if choice == "1":
                self.loading("Viewing Registered Users")
                ViewRegisteredUser = ViewRegisteredUserManager()     # Create object
                ViewRegisteredUser.ViewRegisteredUsers()             # Show users list
                self.loading("Processing")
                

            # ----- OPTION 2 -----
            elif choice == "2":
                self.loading("Viewing Logged In Users")
                ViewLoggedInUser = ViewLoggedInUserManager()         # create object
                ViewLoggedInUser.ViewLoggedInUsers()                 # show looged In list
                self.loading("Processing")
                

            # ----- OPTION 3 -----
            elif choice == "3":
                self.loading("Viewing ticket selling details")
                DetailsManager = ViewTicketSellingDetailsManager()   #create object
                DetailsManager.ViewTicketSellingDetails()            # show ticket selling details
                self.loading("Processing")
                
                

            # ----- OPTION 4 -----
            elif choice == "4":
                self.loading("Changing Bus TimeTable")
                ChangeTime = ChangeBusTimeTableManager               # create object
                ChangeTime.ChangeBusTimetable()                      # call to change time
                self.loading("Processing")
                
                
                
            # ----- OPTION 5 -----
            elif choice == "5":
                self.loading("Adding Bus TimeTable")
                AddTime = AddBusTimeTable()                          # create object
                AddTime.AddBusTimetable()                            # call to add time
                self.loading("Processing")
                
                
                
            # ----- OPTION 6 -----
            elif choice == "6":
                self.loading("Changing Ticket Price")
                PriceChange = ChangePriceManager()                   # create object
                PriceChange.ChangePrice()                            # call to change price
                self.loading("Processing")
                
            

            # ----- OPTION 7 -----
            elif choice == "7":
                self.loading("Adding Bus Details")
                DetailsManager = BusDetailsManager()                 # create object
                DetailsManager.AddDetails()                         # adds details to main bus file
                self.loading("Processing")
                
                

            # ----- exit -----
            elif choice == "0":
                self.loading("Logging out")
                self.loading("Logging out")
                self.clear()
                ValidInput = False             # Stop loop — exit admin menu

            else:
                print("\n❌ Invalid option.")
                self.pause()                  # for pause effect

    
    
