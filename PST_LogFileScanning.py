#Made with love from Texas by Wiilaptop

#Module for PST for scanning and reading log files.

class LogFileClass():

    #Initalizing variables to be used within the class.
    def __init__(self, currentLine, searchWords):
        self.currentLine = currentLine
        self.searchWords = searchWords

    #Function for scanning any word in the line.
    #If the current line finds the word BEFORE the end of the line (-1 index), return True.
    def anyWordScan(self, currentLine, searchWords):
        for word in searchWords:
            if currentLine.find(word) != -1:
                return True
    
    #List comprehension for scanning every word in the current line to see if it matches the words in the searchWords list.
    def allWordScan(self, currentLine, searchWords):
        if all(x in currentLine for x in searchWords):
            return True