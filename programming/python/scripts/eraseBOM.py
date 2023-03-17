#!/usr/bin/env python3

import sys

def eraseBom(oldFilePath, newFilePath, bomLength):
    with open(oldFilePath, mode='br') as template:
        print(template.peek(bomLength)[:bomLength])
        bom = template.read(bomLength)
        print(bom)
        print(template.tell())

        data = template.read()
        #print(len(data))

    with open(newFilePath, mode='bx') as modified:
        modified.write(data)
    return

if __name__ == "__main__":
    assert (len(sys.argv) == 3 or len(sys.argv) == 4), "The number of input parameters is not sufficient ({})".format(len(sys.argv))
    OLD_FILE_NAME = sys.argv[1]
    NEW_FILE_NAME = sys.argv[2]
    BOM_LENGTH = int(sys.argv[3]) if(len(sys.argv) == 4) else 6
    eraseBOM(OLD_FILE_NAME, NEW_FILE_NAME, BOM_LENGTH)
