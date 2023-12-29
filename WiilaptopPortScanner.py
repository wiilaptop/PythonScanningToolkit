"""
Created by Wiilaptop
Port Scanner Class

Purpose: Allow for the Main command to pass arguements to the Port Scanner
"""
import socket

class PortScanner():
    def __init__(self, PN, IPA, TO):
        self.PN = PN
        self.IPA = IPA
        self.IO = TO
    
    def Scanner(self, PN, IPA, TO):
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.settimeout(TO)
        try:
            return (mysock.connect_ex((IPA,PN)))
        except socket.error:
            return (1)