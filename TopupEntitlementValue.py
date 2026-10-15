# ---------- imported the modules ---------- 
import pandas as pd
import time
import os


# ----------- TopupEntitlementValueManager() ----------
class TopupEntitlementValueManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file   # store the file
        self.df = pd.read_csv(csv_file)  # read the file
        

            
# ----------- ShowTopupEntitlementValue() method for showing description -----------
    def ShowTopupEntitlementValue(self, SelectedTopup):
    # filter rows for the selected topup title
        SpecificTopupEntitlementValue = self.df[self.df["topup_title"] == SelectedTopup]

        if SpecificTopupEntitlementValue.empty:
          print("\n🎁 TOPUP Entitlement Value")
          print("━━━━━━━━━━━━━━")
          print("No entitlement value is available for this topup.")
          return

    
        EntitlementValue = SpecificTopupEntitlementValue["topup_entitlement_value"].iloc[0]  
        
# ---------- check if THAT value is NaN / blank ----------
        if pd.isna(EntitlementValue):
             print("\n🎁 TOPUP Entitlement Value")
             print("━━━━━━━━━━━━━━")
             print("Entitlement Value not available for this topup.")
             return

        print("\n🎁 TOPUP Entitlement Value")
        print("━━━━━━━━━━━━━━")
        
        print(f"Value: {EntitlementValue}") 
        time.sleep(0.3) #to delay
        
