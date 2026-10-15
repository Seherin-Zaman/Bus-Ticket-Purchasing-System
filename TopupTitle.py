# ---------- imported the module -----------
import pandas as pd
import time



# ---------- TopupTitle() ----------
class TopupTitle:
    def __init__(self, csv_file):
        self.csv_file = csv_file  #store csv file
        self.df = pd.read_csv(csv_file)  #read csv file
        self.unique_topups = []   #store unique topup titles
    


# ---------- ShowTopupTitle() method for showing topup titles for the selected ticket ----------
    def ShowTopupTitle(self, SelectedTitle):
        # filter rows for the selected category title
        SpecificTitles = self.df[self.df["category_title"] == SelectedTitle]
        
        if SpecificTitles.empty:
            print("No topup titles are available.")
            return
        
        print("\n🎫 AVAILABLE TOPUP TITLES")
        print("━━━━━━━━━━━━━━━━━━━━━━━")
        
        # store topup titles so SelectTitle() can use them
        self.unique_topups = SpecificTitles["topup_title"].dropna().unique()
        
        
        
        #show titles
        for i, title in enumerate(self.unique_topups, start=1):
            print(f"{i}. {title}")
            
        
            
# ---------- SelectTitle() method ----------
    def SelectTitle(self):
        time.sleep(0.3)
        ValidInput = True
        while ValidInput:  #loop will continue until the user give integer
            try:
                choice = int(input("\n👉 Select one of these: "))   #taking input from the user
                
                
                
                if 1 <= choice <= len(self.unique_topups):
                    selected = self.unique_topups[choice - 1]
                    
                    print(f"\n✔ You selected topup: {selected}")
                    time.sleep(1)
                    return selected
                else:
                    print("❌ Please select a valid number.")

            except ValueError:
                print("\n❌ Numbers only!")
