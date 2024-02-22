# Made with love from Texas by Wiilaptop

#Main function that is called for initalization upon first boot.
def main():
    print (f"\n[*] Starting the Python Scanning Toolkit...\n")
    
    #This will be the list that contains all of accessable items 
    AccessableItems = []

    #Statements for importing all detected modules for dynamic functionality

    #Here, every module will attempt to import the PST module AND the required packages. If any of these initial imports fail,
    #PST will tell the user the packages that are missing and exclude that functionality from the program.

    #At minimum, one module is required for PST to function.

    try:
        from PST_HTML import HTMLScrape
        from bs4 import BeautifulSoup
        import requests
        print (f"[✓] The PST HTML Scraping Module was loaded successfully.")
        AccessableItems.append("HTML Scraping")
    except ModuleNotFoundError:
        print (f"[!] One or more dependencies were not found for HTML Scraping. (PST_HTML.py, bs4, and requests.)")
        
    try:
        from PST_Netifaces import NetInfoClass
        import netifaces
        print (f"[✓] The PST Netifaces Module was loaded successfully.")
        AccessableItems.append("View Network Interfaces")
    except ImportError:
        print (f"[!] One or more dependencies were not found for viewing network interfaces. (PST_Netifaces.py, netifaces)")
    
    try:
        from PST_PortScanner import PortScanner
        import socket
        print (f"[✓] The PST Port Scanner Module was loaded successfully.")
        AccessableItems.append("Port Scanning")
    except ImportError:
        print ("[!] One or more dependencies were not found for port scanning. (PST_PortScanner.py, socket)")
    
    try:
        from PST_Image import MetadataImage
        from exif import Image
        import mutagen
        print (f"[✓] The PST Metadata Scraping and editing Module was loaded successfully.")
        AccessableItems.append("View & Change Metadata")
    except ModuleNotFoundError:
        print (f"[!] One or more dependencies were not found for changing metadata. (PST_Image.py, exif, mutagen)")
        
    #Closing PST if there are no modules detected.
    if len(AccessableItems) == 0: print(f"\n[!] No modules were detected. PST requires at least one module."); exit()

    #Adding "Quit" to the list so the user can exit.
    AccessableItems.append("Quit")

    #Calling the Main Menu and throwing AccessableItems into it based on detected modules.
    MainMenu(AccessableItems)

#The Main Menu that is in a "while" loop to keep the user within bounds.
def MainMenu(AccessableItems):
    while True:
        print (f"\n\nWelcome to the Main Menu.")
        TopLevelChoice = MenuTemplate(AccessableItems)

        if TopLevelChoice == "HTML Scraping":
            print (f"Selected Option: {TopLevelChoice}"); HTMLScraping()
        if TopLevelChoice == "View Network Interfaces":
            print (f"Selected Option: {TopLevelChoice}"); NetworkInterfaces()
        if TopLevelChoice == "Port Scanning":
            print (f"Selected Option: {TopLevelChoice}"); PortScannerRun()
        if TopLevelChoice == "View & Change Metadata":
            print (f"Selected Option: {TopLevelChoice}"); MetaDataImage()
        if TopLevelChoice == "Quit":
            print (f"\n[*] Quitting Python Scanning Toolkit..."); exit()

#The Menu Template to keep a consistent menu process throughout the program.
def MenuTemplate(MO):
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

#The function used to read input from a user's file.
def ReadUserFile(condition):

    #The condition for multiple file input. Seperates the files by commas and inserts them into a variable
    #for processing by the function that originally called it.
    if condition == 1:
        File = str(input(f"Seperated by commas (,) - enter the filenames to import: "))
        FileNames = File.split(",")
        return FileNames
        
    #Initalizing an empty list for the file's contents
    FileContents = []
    while True:
        File = str(input(f"Enter the name of the file you would like to import into PST: "))
        try:
            FileLines = open(File, "r").readlines()
            break
        except FileNotFoundError:
            print (f"{File} wasn't found. Maybe it was mispelled, or in a different directory?")

    #Reading the file line by line and returning it to whatever function called it.
    for line in FileLines:
        FileContents.append(line.strip())
    return FileContents

#The function used to write files to the user's machine.
def WriteUserFile(FileContents, TypeOfScan):
    #Declaring the OutputFile as PST with the name of the scan preformed.
    OutputFile = open(f"PST_{TypeOfScan}.txt", "w")
    for i in FileContents:
        OutputFile.write(f"{i}\n")
    OutputFile.close()
    print (f"Written to file successfully!")

#Function for scraping HTML pages.
def HTMLScraping():
    #Initalizing the Website List as empty to not interfere between multiple scans.
    WebsiteList = []

    #Disclamer statement for the current functionality of email scraping.
    print (f"\n[!]Note: Mail Scanning is still in development. You're welcome to try it - but there's some testing happening.")
    print (f"What are we scanning?")
    #Asking the user how many websites to scan, and calling either the read file function
    #or calling the ReadUserFile() function for a file to be read line by line.
    AmountOfWebsites = MenuTemplate(["One Website", "Multiple Websites", "Return to Main Menu"])
    if AmountOfWebsites == "One Website":
        page = input(f"Enter the webpage to browse: ")
        WebsiteList.append(page)
    if AmountOfWebsites == "Multiple Websites":
        WebsiteList = ReadUserFile()
    if AmountOfWebsites == "Return to Main Menu":
        return

    #Asking the user if they want to scrape URLS or mailto: lines in the HTML code
    #and setting a flag dependent on the option.
    WhatToScrape = MenuTemplate(["Scrape URLs", "Scrape mailto:", "Quit"])
    if WhatToScrape == "Scrape URLs":
        MailScrape = False
    if WhatToScrape == "Scrape mailto:":
        MailScrape = True
    if WhatToScrape == "Quit":
        return
    
    #Prompt asking the user for if they want to write to a file or not.
    WriteToFile = MenuTemplate(["Single Run", "Write To File"])
    if WriteToFile == "Single Run":
        pass
    if WriteToFile == "Write To File":
        FileContents = []

    #Calling the function from the previously imported module.
    #Python only imports the function once, so we are simply calling it here.
    from PST_HTML import HTMLScrape

    #Calling the respective class dependent on if the user is scanning for links or emails.
    #The "TypeOfScan" variable is written so that if the user chose to save the file, they will be able to
    #determine what type of scan was ran.
    for page in WebsiteList:
        if MailScrape == False:
            PageView = HTMLScrape(page, 0)
            PageResults = PageView.HTMLurl(page, 0)
            TypeOfScan = "UrlScan"
        if MailScrape == True:
            PageView = HTMLScrape(page, 0)
            PageResults = PageView.HTMLemail(page, 0)
            TypeOfScan = "EmailScan"
        
    
    #Here, we iterate through the list created by the classes above. The classes are coded to throw errors for 0 and 1,
    #which mean that they either did not connect or were incorrectly typed.
    try:
        for item in PageResults:
            if PageResults == 0: print(f"No scheme applied. Perhaps you meant https://{page}?"); continue
            if PageResults == 1: print(f"There was a problem connecting to {page}. Continuing to next page."); continue
            print (f"{page}: {item}")
    except TypeError:
        print (f"There seems to be an error connecting to that page. Perhaps you meant https://{page}?")
            
    #If the user chose to write to a file, throw all the output into a list.
    if WriteToFile == "Write To File":
        FileContents.append(f"{page}: {item}")

    #If the user wanted a file, this calls the write file function.
    if WriteToFile == "Write To File":
        WriteUserFile(FileContents, TypeOfScan)

#Function for viewing the Network Interfacts on the current machine.
def NetworkInterfaces():
    #Importing the class file from the .py file once again, so it does not have
    #to be passed through from the MainMenu Function.
    from PST_Netifaces import NetInfoClass

    GetNetworkInfo = NetInfoClass()
    Output = GetNetworkInfo.GetInterfaces()
    if Output == 0: print(f"An error occured when attempting to retrieve Interfaces.")

    NetInterfaceIndex = 0
    for ipaddress_desc_dict in Output: #for all the data in the list...
        NetInterfaceIndex += 1
        print (f"\n{NetInterfaceIndex}.")
        if ipaddress_desc_dict.get('addr','addr not found'): #If there's an "addr" value, print it
            print (f"IP Address: {ipaddress_desc_dict['addr']}")
        if ipaddress_desc_dict.get('netmask', 'netmask not found'):#If there's a "netmask" value, print it
            print (f"Netmask: {ipaddress_desc_dict['netmask']}")
        
        try:
            if ipaddress_desc_dict.get('broadcast', 'broadcast not found'): #If there's a "broadcast" value, print it
                print (f"Broadcast: {ipaddress_desc_dict['broadcast']}")
        except KeyError:
            print (f"[!] This interface's broadcast was unable to be found.")

    print (f"Your current public IP address is:")

#Function for scanning ports, using either a file or user input.
def PortScannerRun():
    #Declaring a list for the found Ports
    PortsFound = []

    #Asking the user for the IP address to scan for ports on
    IPA = input(f"Enter the IP address to scan for ports on: ")

    #Calling the MenuTemplate function to ask the user if they want to do a single, standalone
    #scan, or if they want to scan ports from a CSV file
    typeOfPortScan = MenuTemplate(["Single Scan", "Scan Ports from .csv File", "Quit"])

    #If Single Scan is selected, mark TypeOfScan as "SoloScan" for file writing,
    #and mark SoloScan as True
    if typeOfPortScan == "Single Scan":
        TypeOfScan = "SoloScan"
        SoloScan = True

    #If the user selects to scan from a .csv file, they can upload a file from the ReadUserFile()
    #function, and marks the scan name as needed. Initalizes the Port Dictionary
    if typeOfPortScan == "Scan Ports from .csv File":
        TypeOfScan = "FileScan"
        SoloScan = False
        PortFile = ReadUserFile()
        PNDictionary = {}

        #This is the for loop that will grab every line in the .csv file, strip it and split it based on comma.
        #The example file in the github repo has a demonstartion of this. (port, name, desc.)
        for i in range(1, len(PortFile)):
            portInfo = []
            LineParts = PortFile[i].strip().split(",")
            portInfo.append(LineParts[1])
            portInfo.append(LineParts[2])
            PNDictionary[int(LineParts[0])] = tuple(portInfo)
        print (f"File read. Num Ports = {len(PNDictionary)}")

    #If the user chooses to quit, return them back to the main menu of the program.
    if typeOfPortScan == "Quit":
        return
    
    #while True statment for catching invalid inputs and asking the user on what the timeout
    #value should be for each port.
    while True:
        try:
            print (f"Timeout values under 1.0 may not grab a connection in time.")
            TO = float(input(f"Enter a timeout (1, 1.5, 2):"))
            break
        except ValueError:
            print (f"Hmm. That didn't seem right. Please enter a float or integer!")
    
    from PST_PortScanner import PortScanner

    #Asking the user the range of ports to scan, with beginning port and ending port.
    print (f"Scanning on {IPA}, what range of ports are we scanning? - Ex. (1 - 85): ")
    begPort = int(input(f"Enter the beginning port to scan: "))
    endPort = int(input(f"Enter the ending port to scan: "))

    #for every port in range, throw the ip address and port into the port scanning class.
    #If the socket connects in the class, it will return a 0. Here, we will document what port was open.
    for port in range(begPort, endPort):
        print (f"IP: {IPA}, Scanning Port: {port}", end = "\r")
        PortScan = PortScanner(port, IPA, TO)
        Results = PortScan.Scanner(port, IPA, TO)
        if Results == 0:
            portscanned = (f"[+ PORT FOUND] Port {port} was open on {IPA}!")
            print (portscanned)
            PortsFound.append(portscanned)
    
    print (f"\nPort Scanning on {IPA} complete!")

    #if the user decides to save the output to a file, call the WriteUserFile() function with
    #a description of the scan and the PortsFound list.
    PrintToFile = input(f"Do you want to write the results of the scan to a file? (Y/n): ")
    if PrintToFile == "Y":
        WriteUserFile(PortsFound,TypeOfScan)

#Function for viewing and changing EXIF data of an image and sound file.
def MetaDataImage():
    
    #Insuring that the Image module from exif and the PST module are imported for access in this function.
    from exif import Image
    from PST_Image import MetadataImage

    #Asking the user if they want to view the metadata of multiple files, or view and change the data of a single file.
    print (f"\nHere, we can view and change the Metadata of Image files.")
    MetaDataMenu = MenuTemplate(["View Metadata of Multiple Images", "Change Metadata of Single Image", "View and Change Metadata of Sound Files","Return to Main Menu"])
    if MetaDataMenu == "View Metadata of Multiple Images":

        #If the user chooses to view the metadata of multiple files, run the ReadUserFile function
        #with the condition of (1) to indicate that it's for multiple files.
        FileNames = ReadUserFile(1)
        for currentFile in FileNames:
            try:

                #Here, we open every file in the list of files, initalize a list for all of the attributes,
                #write them all to a text file using the WriteUserFile() function with the name of the current image.
                with open (currentFile, "rb") as UserImage:
                    WorkingImage = Image(UserImage)
                ImageScan = MetadataImage(WorkingImage)
                commonMemsSorted = ImageScan.ViewParamaters(WorkingImage)
                ExifDataList = []
                count = 0
                for element in commonMemsSorted:
                    try:
                        ExifDataList.append(f"{count}. {element} = {getattr(WorkingImage, element)}")
                    except (AttributeError, NotImplementedError) as Error:
                        ExifDataList.append(f"{count}. {element} = There was an error fetching this attribute. Exception = {Error}")
                    count +=1 
                WriteUserFile(ExifDataList, f"ExifData_{currentFile}")
            except FileNotFoundError:
                print (f"Unable to find {currentFile}. Continuing to next file.")

    #Here, if the user asks to scan the data of a single file, we begin processing.
    if MetaDataMenu == "Change Metadata of Single Image":

        #Asking the user to input the type of file they want to insert into PST. This is seperated from the regular
        #ReadUserFile() function as the Image module requires a bit of configuration before images can be processed.
        while True:
            try:
                ImageFile = input(f"Enter the name of the image file to use: ")
                with open (ImageFile, "rb") as UserImage:
                    WorkingImage = Image(UserImage)
                break
            except FileNotFoundError:
                print (f"Invalid File Name. Perhaps it was in a different directory?")

        #Listing to the user all of the attributes of the image after putting them into a list.
        ImageScan = MetadataImage(WorkingImage)
        commonMemsSorted = ImageScan.ViewParamaters(WorkingImage)
        print (f"There are {len(commonMemsSorted)} attributes. They are: \n")

        #If an image has an attribute that Python is unable to process, it will output the error to the user here and continue processing.
        count = 0
        for element in commonMemsSorted:
            try:
                print (f"{count}. {element} = {getattr(WorkingImage, element)}")
            except (AttributeError, NotImplementedError) as Error:
                print (f"{count}. {element} = There was an error fetching this attribute. Exception = {Error}")
            count += 1

        #Printing out to the user what they would like to do next AFTER viewing all the EXIF data.
        print (f"\n[*] EXIF data for {ImageFile} listed. What would you like to do next?")
        print (f"[!] PST will create a new file when changing EXIF data to keep the original file.")

    #If a user wants to change the metadata of sound files, they can do so here.
    if MetaDataMenu == "View and Change Metadata of Sound Files":
        import mutagen
        print (f"[*] This feature, at this time, permanently changes info of a sound file. Do create backups!")

        while True:
            try:
                soundFile = input(f"Enter the name of the sound file to use (Including File Extension): ")
                audio = mutagen.File(soundFile)
                print (f"File read successfully...")
                break
            except:
                print (f"{soundFile} wasn't found. Maybe it was misspelled or in a different directory?")
        try:
            print (f"Here are the general attributes: {audio.info.pprint()}")
        except:
            print (f"This file may actually have no available metadata to change. Try a different file.")
        
        MutagenMenu = MenuTemplate(["Export EXIF data", "Change EXIF data", "Exit to Main Menu"])

        if MutagenMenu == "Export EXIF data":
            pass
        if MutagenMenu == "Change EXIF data":
            pass
        if MutagenMenu == "Exit to Main Menu":
            return

    #If the user decides to go to the Main Menu, they can do so here.
    if MetaDataMenu == "Return to Main Menu":
        return

    #You can either save the EXIF data as-is, or begin to change it here.
    SaveExifData = MenuTemplate(["Save Exif Data to .txt File", "Change EXIF Data", "Quit"])
    
    #If the user chooses to save the EXIF data to a file, that file will be written here and WriteUserFile() will be called
    #for the creation of the .txt file.
    if SaveExifData == "Save Exif Data to .txt File":
        ExifDataList = []
        count = 0
        for element in commonMemsSorted:
            try:
                ExifDataList.append(f"{count}. {element} = {getattr(WorkingImage, element)}")
            except (AttributeError, NotImplementedError) as Error:
                ExifDataList.append(f"{count}. {element} = There was an error fetching this attribute. Exception = {Error}")
            count +=1 
        WriteUserFile(ExifDataList, f"ExifData_{ImageFile}")

    #If the user chooses to change the EXIF data of the file, they can do so here.
    if SaveExifData == "Change EXIF Data":
        while True:

            #Here, the user is asked for the attribute to change. We use a "get and set", similar to other progrmaming langages.
            #We "get" the attribute that the user wants to change, and "set" it to the variable the user inputs.
            UserEdit = input(f"\nEnter the name of the attribute you like to change: ")
            if UserEdit in commonMemsSorted:
                UserChange = input(f"{UserEdit} is currently {getattr(WorkingImage, UserEdit)}. What would you want to change it to?: ")
                setattr(WorkingImage, UserEdit, UserChange)
                print (f"[*] {UserEdit} has now been changed to {UserChange}!")
                
                #The user now has the choice of saving the changed file, continously change attributes, or abort the process entirely.
                ChangeAgain = MenuTemplate(["Change Additional EXIF data", "Save Changed File", "Exit without Saving"])

                #If the user wants to change additional EXIF data, simply continue the loop once more.
                if ChangeAgain == "Change Additional EXIF data":
                    continue
                
                #If the user wants to save the changed file, we create it here.
                if ChangeAgain == "Save Changed File":
                    NewFile = input(f"What you like the modified {ImageFile} to be named?: ")
                    with open (NewFile, 'wb') as newimage:
                        newimage.write(WorkingImage.get_file())
                    print (f"[*] The new file has been created successfully.")
                    return
                
                #If the user wants to abort, return to the Main Menu here.
                if ChangeAgain == "Exit without Saving":
                    print (f"[*] Returning to Main Menu. Changes will not be saved.")
                    return

            #If an attribute was not found, tell the user what happened here.
            else:
                print (f"Seems like {UserEdit} was not a valid attribute. ")
    
    #Returns to the Main Menu.
    if SaveExifData == "Quit":
        return
    
#Calling Main for first boot.
if __name__ == "__main__":
    main()