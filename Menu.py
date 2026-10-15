# ---------- Menu.py ----------
import os
import time
from TicketTitle import run_purchase_flow
from ConfidentialInfoHandling import ConfidentialInfoManager
from Purchase import PurchaseManager
from TimeTable import BusTimetable

class MenuOfTheApp:
    def __init__(self):
        self.LoggedIn = False
        self.current_user = None
        self.auth_manager = ConfidentialInfoManager()

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")

    def loading(self, text):
        for i in range(3):
            print(f"{text} {'.'*(i+1)}")
            time.sleep(0.3)
            self.clear()

    def PreLoginMenu(self):
        self.clear()
        print("""
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      🚌 BUS TICKET APP
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  """)     #print a welcome message and options
   
        print("Do not have an account? Please register first")   #If customer has not any account, he should make an account first
        print("1. 🔐 Login")
        print("2. 📝 Register")
        print("0. 🚪 Exit")

        # ----------- Input validation -----------
        ValidInput = True
        while ValidInput:
          try:
            choice = int(input("\n👉 Select an option: "))
            ValidInput = False
          except ValueError:
            print("\n❌ Numbers only! Try again.")
            time.sleep(1)
          

        if choice == 1:
            self.login()
        elif choice == 2:
            self.register()
        elif choice == 0:
            self.loading("Logging Out")
            time.sleep(1)
            print("\n✔Thank you for using Bus Ticket App! 👋")
        else:
            print("❌ Invalid choice")
            self.PreLoginMenu()

    def login(self):
        self.loading("Opening Login")
        user = self.auth_manager.login()
        if user:
            self.current_user = user
            self.LoggedIn = True
            input("Press click Enter to see options")
            self.loading("Processing")
            self.PostLoginMenu()
        else:
            input("Press Enter to return...")
            self.PreLoginMenu()

    def register(self):
        self.loading("Opening Registration")
        success = self.auth_manager.register()
        if success:
            input("Press Enter to return to login menu...")
            self.loading("Processing")
        self.PreLoginMenu()

    def PostLoginMenu(self):
        self.clear()
        print("1. Purchase Ticket")
        print("2. View Purchased Ticket")
        print("3. View Bus TimeTable")
        print("0. Exit")
        
        # ----------- Input validation -----------
        ValidInput = True
        while ValidInput:
          try:
            choice = int(input("\n👉 Select an option: "))
            ValidInput = False
          except ValueError:
            print("\n❌ Numbers only! Try again.")
            time.sleep(1)
            self.clear()
            self.loading("Viewing Purchased Ticket")
          
        if choice == 1:
            self.loading("Loading Ticket Purchase")
            run_purchase_flow(self.current_user)
            input("Press Enter to return")
            self.PostLoginMenu()
        elif choice == 2:
            self.loading("Processing")
            purchase = PurchaseManager()
            purchase.ViewPurchasedTickets(self.current_user)
            input("Press Enter to return")
            self.loading("Processing")
            self.PostLoginMenu()
        elif choice == 3:
            self.loading("Processing")
            timetable = BusTimetable()
            timetable.ViewTimeTable()
            input("Press Enter to return")
            self.loading("Processing")
            self.PostLoginMenu()
        elif choice == 0:
            self.loading("Logging Out")
            time.sleep(1)
            print("\n✔Thank you for using Bus Ticket App! 👋") 
        else:
            print("❌ Invalid choice")
            self.PostLoginMenu()

if __name__ == "__main__":
    BusTicketApp = MenuOfTheApp()
    BusTicketApp.PreLoginMenu()
