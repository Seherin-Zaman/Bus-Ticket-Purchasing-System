# ---------- imported the modules ---------- 
import pandas as pd
import time



# ----------- TopupPassengerClassNameManager() ----------
class TopupPassengerClassNameManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file   # store the file
        self.df = pd.read_csv(csv_file)  # read the file
        

# ----------- ShowTopupPassengerClassName() method for showing class name-----------
    def ShowTopupPassengerClassName(self, SelectedTopup):
        # filter rows for the selected topup title
        SpecificTopup = self.df[self.df["topup_title"] == SelectedTopup]

        if SpecificTopup.empty:
            print("No topup passenger class name is available for this topup.")
            return

# ----------- get the class name (may contain NaN if empty in CSV) -----------
        ClassName = SpecificTopup["topup_passenger_class_name"].iloc[0]

# ---------- check if value is missing ----------
        # pd.isna() is used because empty cells in CSV become NaN in pandas.
       
        if pd.isna(ClassName):
            print("\n🎁 TOPUP Passenger Class Name")
            print("━━━━━━━━━━━━━━")
            print("Class Name not available for this topup.")
            return
        
        print("\n🎁 TOPUP Passenger Class Name")
        print("━━━━━━━━━━━━━━")
        print(f"Class Name: { ClassName}")   # printing the class id
        time.sleep(0.3)  # to delay
        return ClassName
