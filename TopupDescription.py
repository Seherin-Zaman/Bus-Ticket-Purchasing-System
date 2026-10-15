# ---------- imported the modules ---------- 
import pandas as pd
import time
import os


# ----------- TicketDescriptionManager() ----------
class TopupDescriptionManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file               # store the file
        self.df = pd.read_csv(csv_file)        # read the file
        



# ---------- clear() method to clear terminal ----------
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        



# ---------- loadind() method for loading effect ----------
    def loading(self,text):
        for i in range(3):
            print(f"{text} {'.'* (i+1)}")
            time.sleep(0.2)                           #used it to make the loading 
            self.clear()                              # wiping the terminal
            



# ----------- ShowTopupDescription() method for showing description -----------
    def ShowTopupDescription(self, SelectedTitle):
        SpecificDesription = self.df[self.df["category_title"] == SelectedTitle]    #stored the data of the specific title
        
        if SpecificDesription.empty:
            print("No description is available for this ticket")                    #If the description of the title is not available
            return
        
        
        description = SpecificDesription.iloc[0]["category_description"]            #store the specific an first description 
        
        # --- check if description is missing (NaN / empty) using isna() ---
        if pd.isna(description) or str(description).strip() == "":
            print("Description not provided for this topup yet.")
            return
        
        
        
        input("\nPress enter to see details")
        self.loading("loading details")
        
        print("\n💡 Topup Title")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        print(SelectedTitle) 
        print("\n📄 Topup Description") 
        print("━━━━━━━━━━━━━━━━━━━━━━━") 
        print(description)            #printing the description
        time.sleep(0.3)               # delayed to see the description properly
