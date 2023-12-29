import exif
"""
Created by Wiilaptop
EXIF Class

Objective: Processes changes done through the Exif package in the main program. 
"""
class ExifChange(): #Class to change the attribute
    def __init__(self,WE,UE,UC): #Declares variables for (WorkingimagE), (UserEdit), and (UserChange) - all variables used in the main program and named similarly for readability.
        self.WE = WE
        self.UE = UE
        self.UC = UC
 
    def ChangeAttribute(self,WE,UE,UC):
        setattr(WE, UE, UC) #Setattribute to call the variable that is the same name as the function in exif - allowing the user to change it
        print (f"The {UE} attribute is now: ", getattr(WE, UE)) #Ensures the daata was changed by calling the attribute again through the package for the user.

class ExifGet(): #Class to get the attribute - different class is used since only 2 variables are used for this as compared to the three needed above.
    def __init__(self, WE, UE):
        self.WE = WE
        self.UE = UE

    def GetAttribute(self, WE, UE):
        print (f"The {UE} attribute is: ", getattr(WE, UE)) #Similar line as above, but only uses two paramaters. 
