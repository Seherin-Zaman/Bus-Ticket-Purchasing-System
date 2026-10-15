# ---------- import module ---------
import os                           # the operating system (clear screen)
import time                         # used for loading animation delays274aKo0##&##
from AdminMenu import AdminMenu




# ---------- function for displaying dots while typing info ----------
# 'nt' means Windows system
if os.name == "nt":                   # check if program is running on Windows
    import msvcrt                     # module to read keyboard input secretly (without showing text)

    def DotInput(prompt):
        print(prompt, end="", flush=True)       # show prompt and stay on same line
        value = ""                              # stores what the user types
        ContinueTyping = True                   # controls the loop

        while ContinueTyping:                       # keep looping while user types
            ch = msvcrt.getch()                     # read a single key press

            if ch in {b"\r", b"\n"}:        # if ENTER is pressed
                print()                     # move to next line
                ContinueTyping = False      # stop loop

            elif ch == b"\x08":                           # if BACKSPACE key pressed
                if value:                                 # only delete if there is something
                    value = value[:-1]                    # remove last character from value
                    print("\b \b", end="", flush=True)    # visually remove dot

            elif ch == b"\x03":             # Ctrl + C (exit program)
                raise KeyboardInterrupt     # stop program immediately

            else:
                value += ch.decode()                 # add typed key to the value
                print(".", end="", flush=True)       # show dot instead of real character

        return value                        # send back the hidden text
    

else:   # ---------- Mac / Linux version ----------
    import tty, termios                     # libraries to control terminal input
    

    def dot_input(prompt):
        print(prompt, end="", flush=True)           # show prompt text
        value = ""                                  # store typed characters
        fd = sys.stdin.fileno()                     # file descriptor of terminal
        old_settings = termios.tcgetattr(fd)        # save current terminal settings
        
        

        try:
            tty.setraw(fd)                     # switch to raw mode (read char by char)
            ContinueTyping = True
            while  ContinueTyping:             # read until ENTER
                ch = sys.stdin.read(1)

                if ch in ("\r", "\n"):      # when ENTER pressed
                    print()
                    ContinueTyping= False

                elif ch == "\x7f":          # backspace key
                    if value:
                        value = value[:-1]  # remove last char
                        print("\b \b", end="", flush=True)

                else:
                    value += ch                        # store typed character
                    print(".", end="", flush=True)     # show dot instead

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)    # restore terminal settings

        return value                     # return full hidden text
    
    


# --------- create class for access verifying --------
class AdminPanel:
    def __init__(self):
        self.AdminUsername = "@dmin@"       # fixed admin username
        self.AdminPassword = "27@@&@@13" # fixed admin password
        
        
        

# --------- method for clearing terminal ---------
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # clear terminal based on OS
        
 
 # -------- method for loading effect ---------       
    def loading(self, text):
        for i in range(3):                                  # repeat 3 times
            print(f"{text} {'.'*(i+1)}")                    # show text with dots
            time.sleep(0.2)                                 # short pause
            self.clear()                                    # clear screen
            
            
            

# --------- method for checking login details ---------
    def login(self):
        print("""
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
      🚌 BUS TICKET APP
  ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛  """)     #print a welcome message and options
       
        print("\n🛡️  ADMIN LOGIN")                               # title text
        
        ValidInput = True                                         # loop controller
        while ValidInput:                                         # keep asking until correct
            username = DotInput("Admin Username: ").strip()       # secure username entry
            password = DotInput("Admin Password: ")               # secure password entry
            
            self.loading("Verifying")                             # show loading animation

            if username == self.AdminUsername and password == self.AdminPassword:
                self.clear()                                      # clean screen
                print("✔ Access granted — Welcome, Admin!")       # success message
                ValidInput = False                                # stop loop
                                                                  # notify login success
            else:
                print("\n❌ Incorrect admin credentials. Try again.\n")
                time.sleep(1.2)                   #to delay
                self.loading("Processing")        # for loading effect
                # loop continues automatically
        
        
        

# --------- create admin object ---------
admin = AdminPanel()
admin.login()



# ---------- call login — only enters dashboard if login returned True ----------
#if admin.login():
    #print()
menu = AdminMenu()
menu.show_menu()

