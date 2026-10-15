#---------- import modules ---------
import pandas as pd                    # import pandas for reading/writing CSV files
import os                              # import os to check whether files exist




# ----------- create class ---------
class ViewLoggedInUserManager:
    def __init__(self):
        self.users_file = "LoggedInUsers.csv"         #define file path

    
    
    
    # ----------- method to clear terminal ----------  
    def clear(self):
        # clear the terminal screen (Windows uses 'cls', Mac/Linux uses 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')   




    # --------- method to pause -----------
    def pause(self):
        # wait for the user to press Enter before continuing
        input("\nPress Enter to continue...")              


    
    
    # ---------- method to view loggedIn users
    def ViewLoggedInUsers(self):
        self.clear()                               # clear terminal
        print("\n🔓 LOGGED-IN USERS\n")

        
        
        if not os.path.exists(self.users_file):    # check existance of file
            print("No active sessions.")
        else:
            df = pd.read_csv(self.users_file)
            print(df)

        self.pause()                               # paused
