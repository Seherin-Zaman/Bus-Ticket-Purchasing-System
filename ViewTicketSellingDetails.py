# ---------- import modules ---------
import pandas as pd                    # import pandas for reading/writing CSV files
import os                              # import os to check whether files exist



# ---------- create class ----------
class ViewTicketSellingDetailsManager:
    def __init__(self):
        self.users_file = "UserReceipts.csv"               # set the path/name of the CSV file that stores ticket receipts

    
    
  
  # ----------- method to clear terminal ----------  
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')   # clear terminal screen (works on Windows and Mac/Linux)

    
    
    
    # --------- method to pause -----------
    def pause(self):
        input("\nPress Enter to continue...")              # pause program until user presses Enter
    
    
    
    
    # ---------- method to view tciket selling details ----------
    def ViewTicketSellingDetails(self):
      self.clear()                                         # clear screen before displaying data
      print("\n🎟 TICKET SALES REPORT\n")                  # print report heading

      
      
      if not os.path.exists(self.users_file):              # checking existance of file
        print("No ticket sales yet.")                      # print if file is missing
        self.pause()                                       # pause so user can read message
        return                                             # exit the method

      
      
      df = pd.read_csv(self.users_file)                    # read all ticket data from CSV into a DataFrame

      
      
      if df.empty:                                         # check if the CSV file is empty
        print("No ticket sales yet.")                      # print for empty file
        self.pause()                                       # pause program
        return                                             # exit the method

      
      
      #  loop through all rows in reverse order (latest sale first)
      for _, row in df.iloc[::-1].iterrows():              # iterate over each ticket sale record, reversed
        
        
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━") 
        print(f"    🧾 Ticket Details ")                   # print section header
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        
        
        
        
        print(f"  UserName    :  {row['UserName']}")       # Display username
        print(f"  Category    :  {row['Category']}")       # Display ticket category
        print(f"  Topup Title :  {row['Topup Title']}")    # Display top-up type
        print(f"  Price       :  £{row['Price']}")         # Display ticket price
        print(f"  Class       :  {row['Class']}")          # Display travel class
        print(f"  Quantity    :  {row['Quantity']}")       # Display number of tickets purchased
        print(f"  Start Date  :  {row['Start Date']}")     # Display starting date
        print(f"  End Date    :  {row['End Date']}")       # Display ending date
        
      
      
      # pause only after all rows have been shown
      self.pause()                                         # Wait so user can review the report
