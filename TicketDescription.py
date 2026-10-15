# ---------- imported the modules ---------- 
import pandas as pd

# ----------- TicketDescriptionManager() ----------
class TicketDescriptionManager:
    def __init__(self, csv_file):
        self.csv_file = csv_file   # store the file
        self.df = pd.read_csv(csv_file)  # read the file
        
# ----------- ShowDescription() method for showing description -----------
    def ShowDescription(self, SelectedTitle):
        SpecificDesription = self.df[self.df["category_title"] == SelectedTitle]  #stored the data of the specific title
        
        if SpecificDesription.empty:
            print("\n📄 CATEGORY DESCRIPTION") 
            print("━━━━━━━━━━━━━━━━━━━━━━━") 
            print("No description is available for this ticket")   #If the description of the title is not available
            return
        
        description = SpecificDesription.iloc[0]["category_description"]   #store the specific an first description 
# ---------- check if value is missing ----------
# pd.isna() is used because empty cells in CSV become NaN in pandas.
       
        if pd.isna(description):
            print("\n📄 CATEGORY DESCRIPTION") 
            print("━━━━━━━━━━━━━━━━━━━━━━━") 
            print("No description is available for this ticket") 
        
        
        print("\n📄 CATEGORY DESCRIPTION") 
        print("━━━━━━━━━━━━━━━━━━━━━━━") 
        print(description)   #printing the description
