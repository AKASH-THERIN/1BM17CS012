import os

path = "/tmp/my_program.fifo"
os.mkfifo("file12.txt")

fifo = open("file2.txt", "w")
fifo.write("Message from the sender!\n")
fifo.close()
