# ---------- import modules ----------
import os                  # work with files, paths, and system commands
import sys                 # access system-level I/O
import pandas as pd        # read/write CSV files
import time                # create loading delays

# ---------- function for displaying dots while typing info ----------
# 'nt' means Windows system
if os.name == "nt":
    import msvcrt          # module to read keyboard input without showing it

    def DotInput(prompt):
        print(prompt, end="", flush=True)   # print prompt and stay on same line
        value = ""                          # store the typed text here
        ValidInput = True                   # loop control

        while ValidInput:                   # keep reading until Enter is pressed
            ch = msvcrt.getch()             # read one key

            if ch in {b"\r", b"\n"}:        # user pressed Enter
                print()                     # move to next line
                ValidInput = False          # stop loop

            elif ch == b"\x08":             # user pressed Backspace
                if value:                   # only delete if something exists
                    value = value[:-1]      # remove last character
                    print("\b \b", end="", flush=True)  # visually erase dot

            elif ch == b"\x03":             # Ctrl + C pressed
                raise KeyboardInterrupt     # stop program

            else:
                value += ch.decode()        # add typed character to value
                print(".", end="", flush=True)  # show dot instead of character

        return value                        # return the hidden value

else:
    # Mac/Linux handling
    import tty, termios

    def dot_input(prompt):
        print(prompt, end="", flush=True)
        value = ""
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)    # read keypress raw mode
            ValidInput = True
            while ValidInput:
                ch = sys.stdin.read(1)

                if ch in ("\r", "\n"):     # Enter key
                    print()
                    ValidInput = False
                elif ch == "\x7f":         # Backspace key
                    if value:
                        value = value[:-1]
                        print("\b \b", end="", flush=True)
                else:
                    value += ch            # store character
                    print(".", end="", flush=True)

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return value   # return the hidden value



# ---------- User authentication manager ----------
class ConfidentialInfoManager:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.users_file = os.path.join(base_dir, "RegisteredUsers.csv")
        self.sessions_file = os.path.join(base_dir, "LoggedInUsers.csv")

        if not os.path.exists(self.users_file):
            pd.DataFrame(
                columns=["Username", "Email", "Password"]
            ).to_csv(self.users_file, index=False)

        if not os.path.exists(self.sessions_file):
            pd.DataFrame(
                columns=["LoggedUser"]
            ).to_csv(self.sessions_file, index=False)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')    # clear terminal

    def loading(self, text):
        for i in range(3):
            print(f"{text} {'.'*(i+1)}")                   # show loading text
            time.sleep(0.2)                                # wait slightly
            self.clear()                                   # clear screen again

    # ---------- Register ----------
    def register(self):
      print("\n📝 REGISTER ACCOUNT")

      username = DotInput("Create username: ").strip().lower()
      email = DotInput("Enter email: ").strip().lower()
      password = DotInput("Create password: ").strip()

      df = pd.read_csv(self.users_file)

      if username in df["Username"].str.lower().str.strip().values:
        print("\n❌ This username already exists. Please login instead.")
        return False

      new_user = pd.DataFrame([[username, email, password]],
                            columns=["Username", "Email", "Password"])

      df = pd.concat([df, new_user], ignore_index=True)
      df.to_csv(self.users_file, index=False)

      print("\n✔ Registration successful!")
      return True

    # ---------- Login ----------
    def login(self):
        print("\n🔐 LOGIN")
        ValidInput = True

        while ValidInput:                                 # keep asking until correct
            username = DotInput("Username: ")            # hidden username
            password = DotInput("Password: ")            # hidden password

            df = pd.read_csv(self.users_file)             # load users

            # checking match
            match = df[(df["Username"].str.lower() == username.lower().strip()) &
                       (df["Password"] == password)]

            if not match.empty:                           # login success
                self.log_session(username)                # store session
                self.loading("Logging In")
                print("\n✔ Login verified!")
                CurrentUser = username                    #save username in a variable
                return CurrentUser                        # return logged-in user

            else:
                print("\n❌ Wrong username or password — try again.\n")   #prints prompt if details is incorrect

    # ---------- Log session ----------
    def log_session(self, username):
        df = pd.read_csv(self.sessions_file)              # load session file
        df.loc[len(df)] = [username]                      # add user to bottom
        df.to_csv(self.sessions_file, index=False)        # save file again
