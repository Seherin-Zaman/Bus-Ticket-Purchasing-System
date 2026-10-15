# ---------- imported the modules ---------- 
import pandas as pd
import time
import os



# ----------- TopupPassengerClassQuantityManager() ----------
class TopupPassengerClassQuantityManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file   # store the file
        self.df = pd.read_csv(csv_file)  # read the file
        


# ---------- clear() for wiping the terminal ----------
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        


# ---------- loading() for giving the loading effect ----------
    def loading(self,text):
        for i in range(3):
            print(f"{text} {'.'* (i+1)}")
            time.sleep(0.2)  #used it to make the loading 
            self.clear()  # wiping the terminal
            
            
        

# ----------- ShowTopupPassengerClassQuantity() method for showing class quantity-----------
    def ShowTopupPassengerClassQuantity(self, SelectedTopup):
        # filter rows for the selected topup title
        SpecificTopup = self.df[self.df["topup_title"] == SelectedTopup]

        if SpecificTopup.empty:
            print("\n🎁 TOPUP Passenger Class Quantity")
            print("━━━━━━━━━━━━━━")
            print("No topup passenger class name is available for this topup.")
            return

        
        # get the class name (may contain NaN if empty in CSV) 
        ClassQuantity = SpecificTopup["topup_passenger_class_quantity"].iloc[0]

        
        # check if value is missing 
        # pd.isna() is used because empty cells in CSV become NaN in pandas.
       
        if pd.isna(ClassQuantity):
            print("\n🎁 TOPUP Passenger Class Quantity")
            print("━━━━━━━━━━━━━━")
            print("Class quantity not available for this topup.")
            return
        
        
        print("\n🎁 TOPUP Passenger Class Quantity")
        print("━━━━━━━━━━━━━━")
        print(f"Class Quantity: { ClassQuantity}")   # printing the class id
        time.sleep(1)                                # to delay
        self.clear()                                 # clear terminal
        return ClassQuantity                         # return value
