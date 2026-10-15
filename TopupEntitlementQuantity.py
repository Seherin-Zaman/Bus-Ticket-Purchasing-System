# ---------- imported the modules ---------- 
import pandas as pd
import time
import os


# ----------- TopupEntitlementQuantityManager() ----------
class TopupEntitlementQuantityManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file   # store the file
        self.df = pd.read_csv(csv_file)  # read the file
        

            
# ----------- ShowTopupEntitlementQuantity() method for showing description -----------
    def ShowTopupEntitlementQuantity(self, SelectedTopup):
    
    
    # filter rows for the selected topup title
        SpecificTopupEntitlementQuantity = self.df[self.df["topup_title"] == SelectedTopup]

        
        if SpecificTopupEntitlementQuantity.empty:
          print("\n🎁 TOPUP Entitlement Quantity")
          print("━━━━━━━━━━━━━━")
          print("No entitlement value is available for this topup.")
          return

    
        EntitlementQuantity = SpecificTopupEntitlementQuantity["topup_entitlement_quantity"].iloc[0]  




# ---------- check if that value is NaN / blank ----------
        if pd.isna(EntitlementQuantity):
             print("\n🎁 TOPUP Entitlement Quantity")
             print("━━━━━━━━━━━━━━")
             print("Entitlement Quantity not available for this topup.")
             return
        
        
        
        print("\n🎁 TOPUP Entitlement Quantity")
        print("━━━━━━━━━━━━━━")
        
        print(f"Quantity: {EntitlementQuantity}") 
        time.sleep(0.3) #to delay     
