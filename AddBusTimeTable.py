# ---------- import modules ----------
import os                     # Used to check file existence and clear the terminal screen
import pandas as pd           # Used to read and write CSV files
import datetime               # Used to validate time format (HH:MM)




# ---------- create class ----------
class AddBusTimeTable:
    def __init__(self):
        pass                  # Constructor exists but no initialization needed right now
    
    
    

    # ---------- clear() method ----------
    def clear(self):
        # Clears the terminal screen for better UI
        # Uses 'cls' for Windows and 'clear' for Mac/Linux
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
        

    # ---------- method to add bus timetable ----------   
    def AddBusTimetable(self):
        self.clear()          # Clear screen at the start of the method
        print("\n🚌 ADD NEW BUS TIMETABLE")   # Heading for admin

        FileName = "TimeTable.csv"    # CSV file where timetable is stored



       # load or create CSV 
        if os.path.exists(FileName):          # Check if timetable file exists
            df = pd.read_csv(FileName)        # Load existing timetable
        else:
            # If file does not exist, create a new DataFrame with required columns
            df = pd.DataFrame(columns=["BusNumber", "Stop", "Time"])



        # main input loop 
        PendingDetails = True                 # controls whether admin keeps adding data
        while PendingDetails:

            # ---------- ask for bus number ----------
            bus = input("\nEnter Bus Number (e.g., NCTX 1): ").strip()  # Take bus number input
            
            
            if not bus:                       # check if input is empty
                print("⚠ Bus number cannot be empty.")
                continue                     # restart loop


            # ask for bus stop
            stop = input("Enter Stop Name: ").strip()   # take stop name input
            
            if not stop:                     # check if input is empty
                print("⚠ Stop cannot be empty.")
                continue                     # restart loop


            
            # ask for bus time with validation 
            ValidInput = True
            while ValidInput:
                TimeValue = input(
                    "Enter Time (HH:MM, e.g., 14:30): "
                ).strip()                    # take time input

                try:
                    # validate time format using datetime
                    datetime.datetime.strptime(TimeValue, "%H:%M")
                    ValidInput = False       # valid time then exit loop
                except ValueError:
                    # runs if time format is invalid
                    print("⚠ Invalid time format. Please enter time as HH:MM (24-hour format).")
                    
                    if not TimeValue: #Prevent empty entry 
                        print("⚠ Time cannot be empty.") 
                        continue
                        
                    


            # show preview of entered data 
            print("\nYou are about to add:")
            print(f"  Bus   : {bus}")        # display bus number
            print(f"  Stop  : {stop}")       # display stop name
            print(f"  Time  : {TimeValue}")  # display time
            
            


            # confirm save 
            ValidInput = True
            while ValidInput:
                confirm = input(
                    "\nSave this timetable? (y/n): "
                ).strip().lower()            # ask admin for confirmation

                
                if confirm in ("y", "yes"):
                    # add new row to DataFrame
                    df.loc[len(df)] = [bus, stop, TimeValue]
                    # save DataFrame back to CSV
                    df.to_csv(FileName, index=False)
                    print("✔ Timetable entry added successfully!")
                    ValidInput = False       # exit confirmation loop

                elif confirm in ("n", "no"):
                    print("❌ Entry discarded.")
                    ValidInput = False       # exit confirmation loop

                else:
                    print("⚠ Please type only y or n.")
                    


            
            # ---------- ask if admin wants to add more ----------
            AddMore = True
            while AddMore:
                more = input(
                    "\nDo you want to add another timetable? (y/n): "
                ).strip().lower()            # ask admin choice

                
                
                
                if more in ("y", "yes"):
                    AddMore = False          # go back to main loop
                elif more in ("n", "no"):
                    print("\nReturning to admin menu...")
                    return                  # exit function completely
                else:
                    print("⚠ Please type only y or n.")
