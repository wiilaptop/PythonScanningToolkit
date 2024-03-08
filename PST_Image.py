# Created with love from Texas by Wiilaptop
from typing import Any
from exif import Image

#This is the Metadata module for use in the Python Scanning Toolkit.

class MetadataImage():
    def __init__(self, WorkingImage):
        self.Image = WorkingImage

    def ViewParamaters(self, WorkingImage):

        #Puts every attribute into a list and sorts them.
        commonMems = set(list(dir(WorkingImage)))
        commonMemsSorted= sorted(commonMems)
        return commonMemsSorted
