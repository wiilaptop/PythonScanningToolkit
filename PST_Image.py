# Created with love from Texas by Wiilaptop
from typing import Any
from exif import Image

#This is the Metadata module for use in the Python Scanning Toolkit.

class MetadataImage():
    def __init__(self, WorkingImage):
        self.Image = WorkingImage

    def ViewParamaters(self, WorkingImage):
        commonMems = set(list(dir(WorkingImage))) #puts every attribute into a list and sorts them
        commonMemsSorted= sorted(commonMems)
        return commonMemsSorted

class ExifGet():
    def __init__(self, WE, UE):
        self.WE = WE
        self.UE = UE
    
    def getattribute(self, WE, UE):
        pass