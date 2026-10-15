# ---------- imported the modules ---------- 
import pandas as pd
import time



# ----------- TopupPassengerClassIdManager() ----------
class TopupPassengerClassIdManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file   # store the file
        self.df = pd.read_csv(csv_file)  # read the file
        

# ----------- ShowTopupPassengerClassId() method for showing class id-----------
    def ShowTopupPassengerClassId(self, SelectedTopup):
        # filter rows for the selected topup title
        SpecificTopup = self.df[self.df["topup_title"] == SelectedTopup]

        if SpecificTopup.empty:
            print("No topup passenger class id is available for this topup.")
            return

# ----------- get the class id (may contain NaN if empty in CSV) -----------
        ClassId = SpecificTopup["topup_passenger_class_id"].iloc[0]

# ---------- check if value is missing ----------
        # pd.isna() is used because empty cells in CSV become NaN in pandas.
       
        if pd.isna(ClassId):
            print("\n🎁 TOPUP Passenger Class Id")
            print("━━━━━━━━━━━━━━")
            print("Class Id not available for this topup.")
            return
        
        print("\n🎁 TOPUP Passenger Class Id")
        print("━━━━━━━━━━━━━━")
        print(f"Class Id: {ClassId}")   # printing the class id
        time.sleep(0.3)  # to delay
