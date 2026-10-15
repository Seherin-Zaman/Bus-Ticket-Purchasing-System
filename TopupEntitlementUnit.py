# ---------- imported the modules ---------- 
import pandas as pd
import time
import os


# ----------- TopupEntitlementUnitManager() ----------
class TopupEntitlementUnitManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file   # store the file
        self.df = pd.read_csv(csv_file)  # read the file
        

            


# ----------- ShowTopupEntitlementUnit() method for showing description -----------
    def ShowTopupEntitlementUnit(self, SelectedTopup):
    # filter rows for the selected topup title
        SpecificTopupEntitlementUnit = self.df[self.df["topup_title"] == SelectedTopup]

        if SpecificTopupEntitlementUnit.empty:
          print("\n🎁 TOPUP Entitlement Unit")
          print("━━━━━━━━━━━━━━")
          print("No entitlement unit is available for this topup.")
          return

    
        EntitlementUnit = SpecificTopupEntitlementUnit["topup_entitlement_unit"].iloc[0]  
        #check if value is missing 
        # pd.isna() is used because empty cells in CSV become NaN in pandas.
       
        if pd.isna(EntitlementUnit):
            print("\n🎁 TOPUP Entitlement Unit")
            print("━━━━━━━━━━━━━━")
            print("No entitlement unit is available for this topup.")
            return
        
        
        print("\n🎁 TOPUP Entitlement Unit")
        print("━━━━━━━━━━━━━━")
        
        print(f"Unit: {EntitlementUnit}") 
        time.sleep(0.3) #to delay
        
           
