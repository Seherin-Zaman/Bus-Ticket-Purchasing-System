# ---------- import modules ----------
import os                                     # import os to check whether files exist
import pandas as pd                           # import pandas for reading/writing CSV files



# --------- create class ----------
class ChangePriceManager:
    def __init__(self):
        pass   # No setup needed yet

    


# ----------- method for changing price ----------    
    def ChangePrice(self):
      print("\n💷 CHANGE TOPUP PRICE")

      FileName = "mobile_products.csv"     # CSV file storing product data

      
      
      if not os.path.exists(FileName):     # checked existance of file
        print("❌ File not found!")
        return

      
      
      
      
      df = pd.read_csv(FileName)           # loaded CSV file into DataFrame

      # If there are no rows, nothing to update
      if df.empty:
        print("⚠ No products to update.")
        return

      
      # show products to admin
      print("\n📦 Available Topups:")
      
      
      # display column of price alongside 2 columns to understand
      print(df[['topup_id', 'topup_title', 'topup_price_in_pence']].to_string(index=False))

      
      
      # asked for valid topup ID
      ValidInput = True
      while ValidInput:
        topup_id = input("\nEnter Topup ID to change price: ").strip()

        
        
        # Filter dataframe where id matches
        matches = df[df["topup_id"] == topup_id]

        
        
        
        
        # If nothing matches — handle gracefully
        if matches.empty:
            print("❌ Topup ID not found.")

            
            
            # Ask admin if they want to retry
            PendingEntry = True
            while PendingEntry:
                again = input("Try another Topup ID? (y/n): ").strip().lower()

                
                
                if again in ("y", "yes"):
                  PendingEntry = False           # go back & ask again
                elif again in ("n", "no"):
                    print("Returning to admin menu...")
                    return                       # exit completely
                else:
                    print("⚠ Please type only y or n.")

            
            continue                 # restart outer loop

        else:
            break                    # valid ID found → continue

      
      
      
      
      # shwed current details
      row_index = matches.index[0]   # get actual dataframe index for editing

      print("\nCurrent Topup:")
      print(matches[['topup_title', 'topup_price_in_pence']])

      
      
      
      # asked for new price
      ValidInput = True
      while ValidInput:
        new_price_text = input("\nEnter NEW price in pence (e.g., 29900): ").strip()
        try:
            new_price = int(new_price_text)   # convert input to integer

            # price must be positive
            if new_price <= 0:
                raise ValueError

            ValidInput = False

        except ValueError:
            print("⚠ Please enter a valid positive integer.")

      
      
      
      
      # confirm update
      ValidInput= True
      while ValidInput:
        confirm = input(f"\nConfirm change price to {new_price} pence? (y/n): ").strip().lower()

        
        
        if confirm in ("y", "yes"):
            # Update dataframe value
            df.at[row_index, "topup_price_in_pence"] = new_price

            
            # Save file back to CSV
            df.to_csv(FileName, index=False)

            
            print("✔ Price updated successfully!")
            return

        
        
        elif confirm in ("n", "no"):
            print("❌ No changes made.")
            return

        
        else:
            print("⚠ Please type only y or n.")

