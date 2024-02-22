# Created with love from Texas by Wiilaptop
import netifaces

#This is the Netifaces module for use in the Python Scanning Toolkit.

Information = []
class NetInfoClass():
    def __init__(self):
        pass

    def GetInterfaces(self):
        try:
            MyInterfaces = netifaces.interfaces()
        except:
            return 0
        for Interface in MyInterfaces:
            ipaddresses = netifaces.ifaddresses(Interface)
            if netifaces.AF_INET in ipaddresses:
                ipaddress_desc = ipaddresses[netifaces.AF_INET]
                ipaddress_desc_dist = ipaddresses[netifaces.AF_INET][0]
                Information.append(ipaddress_desc_dist)
        return Information