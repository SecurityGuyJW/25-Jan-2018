import sys
import socket
import getopt
import ntpath
import random
import time
import threading


target = 0
port = 0
listen = False
destination = ""
conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)



def instruction():

    print("-t : IPV4")
    print("-p : PORT")
    print("-f : File")

    print("")

    print("Example: -t 192.168.1.1 -p 5000 -f urs/somefile/example.txt")


def server():
    global port
    global conn

    destination = "/home/ubuntu/Desktop/Juans_Scripts/dump"

    filename = random.randrange(1,50)

    destination = destination + '/' + str(filename)

    conn.bind(("",int(port)))

    conn.listen(5)

    server, var = conn.accept()

    #gets the leaf of the file


    # add conversion here for other OS

    with open(destination, "wb") as fw:

        data = server.recv(4060)

        fw.write(data)

        fw.close()

def client():
    global target
    global port
    global destination

    destination = str(destination)

    conn.connect((target,int(port)))

    with open(destination, 'rb') as fs:

        data = fs.read(1024)

        conn.send(data)

        fs.close()


def main():

    global listen
    global target
    global port
    global destination
    global conn

    if not len(sys.argv[1:]):

        instruction()

        sys.exit("no input")

    opts, args = getopt.getopt(sys.argv[1:], "t:p:f:l",
                               ["host", "port", "file","listen"])

    for o,a in opts:

        if o in ("-t"):
            target = a

        elif o in ("-p"):
            port = a

        elif o in ("-f"):
            destination = a

        elif o in ("-l"):
            listen = True

        else:
            print("selection%s"%o," not found")
            instruction()
            sys.exit(0)


    if listen == True:

        server()

    else:

        client()

    conn.close()

main()



