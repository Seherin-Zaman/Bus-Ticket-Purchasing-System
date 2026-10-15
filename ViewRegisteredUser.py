# ---------- import modules ---------
import pandas as pd                    # import pandas for reading/writing CSV files
import os                              # import os to check whether files exist
import time



# ----------- create class ------------
class ViewRegisteredUserManager:
    def __init__(self):
        # set the path/name of the CSV file that stores registered user data
        self.users_file = "RegisteredUsers.csv"    
        
                


    # ----------- method to clear terminal ----------  
    def clear(self):
        # clear the terminal screen (Windows uses 'cls', Mac/Linux uses 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')   
        
        
        
        

    # --------- method to pause -----------
    def pause(self):
        # wait for the user to press Enter before continuing
        input("\nPress Enter to continue...")              




    # ---------- method for viewing registered users ----------
    def ViewRegisteredUsers(self):
        self.clear()                                       # clear the screen before showing data
        print("\n👥 REGISTERED USERS\n")                  # print heading text

        
        # check whether the CSV file exists
        if not os.path.exists(self.users_file):
            print("No registered users found.")            # print if the file doesn't exist
        else:
            df = pd.read_csv(self.users_file)              # read user data from CSV into a DataFrame

            if df.empty:                                   # checked if there are no rows in the CSV
                print("No users yet.")                     # print if file is empty
            else:
                print(df)                                  # print the table of users to the screen

        
        self.pause()                                       # pause so the user can read the output

