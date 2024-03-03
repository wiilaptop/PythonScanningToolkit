My first GitHub repo, named the "PythonScanningToolkit", or PST for short.

A small based Python program made during university in my sophomore year. Still actively being worked on and developed to this day.
I have always had a fondness for command-line based applications, and wanted to put my skills to the test creating a Python script that not only grasped
my passion for development, but also had real-world functional cybersecurity use.

This Python script, to help me get a grasp on how to import and use classes, is split up among multiple .py files, deemed "modules". As of Feb. 2024, PST will now determine what moduels are currently installed and enable further functionality based on that!

Here are the current and future planned abilities of PST:

1. Scrape HTTPS Webpages for mailto: links & any URLS in the HTML code.
2. View the current machine's network interfaces.
3. Scan for ports on a specified network (and give a description of said port using the included .csv file. This can be considered active recon, use at your own risk.)
4. Change the metadata of Image files.
5. Change the metadata of Sound files.
6. Scan log files for specific phrases.
7. (In-Development) Create and determine genuine .onion webpages (Mostly as a proof-of-concept. Onion links are extremely few & far between, and some may contain illegal content. Continue this at your own risk.)

Many of these packages are required to run some of the modules of PST. 
PST will tell you of these requirements when the program is ran.
1. Mutagen (Official docs: https://mutagen.readthedocs.io/en/latest/)
2. EXIF (Official docs: https://exif.readthedocs.io/en/latest/usage.html)
3. Requests (Official docs: https://requests.readthedocs.io/en/latest/)
4. bs4 (Official docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

Many of these can be simply installed with pip.

NOTE: Remember to use this tool in good faith. Only scan networks and websites that you trust and have permission to!

If you have any suggestions, feedback, or ideas about additional modules, do not hesitate to let me know! If you think of something amazing, totally make a fork of this repo and show me!
I would love to one day build this program with community-made modules (and of course ALL credit will be given!) that make PST one of the greatest tools out there! :)

This script is something that I ultimately want to fine-tune and show as a demonstration of my skills. I love Python and how adaptable it is, and I cannot wait to see what the future holds!
