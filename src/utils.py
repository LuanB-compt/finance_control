import os
from Finance import Finance



def title(os_:str) -> None:
    """
    Clean the terminal with 'cls' (windows) or 'clear' (linux) and show the program title.
    ------------------------
    Parameters:
    os_: Operational System that will runing the program
    """
    if os_.upper() == "WINDOWS":
        os.system("cls")
        print("***********************************")
        print("        LUAN FINANCE CONTROL")
        print("***********************************\n")
        print(Finance.importance)
    elif os_.upper() == "LINUX":
        os.system("clear")
        print("***********************************")
        print("        LUAN FINANCE CONTROL")
        print("***********************************\n")
        print(Finance.importance)