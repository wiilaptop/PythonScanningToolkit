"""
Created by Wiilaptop
"A Python Scanning Toolkit"
V 1.0.0
"""
from WiilaptopMenu import MenuClass
from WiilaptopNetInterfaces import NetInfoClass
from WiilaptopHTMLScraping import HTMLScrape
from WiilaptopPortScanner import PortScanner
from WiilaptopExif import *
import time

def main():
    while True:
        print (f"\n\nWelcome to the Main Menu.")

        #Creating the Top Level Menu for the user.
        TopLevelMenu = MenuClass()
        TopLevelChoice = TopLevelMenu.GetMenuChoice(["HTML Scraping","Forensic Tools","Scan Tools", "Quit"])
        print (f"Selected Option: {TopLevelChoice}")

        #All of the Top Level Menu Options for the HTML Scraping Option
        if (TopLevelChoice == "HTML Scraping"):
            ScrapingMenu = MenuClass()
            ScrapMenuChoice = ScrapingMenu.GetMenuChoice(["[Original] Scrape HTTP sites for any contact information","HTTPS Scraping", "Quit"])
            print (f"Selected Option: {ScrapMenuChoice}")

            if (ScrapMenuChoice == "[Original] Scrape HTTP sites for any contact information"):
                HTMLScrapingOriginal()
            if (ScrapMenuChoice == "HTTPS Scraping"):
                HTMLScraping2()
            if (ScrapMenuChoice == "Quit"):
                print (f"Returning to Main Menu!")
        
        # All of the Top Level Menu Options for the Forensic Tools
        if (TopLevelChoice == "Forensic Tools"):
            ForensicsMenu = MenuClass()
            ForensicsChoice = ForensicsMenu.GetMenuChoice(["Change Metadata of Image","Change Metadata of Sound File","Quit"])
            print (f"Selected Option: {ForensicsChoice}")
            if (ForensicsChoice == "Change Metadata of Image"):
                MetaDataImage()
            if (ForensicsChoice == "Change Metadata of Sound File"):
                MetaDataSound()
            if (ForensicsChoice == "Quit"):
                print (f"Returning to Main Menu!")

        # All of the top level Menu Optons for the Scanning Tools
        if (TopLevelChoice == "Scan Tools"):
            ScanToolsMenu = MenuClass()
            ScanToolsChoice = ScanToolsMenu.GetMenuChoice(["Scan Ports","Scan Log Files","View Network Interfaces", "Quit"])
            print (f"Selected Option: {ScanToolsChoice}")
            if (ScanToolsChoice == "Scan Ports"):
                PortScannerRun()
            if (ScanToolsChoice == "Scan Log Files"):
                LogFileScanning()
            if (ScanToolsChoice == "View Network Interfaces"):
                NetworkInterfaces()
            if (ScanToolsChoice == "Quit"):
                print (f"Returning to Main Menu!")

        
        elif(TopLevelChoice == "Quit"):
            print (f"Thank you for using the program! Goodbyes from Wiilaptop!")
            exit(0)

def HTMLScrapingOriginal():
    page = input(f"Enter the webpage to browse: ")
    timeout = int(input(f"Enter a timeout: "))
    PageView = HTMLScrape(page, timeout)
    PageResults = PageView.HTMLConnect(page, timeout)
    print (PageResults)

def HTMLScraping2():
    #Creating a Menu using the Menu Class - Giving the user the option to scan one or multiple websites.
    MultipleWebsites = MenuClass()
    MultipleWebsitesChoice=MultipleWebsites.GetMenuChoice(["One Website","Multiple Websites"])
    WebsiteList = []

    #Setting the flag true or false depending on the decision
    if MultipleWebsitesChoice == "One Website":
        MultipleWebsites=False
    if MultipleWebsitesChoice == "Multiple Websites":
        MultipleWebsites=True
    
    #If MultipleWebsites was chosen, read the user file.
    if MultipleWebsites == True:
        WebsiteList = ReadUserFile()

    #While true statement for asking if the output will be saved to a file.
    while True:
        WriteToFile = input(f"Do you want to write the output to a file? (Y/n): ")
        if WriteToFile == "Y" or WriteToFile == "y":
            WriteToFile = True
            FileContents = []
            break
        if WriteToFile == "N" or WriteToFile == "n":
            WriteToFile = False
            break    

    #Creating the Menu for what to scrape.
    #Keeping track of 3 variables: Multiple Websites, Writing to file, and what is being scraped.
    print (f"Multiple Websites: {MultipleWebsites}, Writing to File: {WriteToFile}, now what are we scanning for?")
    HTMLScraping = MenuClass()
    HTMLScrapeChoice = HTMLScraping.GetMenuChoice(["Scrape for URLs","Scrape for e-mails", "Quit"])
    if (HTMLScrapeChoice == "Scrape for URLs"):
        UrlScrape = True
        EmailScrape = False
    if (HTMLScrapeChoice == "Scrape for e-mails"):
        EmailScrape = True
        UrlScrape = False
    if (HTMLScrapeChoice == "Quit"):     #If the user selected Quit, return to main menu.
        print (f"Returning to Main Menu!")
        return

    if MultipleWebsites == False:
        page = input(f"Enter the webpage to browse: ")
        WebsiteList.append(page) #If the user only reads one page, just add it to the website list and scan it.
    
    #The Scanning Code - ran no matter what the user picks, just adjusts itself based on if conditions.

    #For everypage in the WebsiteList...
    for page in WebsiteList: 
        if UrlScrape == True:   # if the user checked URL scraping, scan the page, throw the errors if needed, write to file.
            PageView = HTMLScrape(page, 0)
            PageResults = PageView.HTTPSUrls(page, 0)
            if PageResults == 0: print(f"No scheme applied. Perhaps you meant https://{page}?"); continue
            if PageResults == 1: print(f"There was a problem connecting to {page}. Continuing to next page."); continue
            for link in PageResults:
                if WriteToFile == True:
                    FileContents.append(f"{page}: {link}")
                print (f"{page}: {link}")
        if EmailScrape == True:
            PageView = HTMLScrape(page, 0)    #if the user checked Email scraping, scan the page, throw the errors, write to file.
            PageResults = PageView.HTTPSEmails(page, 0)
            if PageResults == 0: print(f"No scheme applied. Perhaps you meant https://{page}?"); continue
            if PageResults == 1: print(f"There was a problem connecting to {page}. Continuing to next page."); continue
            for email in PageResults:
                if WriteToFile == True:
                    FileContents.append(f"{page}: {email}")
                print (f"{page}: {email}")

    #After ALL information is gathered, write to the file.
    if WriteToFile == True:
        if UrlScrape == True:
            WriteUserFile(FileContents, "URLScan")
        if EmailScrape == True:
            WriteUserFile(FileContents, "EmailScan")
    print (f"Scan Complete")
    
def ReadUserFile():
    #Initalizing the website list as empty so new scans with different files don't add to a single list.
    WebsiteList = []
    while True:
        File = str(input(f"Enter the file that contains every website to scrape: "))

        #Reading the User's file but stripping it as it gets added to the Website list to avoid newline chars. (\n)
        try:
            FileLines = open(File, "r").readlines()
            break
        except FileNotFoundError:
            print (f"{File} wasn't found! Maybe it was misspelled, or in a different location?")

    for line in FileLines:
        WebsiteList.append(line.strip())
    return WebsiteList

def WriteUserFile(list, TypeOfScan):
    OutputFile = open(f"Wiilaptop{TypeOfScan}.txt", "w")
    for i in list:
        OutputFile.write(f"{i}\n")
    OutputFile.close()
    print (f"Written to file successfully!")

def NetworkInterfaces():
    GetNetworkInfo = NetInfoClass() #Running the Network Class
    Results = GetNetworkInfo.GetInterfaces() #Getting the list that is returned from the class with all of the information
    if Results == 0:
        print (f"An error occurred when attempting to retrive Interfaces.") #Error message if an exception is raised within the class.
    if Results == 1:
        print (f"Netifaces is not installed on this machine, or could not be accessed.")
        print (f"Refer to the README file on how to install netifaces.")

    NetInterfaceIndex = 0
    for ipaddress_desc_dict in Results: #for all the data in the list...
        NetInterfaceIndex += 1
        print (f"\n{NetInterfaceIndex}.")
        if ipaddress_desc_dict.get('addr','addr not found'): #If there's an "addr" value, print it
            print (f"IP Address: {ipaddress_desc_dict['addr']}")
        if ipaddress_desc_dict.get('netmask', 'netmask not found'):#If there's a "netmask" value, print it
            print (f"Netmask: {ipaddress_desc_dict['netmask']}")
        if ipaddress_desc_dict.get('broadcast', 'broadcast not found'): #If there's a "broadcast" value, print it
            print (f"Broadcast: {ipaddress_desc_dict['broadcast']}")

def ReadPortFile():
    PNDictionary = {}
    while True: #while true statement to catch invalid inputs
        try:
            UserPortFile = input(f"Enter the name of the .csv file that contains ports to scan: ") 
            PortFile = open(UserPortFile, "r") #Entering and reading ffile, with try except catching exceptions for invalid file names.
            AllLines = PortFile.readlines() 
            break
        except FileNotFoundError:
            print ("Invalid File Name / File not found!")
    for index in range (1, len(AllLines)): #For loop to read the entire file
        portInfo = []
        LineParts = AllLines[index].strip().split(",")  #These lines create the Dictionary by using a list to fill in the key:value pairs
        portInfo.append(LineParts[1])
        portInfo.append(LineParts[2])
        PNDictionary[int(LineParts[0])] = tuple(portInfo)
    print (f"File read. Num Ports = {len(PNDictionary)}") #Tells the user the number of ports found.
    return PNDictionary

def PortScannerRun(): 
    global IPA
    PortsFound=[]
    if IPA == "":
        IPA = input(f"Enter the IP address to scan for ports on: ")
    else:
        while True:
            UseOldIP = input(f"The previously used IP address was {IPA}, do you want to use it? (Y/n): ")
            if UseOldIP == "Y":
                break
            else:
                IPA = input(f"Enter the IP address to scan for ports on: ")
                break
    
    while True:
        try:
            print (f"Timeout values under 1.0 may not grab a connection in time.")
            TO = float(input(f"Enter a timeout (1, 1.5, 2):"))
            break
        except ValueError:
            print (f"Hmm. That didn't seem right. Please enter a float or integer!")

    print (f"\nHow would you like to scan the ports?")
    print (f"We can scan the ports without a file, but they will lack a description.")
    print (f"On the other hand, you can supply a csv file with a port's number, name, and description to scan as well.")
    print (f"A file demonstrating this is included in the .zip file.\n")
    PortScanningMenu = MenuClass()
    PortScanningChoice = PortScanningMenu.GetMenuChoice(["Scan Ports Only","Scan Ports from File", "Quit"])
    print (f"Selected Option: {PortScanningChoice}")
    if PortScanningChoice == "Scan Ports Only":
        TypeOfScan = "SoloScan"
        SoloScan = True
        FileScan = False
    if PortScanningChoice == "Scan Ports from File":
        PNDictionary = ReadPortFile()
        TypeOfScan = "PortFileScan"
        FileScan = True
        SoloScan = False
    if PortScanningChoice == "Quit":
        return

    if SoloScan == True:
        print(f"Specify what ports to scan - Ex. (5 through 500): ")
        begport = int(input(f"Enter the beginning port to scan: "))
        endport = int(input(f"Enter the ending port to scan: "))
        for port in range(begport, endport):
            print (f"IP: {IPA}, Scanning Port: {port}", end = "\r")
            PortScan = PortScanner(port, IPA, TO)
            Results = PortScan.Scanner(port, IPA, TO)
            if Results == 0:
                portscanned = (f"[+ PORT FOUND] Port {port} was open on {IPA}!")
                print (portscanned)
                PortsFound.append(portscanned)

    if FileScan == True:
        PortNumberList = list(PNDictionary.keys())
        PortNumberList.sort()
        for port in PortNumberList:
            print (f"IP: {IPA}, Scanning Port: {port}", end = "\r")
            PortScan = PortScanner(port, IPA, TO)
            Results = PortScan.Scanner(port, IPA, TO)
            if Results == 0:
                portscanned = (f"IP: {IPA}, Port: {port} is open! Name: {PNDictionary[port][0]}, Desc: {PNDictionary[port][1]}")
                PortsFound.append(portscanned)
    
    print (f"\nPort scanning on {IPA} complete!")

    PrintToFile = input(f"Do you want to append the results to a file? (Y/n): ")
    if PrintToFile == "Y":
        WritePortFile(PortsFound,TypeOfScan)

def WritePortFile(PortsFound,TypeOfScan): 
    OutputFile = open(f"Wiilaptop{TypeOfScan}.txt", "w")
    for i in PortsFound:
        OutputFile.write(f"{i}\n")
    OutputFile.close()
    print (f"Written to file successfully!")

def MetaDataImage():
    try:
        from exif import Image #Importing exif library along with declaring EXIT flag as false by default.
    except ModuleNotFoundError:
        print (f"The EXIF module was not found on this system! Please refer to the README for instructions.")
        return
    EXIT = False
    while True: #while true statement to catch invalid inputs
        try:
            ImageFile = input(f"Enter the name of the image file to use: ") 
            with open (ImageFile, "rb") as UserImage: #Entering and reading ffile, with try except catching exceptions for invalid file names.
                WorkingImage = Image(UserImage)
            break
        except FileNotFoundError:
            print ("Invalid File Name / File not found!")
    commonMems = set(list(dir(WorkingImage))) #puts every attribute into a list and sorts them
    commonMemsSorted= sorted(commonMems)
    while True:
        if EXIT == True: #This loop is entered if the user has decided to EXIT the loop
            NewFile = input(f"What would you like the new edited file to be named? [Include File Extension]: ")
            with open (NewFile, 'wb') as newimage:
                newimage.write(WorkingImage.get_file()) #Creates the new file as per the user's entered name.
            print (f"The new file has been created successfully.") #Success statement
            break
        print (f"\nThere are {len(commonMemsSorted)} attributes. They are:")
        for i in commonMemsSorted:
            print (f"[*] {i}") #Prints all metadata
        while True:
                UserEdit = input(f"What attribute would you like to read: ")
                if UserEdit in commonMemsSorted: #If the user enters a vaild metadata attribute, exit the loop - otherwise, output invalid option message
                    break
                else:
                    print (f"That wasn't an option!") 
        GetAttribute = ExifGet(WorkingImage, UserEdit) #This throws the image and the user's requested change into the class
        Result = GetAttribute.GetAttribute(WorkingImage, UserEdit) #This retrives it and prints it on the screen, telling the user what the value is.
        while True:
            Q1 = input(f"Would you like to change {UserEdit}? (Y/N): ") #asks the user if tthey would like to changge it
            if Q1 == "Y" or Q1 == "y":
                UserChange = input(f"Change {UserEdit} to what?: ")
                ChangeAttribute = ExifChange(WorkingImage, UserEdit, UserChange) #Throws the user's value into the class
                Result = ChangeAttribute.ChangeAttribute(WorkingImage, UserEdit, UserChange) #Prints out the new value using the user's paramaters.
                while True:
                    Q2 = input(f"Would you like to change another? (Y/N): ") #Simple question asking the user if they want to change another, sending them back to the beginning of the loop
                    if Q2 == "Y" or Q2 == "y":
                        break
                    if Q2 == "N" or Q2 == "n":
                        EXIT = True #In order to contain the loop as a whole, if the user chooses to exit: this flag is set to true and the next iteration of the loop asks the user where to save.
                        break
            if Q1 == "N" or "n":
                break
            else:
                print (f"Please use Y/y/N/n.") #Catches invalid inputs.

def MetaDataSound(): #NOT DONE
    try:
        import mutagen
    except ModuleNotFoundError:
        print (f"The MUTAGEN module was not found on this system! Please refer to the README for instructions.")
        return
    print (f"NOTE: This feature permanently changes info of a file. Do create backups!") #Warning message.
    while True:
        while True:
            try:
                SoundFile = input(f"Enter the name of the sound file to use [Including File Extension]: ")
                audio = mutagen.File(SoundFile) #Opens the sound file through mutagen and catches invalid names.
                break
            except:
                print (f"Invalid File / File Not Found.")
        print (f"File Read Successfully...")
        print (f"Here are general attributes: {audio.info.pprint()}")
        try:
            print (audio.tags.pprint()) #Prints all available audio tags (if available)
            if (audio.tags.pprint()) == "":
                print (f"This file doesn't seem to have any attributes that can change. Try a different file.") #If statement for if an audio file has no changable attributes, but doesn't cause an exception.
                break
        except:
            print (f"\nThis file doesn't have any metadata available to change. Try a different file.")
            break #Returns the user back to the beginning of the function
        while True:
            UserEdit = input(f"What attribute would you like to edit? [Type EXIT if finished]: ") #Asks the user which attribute they would like to change
            if UserEdit == "EXIT" or UserEdit == "exit": #If EXIT, then it saves the changes to the audio file
                print (f"Your changes to {SoundFile} have been saved!")
                audio.save() #Function to save the file.
                break
            if UserEdit == "horses": #Easter egg 
                VeryImportant()
                continue
            if UserEdit in audio.tags: #If the user chosen attribute is in the list of tags...
                UserChange = input(f"Change {UserEdit} to what?: ") #Asks the user what to change the attribute to
                MutagenChange = MutagenClass(UserChange, UserEdit, audio) #Passes what the user wants the value to be, the attribute to change, and the file to open
                Result = MutagenChange.MutaChange(UserChange, UserEdit, audio) #Getting those three attributes back to view the tags.
                print (f"The tags of {SoundFile} are now:")
                print (audio.tags.pprint()) #Prints all tags with their updated attributes.
            else:
                print (f"That's not an available attribute.") #Error message to catch invalid inputs.
        break #Break statement to exit the user from both loops

def VeryImportant():
    print("""\

                                        ._ o o
                                        \_`-)|_
                                        ,""       \ 
                                    ,"  ## |   ಠ ಠ. 
                                    ," ##   ,-\__    `.
                                ,"       /     `--._;)
                                ,"     ## /
                            ,"   ##    /


                        """)
    
def LogFileScanning(): #NOT DONE
    pass

def WriteLogFile(): #NOT DONE
    pass

def OnionLinkGen(): #NOT DONE
    pass

if __name__ == "__main__": #calling main!
    IPA = ""
    main()
