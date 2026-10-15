# ---------- import modules ---------
import pandas as pd                    # import pandas for reading/writing CSV files
import os                              # import os to check whether files exist



# --------- create class ---------
class BusDetailsManager:                           # define a class to manage bus/mobile product details
    def __init__(self, file_name="mobile_products.csv"):
        self.file_name = file_name                 # Store the CSV filename when the class is created
        
        
        
# ---------- method for adding details -----------
    def AddDetails(self):
        # Check whether the CSV file exists
        if not os.path.exists(self.file_name):
            print("❌ File not found!")
            return    # Stop function if file not found
        
        
        
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(self.file_name)

        print("\n🚌 ADD NEW BUS DETAILS")
        print("\nAvailable columns:\n")

        
        
        # Display the list of available column headers with numbering
        for i, col in enumerate(df.columns, start=1):
            print(f"{i}. {col}")

        
        
        # Create an empty dictionary (new row) with all columns set to blank initially
        new_row = {col: "" for col in df.columns}

        
        
        # Loop to allow entering values in multiple columns
        PendingTakingColumn = True
        while PendingTakingColumn:
            col_name = input(
                "\n👉 Type the column name you want to add data to "
                "(or type 'done' to finish): "
            ).strip()                 # Ask admin for column name & remove spaces

            
            
            # If admin types "done", exit the loop
            if col_name.lower() == "done":
                PendingTakingColumn = False

            
            
            # Validate the column name
            if col_name not in df.columns:
                print("⚠️ Invalid column name. Please choose exactly as shown.")
                continue              # Ask again if wrong name given

            
            
            # Ask for the value for that column
            value = input(f"Enter value for '{col_name}': ").strip()
            new_row[col_name] = value   # Store entered value in the dictionary

        
        
        print("\n📄 New entry preview:")
        print(new_row)                 # Show the gathered data before saving

        
        
        # Confirm before saving into the CSV file
        ValidInput = True
        while ValidInput:
            confirm = input("\nSave this record? (y/n): ").lower()

            # If user confirms "yes"
            if confirm == "y":
                df.loc[len(df)] = new_row     # Add new row to dataframe
                df.to_csv(self.file_name, index=False)  # Save dataframe to CSV
                print("\n✅ Record added successfully!")
                ValidInput = False

            # If user cancels
            elif confirm == "n":
                print("\n❌ Cancelled. Record not saved.")
                ValidInput = False

            # If neither y nor n
            else:
                print("Please type y or n.")

