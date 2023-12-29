"""
Created by Wiilaptop
HTML Scraping Class

Purpose: Quick and Easy HTML Scraping!
"""
import requests
from bs4 import BeautifulSoup



class HTMLScrape():

    def __init__(self, page, TO):
        self.page = page
        self.TO = TO

    def HTMLConnect(self, page, TO):
        FoundContacts = []
        try:
            import socket
        except ModuleNotFoundError:
            return 1
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TO)
        try:
            sock.connect((page,80))
            target = (f"GET / HTTP/1.1\r\nHost:{page}\r\n\r\n")
        except socket.gaierror: #if an IP could not be resolved, move to the next iteration in the loop.
            return 2 #
        except socket.error: #If for some reason, a socket fails as a whole, move to the next iteration.
            return 3 # Sends socket error back to Main.
        sock.sendall(target.encode('ascii')) #encoding the info recieved into workable information.
        allcontent = b"" #bytes variable to fully recieve data
        content = b"" #bytes variable to fully recieve data
        try:
            while b"</html>" not in content: #while loop to make sure that all content is recieved, only breaking loop if the end of an html file is found / if content doesn't return anything new.
                content = sock.recv(4096)
                allcontent += content # adding whatever content delivers into allcontent, which would contain the entire page.
                if content == b"": #if content doesn't return anything, leave loop.
                    break
        except:
            print(f"This webpage timed out.") #If a webpage doesn't return a connection.
        try:
            webpage = allcontent.decode() #Attempt to decode information from a website
            webpagelines = 0
            for line in webpage.split("\n"):
                webpagelines += 1
            # return (webpage,webpagelines)
            for line in webpage.split("\n"):
                if "<a href=" in line:
                    FoundContacts.append(line)
            return (FoundContacts, webpagelines)
        except:
            print (f"This website didn't recieve properly.") #Move to next iteration if an IP address blocks incoming traffic.
            return 4 # Sends Socket error for didn't recieve
        
    def HTTPSUrls(self, page, TO):

        #Initalizing the list as empty so it doesn't overlap with multiple scans.
        FoundContacts = []

        #Try and get a page, if it fails, print an error and return a 0 to the main program.
        try:
            response = requests.get(page)
        except requests.exceptions.MissingSchema:
            return 0
        except requests.exceptions.ConnectionError:
            return 1
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        for aline in soup.find_all('a', href=True): 
            if aline.text: 
                FoundContacts.append(aline['href'])
        return (FoundContacts)
    
    def HTTPSEmails(self, page, TO):
        emails = []
        try:
            response = requests.get(page)
        except requests.exceptions.MissingSchema:
            return 0
        except requests.exceptions.ConnectionError:
            return 1           
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        for aline in soup.find_all('a', href=True): 
            if "mailto:" in aline['href']:
                emails.append(aline.text)
        return (emails)
