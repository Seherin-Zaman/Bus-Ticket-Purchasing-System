# ---------- import modules ----------
import os                                     # import os to check whether files exist
import pandas as pd                           # import pandas for reading/writing CSV files



# ------------ create class ----------
class ChangeBusTimeTableManager:
    def __init__(self):
        pass                                  # Constructor kept empty — no setup needed yet

    
    
# ----------- method for changing bus timetable ---------
    def ChangeBusTimetable():
        FileName = "TimeTable.csv"            # CSV that stores timetable
        df = pd.read_csv(FileName)            # Load timetable into DataFrame
        
        

        print("\n🚌 CHANGE BUS TIMETABLE")

        # ---------- take bus number ----------
        ChangeTime = True
        while ChangeTime:
            bus = input("Enter Bus Number to change (e.g., NCTX 1): ").strip()

            # Filter rows that match the given bus number
            matches = df[df["BusNumber"].astype(str) == bus]

            
            # If no bus exists with that number
            if matches.empty:
                print("\n❌ This bus is not in our service.")

                
                
                # Ask admin if they want to try again
                TryAgain = True
                while TryAgain:
                    again = input("Do you want to try another bus? (y/n): ").strip().lower()

                    if again in ("y", "yes"):
                        TryAgain = False               # Ask for bus again
                    elif again in ("n", "no"):
                        print("Returning to admin menu...")
                        return                         # Exit function
                    else:
                        print("⚠ Please type only y or n.")

                
                
                continue                    # restart main loop

            
            
            ChangeTime = False              # valid bus found — exit loop

        
        
        # show existing timetable 
        print("\nExisting timetable entries:")
        print(matches.reset_index())         # Reset index so admin sees simple 0,1,2...

        
        
        
        # ---------- CONFIRM CHANGE ----------
        ValidInput = True
        while ValidInput:
            confirm = input("\nDo you want to change this timetable? (y/n): ").strip().lower()

            
            if confirm in ("y", "yes"):
                ValidInput = False                      # continue to editing
            elif confirm in ("n", "no"):
                print("No changes made. Returning...")
                return                                  # exit function
            else:
                print("⚠ Please type only y or n.")

        
        
        
        # ---------- SELECT WHICH ROW TO EDIT ----------
        ValidInput = True
        while ValidInput:
            try:
                # Ask admin which row (index from printed table)
                row_index = int(input("\nEnter index of the row to modify: "))

                # Convert printed index back to real dataframe index
                real_index = matches.index[row_index]
                ValidInput = False  #exit loop

            except (ValueError, IndexError):
                print("❌ Invalid index — please choose one from the table.")

        
        
        
        
        # took and stripped new values
        new_stop = input("New Stop (leave blank to keep): ").strip()
        new_time = input("New Time (leave blank to keep): ").strip()

        
        # only overwrite if user typed something
        if new_stop:
            df.at[real_index, "Stop"] = new_stop

        if new_time:
            df.at[real_index, "Time"] = new_time

        
        
        
        # save changes
        df.to_csv(FileName, index=False)

        print("\n✔ Timetable updated successfully!")

