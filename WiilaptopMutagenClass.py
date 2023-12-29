import mutagen
"""
Jayden Bou-Quraiss
Mutagen Class

Objective = Use the functionality of the main program's menu system to create a dynamic metadata system.
"""

class MutagenClass(): #Mutagen class to handle the three variables that are passed through it.
    def __init__(self, UserChange, UserEdit, UserFile):
        self.UC = UserChange
        self.UE = UserEdit
        self.UF = UserFile

    def MutaChange(self, UserChange, UserEdit, UserFile):
            UserFile.tags[UserEdit] = UserChange #Since mutagen uses the .tags function, by parsing the UserEdit variable (the variable that contains the attribute to change) you set it to UserEdit.
            #This works as (User's File).tags [change this attribute given by user] = assign this value given by user.
