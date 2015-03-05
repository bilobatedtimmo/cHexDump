#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv)==2:
        filename = sys.argv[1]
    try:
        fd=open(filename, "rb")
    except:
        print("error, filename required", sys.exc_info()[0])
        sys.exit(0)
    counter = 0
    offset = 0
    byte = fd.read(8)
    asciList = []
    i = 1
    #if the file is empty, exit gracefully
    if len(byte) == 0:
        sys.exit(0)
    print("%08x " % (offset), end = " ")
    offset += int(len(byte))
    while len(byte)>0:
        for b in byte:
            print("%02x" %b, end = " ")
            c = chr(b)
            asciList.append(c)
        print(" ", end = "")
        #to print ascii values of all hex shown
        if len(asciList)>=16:
            print("|", end = "")
            for c in asciList:
                if ord(c) < 33:
                    print (".",end ="")
                elif ord(c) > 126:
                    print (".",end="")
                else:
                    print(c,end ="")
            print("|",end="")
            asciList[:] = []
        #to print previous bits displayed
        if (offset % 16 == 0):
                print("")
                print("%08x " % (offset), end = " ")
        #refreshing all values
        prev = byte
        byte = fd.read(8)
        offset += int(len(byte))
    #checks if list has items in it, if not print nothing
    if asciList:
        #this formats the final line if less than 8 bytes were read
        if (offset % 16 < 8):
            while i <= 25:
                print(" ",end="")
                i= i+1
        i = 1
        #this helps formatting of the last line
        while i <= 24 - (len(prev)*3):
            print (" ", end ="")
            i= i+1
        print("|", end ="")
        for c in asciList:
            if ord(c) < 33:
                print (".",end ="")
            elif ord(c) > 126:
                print (".",end="")
            else:
                print(c,end ="")
        print("|")
        print("%08x " % (offset))
    else:
        print("")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("")
        sys.exit(0)
