# ---------- imported the modules ----------
import pandas as pd          # Used for reading and processing CSV data
import time                  # Used to add a short delay for better user experience



# ----------- TopupEntitlementTypeManager ----------
class TopupEntitlementTypeManager:
    

    def __init__(self, csv_file):
    
        self.csv_file = csv_file                 # Store CSV file path
        self.df = pd.read_csv(csv_file)          # Load CSV data into a DataFrame


    
    
    # ----------- ShowTopupEntitlementType() ----------
    def ShowTopupEntitlementType(self, SelectedTopup):

        # Filter the DataFrame for the selected top-up
        SpecificTopupEntitlementType = self.df[
            self.df["topup_title"] == SelectedTopup
        ]

        
        # If the selected top-up does not exist
        if SpecificTopupEntitlementType.empty:
            print("\n🎁 TOPUP Entitlement Type")
            print("━━━━━━━━━━━━━━")
            print("No entitlement type is available for this topup")
