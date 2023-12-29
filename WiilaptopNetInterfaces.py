"""
Created by Wiilaptop
Network Interface Class

Purpose: Allow for the Main command to pass arguements to the netifaces module.
"""


Information = []
class NetInfoClass():
    def __init__(self):
        pass

    def GetInterfaces(self):
        try:
            import netifaces
        except ModuleNotFoundError:
            return 1
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