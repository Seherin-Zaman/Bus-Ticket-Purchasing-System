# ---------- TicketTitle.py ----------
import os
import time
import pandas as pd




# ----------- import classes ----------
from TicketDescription import TicketDescriptionManager
from TopupTitle import TopupTitle
from TopupDescription import TopupDescriptionManager
from TopupPrice import TopupPriceManager
from TopupEntitlementType import TopupEntitlementTypeManager
from TopupEntitlementUnit import TopupEntitlementUnitManager
from TopupEntitlementValue import TopupEntitlementValueManager
from TopupEntitlementQuantity import TopupEntitlementQuantityManager
from TopupEntitlementStartDate import TopupEntitlementStartDateManager
from TopupEntitlementEndDate import TopupEntitlementEndDateManager
from TopupPassengerClassId import TopupPassengerClassIdManager
from TopupPassengerClassName import TopupPassengerClassNameManager
from TopupPassengerClassQuantity import TopupPassengerClassQuantityManager
from Purchase import PurchaseManager
from Receipts import Receipt
from Purchase import PurchaseManager  # make sure this exists



# ---------- Ticket title class ----------
class TicketCategoryTitle:
    def __init__(self, number, title):
        self.number = number
        self.title = title



# ---------- Ticket manager ----------
class TicketCategoryTitleManager:
    def __init__(self, csv_file="mobile_products.csv"):
        self.csv_file = csv_file
        self.AllTitles = []
        self.titles = set()
        self.LoadTitles()


# ---------- method to clear terminal ----------
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


# ---------- method for loading effect ----------
    def loading(self, text):
        for i in range(3):
            print(f"{text} {'.'*(i+1)}")
            time.sleep(0.2)
            self.clear()


    

 # ---------- method to store objects ----------
    def LoadTitles(self):
        df = pd.read_csv(self.csv_file)
        number = 1
        for title in df["category_title"]:
            if title not in self.titles:
                self.titles.add(title)
                self.AllTitles.append(TicketCategoryTitle(number, title))
                number += 1

 

# ---------- method to showcase titles ----------
    def ShowTitles(self):
        self.loading("Loading ticket categories")
        print("📋 Categories:")
        for t in self.AllTitles:
            print(f"{t.number}. {t.title}")



# ---------- method to select title ----------    
    def SelectTitle(self):
        ValidInput = True
        while ValidInput:
            try:
                choice = int(input("\nSelect a ticket: "))
                if 1 <= choice <= len(self.AllTitles):
                    selected = self.AllTitles[choice-1]
                    print(f"\n✔ You selected: {selected.title}")
                    return selected
                else:
                    print("❌ Invalid number.")
            except ValueError:
                print("❌ Numbers only.")




# ---------- Run purchase flow ----------
def run_purchase_flow(username):
    if not username:
        print("❌ No user logged in.")
        return

    manager = TicketCategoryTitleManager("mobile_products.csv")
    manager.ShowTitles()      # call method to show titles
    
    selected = manager.SelectTitle()
    if selected:
        manager.loading("Loading titles of the tickets")
        
# --------- To see the description of selected Ticket ---------
        DescriptonManager = TicketDescriptionManager("mobile_products.csv")
        DescriptonManager.ShowDescription(selected.title)
        
# ---------- To display and select TopupTitle ----------
        TopupTitleManager = TopupTitle("mobile_products.csv")
        TopupTitleManager.ShowTopupTitle(selected.title)
        SelectedTopupTitle = TopupTitleManager.SelectTitle()
        
# -------- To see the description of selected TopupTitle ----------
        TopupDescriptonManager = TopupDescriptionManager("mobile_products.csv")
        TopupDescriptonManager.ShowTopupDescription(selected.title)
        
# --------- To see the price of the selected TopupTitle ----------
        PriceManager = TopupPriceManager("mobile_products.csv")
        Price = PriceManager.ShowTopupPrice(SelectedTopupTitle)
        
# --------- To see Topup Entitlement typeof the selected Topup Title -----------
        EntitlementTypeManager = TopupEntitlementTypeManager("mobile_products.csv")
        EntitlementTypeManager.ShowTopupEntitlementType(SelectedTopupTitle)
        
# --------- To see Topup Entitlement unit of the selected Topup Title -----------
        EntitlementUnitManager = TopupEntitlementUnitManager("mobile_products.csv")
        EntitlementUnitManager.ShowTopupEntitlementUnit(SelectedTopupTitle)
        
# --------- To see Topup Entitlement value of the selected Topup Title -----------
        EntitlementValueManager = TopupEntitlementValueManager("mobile_products.csv")
        EntitlementValueManager.ShowTopupEntitlementValue(SelectedTopupTitle)
        
# --------- To see Topup Entitlement quantity of the selected Topup Title -----------
        EntitlementQuantityManager = TopupEntitlementQuantityManager("mobile_products.csv")
        EntitlementQuantityManager.ShowTopupEntitlementQuantity(SelectedTopupTitle)
                         
# --------- To see Topup Entitlement start date of the selected Topup Title -----------
        EntitlementStartDateManager = TopupEntitlementStartDateManager("mobile_products.csv")
        StartDate = EntitlementStartDateManager.ShowTopupEntitlementStartDate(SelectedTopupTitle)
                 
# --------- To see Topup Entitlement end date of the selected Topup Title -----------
        EntitlementEndDateManager = TopupEntitlementEndDateManager("mobile_products.csv")
        EndDate = EntitlementEndDateManager.ShowTopupEntitlementEndDate(SelectedTopupTitle)
                 
# --------- To see Topup Passenger Class Id of the selected Topup Title -----------
        PassengerClassIdManager = TopupPassengerClassIdManager("mobile_products.csv")
        PassengerClassIdManager.ShowTopupPassengerClassId(SelectedTopupTitle)
                                            
# --------- To see Topup Passenger Class Name of the selected Topup Title -----------
        PassengerClassNameManager = TopupPassengerClassNameManager("mobile_products.csv")
        ClassName = PassengerClassNameManager.ShowTopupPassengerClassName(SelectedTopupTitle)
                                            
# --------- To see Topup Passenger Class Quantity of the selected Topup Title -----------
        PassengerClassQuantityManager = TopupPassengerClassQuantityManager("mobile_products.csv")
        Quantity = PassengerClassQuantityManager.ShowTopupPassengerClassQuantity(SelectedTopupTitle)
     
 # --------- To buy ticket --------   
        purchase = PurchaseManager()
        purchase.choice(username, selected.title, selected.title, Price, ClassName, Quantity, StartDate, EndDate)



