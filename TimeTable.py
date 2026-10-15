# ---------- import modules ----------
import pandas as pd
import os



# --------- created class for timetable ----------
class BusTimetable:
    def __init__(self, FileName="TimeTable.csv"):
        self.FileName = FileName



# ---------- method to view timetable ----------
    def ViewTimeTable(self):
        print("\n🚌 VIEW BUS TIMETABLE")

        # checking the existance of file
        if not os.path.exists(self.FileName):   
            print("❌ Timetable is not available.")
            return

        df = pd.read_csv(self.FileName)  #read the csv file
        bus = input("\nEnter bus number (e.g., NCTX 45): ").strip() #asking for the bus number
        results = df[df["BusNumber"].str.lower() == bus.lower()] #searching the bus number
        
        #if no match s found
        if results.empty: 
            print("\n❌ No timetable found for that bus.")
            return

        #print statement
        print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"⏰ Timetable for {bus}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        # printing the stop and time
        for _, row in results.iterrows():
            print(f"Stop : {row['Stop']}")
            print(f"Time : {row['Time']}")
            print("———————————————")

