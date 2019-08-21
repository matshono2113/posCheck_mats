from bluetooth.ble import DiscoveryService
import re
import serial
import time
import struct

class Scan():
        def __init__(ser):
                ser.s = serial.Serial('/dev/ttyS0',38400,timeout=10)
                print(ser.s)

        def scanBLE(ser):
                postList = []
                service = DiscoveryService()
                devices = service.discover(2)

                l = []

                for address, name in devices.items():
                        address = address.replace(':', '')
                        address = [ address[i*2:i*2+2] for i in xrange(len(address)/2) ]
                        #print (address)
                        l.extend(address)

                #print (l)
                return l

def main():
        sc=Scan()
        while True:
                print (sc.scanBLE())

if __name__ == "__main__":
        main()
