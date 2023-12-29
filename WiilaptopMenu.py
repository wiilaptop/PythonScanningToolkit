"""
Created by Wiilaptop
Menu Frame Class

Purpose: Allows for every menu in the program to have the same file and adaptable to different options.
"""

class MenuClass():
    def __init__(self):
        pass

    def GetMenuChoice(self, MO):
        MenuNum=0
        for MenuItem in MO:
            MenuNum+=1
            print (f"{MenuNum}. {MenuItem}")
        while True:
            try:
                MenuChoice = int(input(f"Enter choice between 1 and {MenuNum}: "))
                if (MenuChoice >= 1) and (MenuChoice <= MenuNum):
                    break
            except ValueError:
                pass
        return (MO[MenuChoice-1])
