from InquirerPy import inquirer
import time
def main():
    command_check = False
    while command_check == False:
        choice = inquirer.text(message="Do you want to find an address? [Y/N]").execute()
        if choice == "Y":
            address = inquirer.text(message="Give me a House Number:", completer={
                "5502 Reagan Ave, Rochester, New York": None,
                "6028 Carter Blvd, Rome, Florida": None,
                "7708 SW Bull CT, Austin, Texas": None,
                "1229 SE Kramer St, Salt Lake City, Nevada": None}, multicolumn_complete=True).execute()
            print(address)
            command_check = True
        elif choice == "N":
            print("Oh, okay then. Have a good day")
            command_check = True
        else:
            time.sleep(1)
            print("Please type the right command!")
            

main()
