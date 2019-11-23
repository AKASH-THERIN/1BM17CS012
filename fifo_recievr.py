import os
import sys

path = "/tmp/my_program.fifo"
fifo = open("file2.txt", 'r')
print(fifo)
for line in fifo:
    print ("Received: " + line),
fifo.close()
