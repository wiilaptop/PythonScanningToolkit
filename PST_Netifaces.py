# Created with love from Texas by Wiilaptop
import netifaces

#This is the Netifaces module for use in the Python Scanning Toolkit.

Information = []
class NetInfoClass():
    def __init__(self):
        pass

    def GetInterfaces(self):
        try:
            #Attempt to simply print all information using the netifaces module
            MyInterfaces = netifaces.interfaces()
        except:
            #Due to the variety of network types, exception handling here for if an error occurs. 
            return 0
        for Interface in MyInterfaces:

            #Appending found information about the IP addresses and sending them back to the main program.
            ipaddresses = netifaces.ifaddresses(Interface)
            if netifaces.AF_INET in ipaddresses:
                ipaddress_desc = ipaddresses[netifaces.AF_INET]
                ipaddress_desc_dist = ipaddresses[netifaces.AF_INET][0]
                Information.append(ipaddress_desc_dist)
        return Information