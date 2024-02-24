# Created with love from Texas by Wiilaptop

import socket

#This is the Port Scanner module for use in the Python Scanning Toolkit.

class PortScanner():
    # Initalizing the use of the Port Number, IP Address, and the Timeout
    def __init__(self, PN, IP, TO):
        self.PN = PN
        self.IP = IP
        self.TO = TO

    #Here, the socket module is used to attempt to connect to the current port in
    #iteration, returning a 1 to the main program if a connection is unsuccessful.
    def Scanner(self, PN, IP, TO):
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.settimeout(TO)
        try:
            return (mysock.connect_ex((IP, PN)))
        except socket.error:
            return (1)
