# ---------- imported the modules ----------
import pandas as pd          # Used for reading and processing CSV data
import time                  # Used to add a short delay for better user experience


# ----------- TopupEntitlementStartDateManager ----------
class TopupEntitlementStartDateManager:
    def __init__(self, csv_file):
        
        self.csv_file = csv_file                 # Store CSV file path
        self.df = pd.read_csv(csv_file)          # Load CSV file into a DataFrame

        # Convert 'topup_entitlement_start_date' column to datetime format once
        # Invalid or missing values are converted to NaT
        self.df["topup_entitlement_start_date"] = pd.to_datetime(
            self.df["topup_entitlement_start_date"],
            errors="coerce",
            utc=True
        )


    
    
    
    # ----------- ShowTopupEntitlementStartDate() ----------
    def ShowTopupEntitlementStartDate(self, SelectedTopup):
        
        
        # Filter the DataFrame for the selected top-up
        SpecificTopup = self.df[self.df["topup_title"] == SelectedTopup]

        # If the selected top-up does not exist
        if SpecificTopup.empty:
            print("\n🎁 Topup Entitlement Start Date & Time")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Start date not available for this topup.")
            return

        
        # Extract the entitlement start date
        start_date = SpecificTopup["topup_entitlement_start_date"].iloc[0]

        
        
        # If the start date is missing or invalid
        if pd.isna(start_date):
            print("\n🎁 Topup Entitlement Start Date & Time")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("Start date not available for this topup.")
            return


        # ----------- Format date and time -----------
        formatted_date = start_date.strftime("%d %B %Y, %I:%M %p")

        
        # Display the formatted start date
        print("\n🎁 Topup Entitlement Start Date & Time")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Start Date: {formatted_date}")

        # Short delay for improved user interface experience
        time.sleep(0.3)

        return formatted_date
