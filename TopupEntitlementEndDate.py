# ---------- imported modules ----------
import pandas as pd          # Used for reading and manipulating CSV data
import time                  # Used to add a short delay for better UI experience


# ----------- TopupEntitlementEndDateManager ----------
class TopupEntitlementEndDateManager:
    def __init__(self, csv_file):
    
        self.csv_file = csv_file                 # Store CSV file path
        self.df = pd.read_csv(csv_file)          # Read CSV into DataFrame

        
        # Convert 'topup_entitlement_end_date' column to datetime format once
        # Invalid or missing values will be converted to NaT
        self.df["topup_entitlement_end_date"] = pd.to_datetime(
            self.df["topup_entitlement_end_date"],
            errors="coerce",
            utc=True
        )


    # ----------- ShowTopupEntitlementEndDate() ----------
    def ShowTopupEntitlementEndDate(self, SelectedTopup):
        

        # Filter the DataFrame for the selected top-up
        SpecificTopup = self.df[self.df["topup_title"] == SelectedTopup]

        # If the top-up does not exist
        if SpecificTopup.empty:
            print("\n🎁 Topup Entitlement End Date & Time")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("End date not available for this topup.")
            return

        
        # Extract the entitlement end date
        end_date = SpecificTopup["topup_entitlement_end_date"].iloc[0]

        
        
        # If the end date exists but is invalid or missing
        if pd.isna(end_date):
            print("\n🎁 Topup Entitlement End Date & Time")
            print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
            print("End date not available for this topup.")
            return


        # ----------- Format date and time -----------
        formatted_date = end_date.strftime("%d %B %Y, %I:%M %p")

        # Display the formatted end date
        print("\n🎁 Topup Entitlement End Date & Time")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"End Date: {formatted_date}")

        # Small delay for better user experience
        time.sleep(0.3)

        return formatted_date

