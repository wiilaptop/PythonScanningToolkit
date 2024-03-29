# Created with love from Texas by Wiilaptop
import requests
import httpx
from bs4 import BeautifulSoup
import re
import json

#This is the HTML scraper module for use in the Python Scanning Toolkit.

class HTMLScrape():
    def __init__(self, page, TO):
        self.page = page
        self.TO = TO
    
    def HTMLurl(self, page, TO):
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

        #Using BeautifulSoup's html.parser ability to quickly search for a specific character
        #within the HTML code.
        soup = BeautifulSoup(html_content, 'html.parser')
        for aline in soup.find_all('a', href=True): 
            if aline.text: 
                FoundContacts.append(aline['href'])
        return (FoundContacts)
    
    def HTMLemail(self, page, TO):
        emails = []
        try:
            response = requests.get(page)
        except requests.exceptions.MissingSchema:
            return 0 #Error if the website does not have a schema (https://)
        except requests.exceptions.ConnectionError:
            return 1 #Error if the website does not connect.
        html_content = response.text

        #Similarly to the previous function, but this one looks for "Mmailto:" tags.
        soup = BeautifulSoup(html_content, 'html.parser')
        for aline in soup.find_all('a', href=True): 
            if "mailto:" in aline['href']:
                emails.append(aline.text)
        return (emails)
