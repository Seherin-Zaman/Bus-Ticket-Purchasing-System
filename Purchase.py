# ---------- import the modules ---------
import time
import pandas as pd
import os

# ---------- import a class ----------
from Receipts import Receipt


# ---------- class for purchasing the ticket ----------
class PurchaseManager:
    def __init__(self):
        # list that stores all created receipts (in memory)
        self.receipt = []

        # stores the MOST RECENT receipt
        self.CurrentReceipt = None
    

    # ---------- clear() for wiping the terminal ----------
    def clear(self):
        # Windows uses 'cls', Mac/Linux uses 'clear'
        os.system('cls' if os.name == 'nt' else 'clear')


    # ---------- loading() for giving the loading effect ----------
    def loading(self,text):
        # show loading text 3 times with dots
        for i in range(3):
            print(f"{text} {'.'* (i+1)}")
            time.sleep(0.2)          # short pause
            self.clear()             # clear screen
            

    # ---------- ask user if they want to buy ----------
    def choice(self,UserName, CategoryTitle, TopupTitle, Price, ClassName, Quantity, StartDate, EndDate):
        
        ValidInput = True
        
        # repeat until user types y or n
        while ValidInput:
            choice = input("Do you want to buy a ticket? (y/n): ").strip().lower()

            # YES → continue purchase
            if choice in ("y", "yes"):
                self.ConfirmPurchase(
                    UserName, CategoryTitle, TopupTitle,
                    Price, ClassName, Quantity, StartDate, EndDate
                )
                ValidInput = False

            # NO → cancel and stop loop
            elif choice in ("n", "no"):
                self.loading("Cancelling purchase process")
                print("Purchase Process cancelled.")
                ValidInput = False  

            # invalid answer
            else:
                print("❌ Please type only 'y' or 'n'.")


    # ---------- confirm and finalize purchase -----------
    def ConfirmPurchase(self, UserName, CategoryTitle, TopupTitle, Price, ClassName, Quantity, StartDate, EndDate):
          
            # simulate processing steps
            self.loading("Processing")
            self.loading("Finalizing purchase")

            print("🎟️ Purchase completed successfully!")
            time.sleep(2)

            self.loading("Processing receipt")

            # ----------- create Receipt object -----------
            self.CurrentReceipt = Receipt(
                UserName, CategoryTitle, TopupTitle,
                Price, ClassName, Quantity, StartDate, EndDate
            )

            # keep it in memory
            self.receipt.append(self.CurrentReceipt)

            # show receipt on screen
            self.ShowReceipt()

            # save receipt to CSV
            self.SaveReceiptsToCsv()
            

    # ---------- To show receipt ----------
    def ShowReceipt(self):

        # shortcut variable
        r = self.CurrentReceipt

        print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("        🧾 PURCHASE RECEIPT")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")

        # printing all details
        print(f"    UserName   :  {r.UserName}")
        print(f"    Category   :  {r.CategoryTitle}")
        print(f"    Topup Title:  {r.TopupTitle}")
        print(f"    Price      :  £{r.Price}")
        print(f"    Class      :  {r.ClassName}")
        print(f"    Quantity   :  {r.Quantity}")
        print(f"    Start Date :  {r.StartDate}")
        print(f"    End Date   :  {r.EndDate}")

        print("\n✔ Thank you for your purchase!\n")
        time.sleep(0.3)
        

    # ---------- View all purchased tickets of a user ----------
    def ViewPurchasedTickets(self, username):

      FileName = "UserReceipts.csv"

      print("\n🚌 VIEW PURCHASED TICKETS\n")

      # if file doesn't exist yet
      if not os.path.exists(FileName):
        print("❌ No receipts file found yet.")
        return

      # read CSV file
      df = pd.read_csv(FileName)

      # filter records belonging to the logged-in user
      user_tickets = df[df["UserName"].str.lower() == username.lower()]

      if user_tickets.empty:
        print("⚠ You have not purchased any tickets yet.")
        return

      # iterate in REVERSE (newest first)
      for i, row in user_tickets.iloc[::-1].iterrows():

        print("\n┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
        print("        🧾 PURCHASE RECEIPT")
        print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")

        print(f"  UserName    : {row['UserName']}")
        print(f"  Category    : {row['Category']}")
        print(f"  Topup Title : {row['Topup Title']}")
        print(f"  Price       : £{row['Price']}")
        print(f"  Class       : {row['Class']}")
        print(f"  Quantity    : {row['Quantity']}")
        print(f"  Start Date  : {row['Start Date']}")
        print(f"  End Date    : {row['End Date']}")
        print()
     
        
    # ---------- Save receipt to CSV ----------
    def SaveReceiptsToCsv(self):

     # if nothing to save
     if not self.CurrentReceipt: 
          print("No receipt is available") 
          return
      
     FileName = "UserReceipts.csv"

     # shortcut to object
     r = self.CurrentReceipt

     # turn single receipt into dataframe row
     df = pd.DataFrame([{
        "UserName": r.UserName,
        "Category": r.CategoryTitle,
        "Topup Title": r.TopupTitle,
        "Price": r.Price,
        "Class": r.ClassName,
        "Quantity": r.Quantity,
        "Start Date": r.StartDate,
        "End Date": r.EndDate
     }])

     # append if file exists — otherwise create new
     if os.path.exists(FileName):
        df.to_csv(FileName, mode="a", index=False, header=False)
     else:
        df.to_csv(FileName, index=False)

        
        
        


