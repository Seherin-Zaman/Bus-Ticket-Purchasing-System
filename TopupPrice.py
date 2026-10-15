# ---------- imported the modules ---------- 
import pandas as pd
import time




# ---------- TopupPriceManager() ----------
class TopupPriceManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file  # store the file
        self.df = pd.read_csv(csv_file)  # read the file



# ---------- ShowTopupPrice() method for showing price ----------
    def ShowTopupPrice(self, SelectedTopup):
    # filter rows for the selected topup title
        SpecificTopup = self.df[self.df["topup_title"] == SelectedTopup]

        if SpecificTopup.empty:                                      #if empty
          print("\n💰 TOPUP PRICE")
          print("━━━━━━━━━━━━━━")
          print("No price available for this topup.")
          return
    
        # get the price as a scalar value 
        raw_price = SpecificTopup["topup_price_in_pence"].values[0]  # use .values[0] to get the scalar
        
    
    
    # .isna() is used to handle Nan 
        if pd.isna(raw_price):
          print("\n💰 TOPUP PRICE")
          print("━━━━━━━━━━━━━━")
          print("Price not available for this topup.")
          return
      
        formatted_price = raw_price / 100               # convert to real price

        
        print("\n💰 TOPUP PRICE")
        print("━━━━━━━━━━━━━━")
       
        print(f"Price: £{formatted_price:.2f}")         # now it will format correctly
        time.sleep(0.3)                                 #to delay
        return  formatted_price                         # return value
        
