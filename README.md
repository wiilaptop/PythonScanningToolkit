My first GitHub repo, named the "PythonScanningToolkit", or PST for short.

A small based Python program made during university in my sophomore year. Still actively being worked on and developed to this day.
I have always had a fondness for command-line based applications, and wanted to put my skills to the test creating a Python script that not only grasped
my passion for development, but also had real-world functional cybersecurity use.

This Python script, to help me get a grasp on how to import and use classes, is split up among multiple .py files. In the future, the script will adapt to the functionality of the currently
installed .py files, but for now - download all of the files to ensure nothing blows up :)

Here are the current and future planned abilities of PST:

1. Scrape HTTP Webpages running on Port 80 (This was the original function of the program for uni.)
2. Scrape HTTPS Webpages for mailto: links & any URLS in the HTML code.
3. View the current machine's network interfaces.
4. Scan for ports on a specified network (and give a description of said port using the included .csv file. This can be considered active recon, use at your own risk.)
5. Change the metadata of Image files.
6. Change the metadata of Sound files.
7. (In-Development) Scan log files for specific phrases.
8. (In-Development) Create and determine genuine .onion webpages (Mostly as a proof-of-concept. Onion links are extremely few & far between, and some may contain illegal content. Continue this at your own risk.)

In order for FULL functionality as the script currently stands, some Python libraries are to be installed...
1. Mutagen (Official docs: https://mutagen.readthedocs.io/en/latest/)
2. EXIF (Official docs: https://exif.readthedocs.io/en/latest/usage.html)
3. Requests (Official docs: https://requests.readthedocs.io/en/latest/)
4. bs4 (Official docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Many of these can be simply installed with pip :)

This script is something that I ultimately want to fine-tune and show as a demonstration of my skills. I love Python and how adaptable it is, and I cannot wait to see what the future holds!
