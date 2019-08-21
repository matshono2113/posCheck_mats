import lora
import time
import sys
import scan

lr = lora.LoRa()
sc = scan.Scan()

def sendcmd(cmd):
    print (cmd)
    lr.write(cmd)
    time.sleep(0.2)
    print (lr.readline())

def setMode():
    lr.write('config\r\n')
    lr.s.flush()
    time.sleep(0.2)
    lr.reset()
    time.sleep(1.5)

    sendcmd('2\r\n')
    sendcmd('bw 3\r\n')
    sendcmd('sf 7\r\n')
    sendcmd('q 2\r\n')
    sendcmd('w\r\n')

    lr.reset()
    print ('LoRa module set to new mode')
    time.sleep(1)
    sys.stdout.flush()

while (True):
        setMode()
        print (lr.readlines())
        while (True):
            bdAddr = []
            bdAddr = sc.scanBLE()
            print (bdAddr)
            print (type(bdAddr))
            if bdAddr is not None:
                #lr.write(bdAddr)
                time.sleep(0.5)
                print (lr.readline(timeout=0.5))

        sys.stdout.flush()
