import sys
import os
import socket
import getopt
import threading

target       = 0
port         = 0
connections  = 0
toggle       = True
toggle_l     = True
loop         = True
listen       = False

pullFrom        = ""
placeIn         = "/home/ubuntu/Desktop/dump"

def instruction():

    print("-t : IPV4")
    print("-p : PORT")
    print("-f : File")

    print("")

    print("Example: -t 192.168.1.1 -p 5000 -f urs/somefile/example.txt")
    

#***********************************************************************************************************************
def serverSide():

    global port
    global toggle
    global connections

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(("",int(port)))

    server.listen(5)

    print("file transfer server waiting for connections...")

    def clientHandler(client):

        handlePayload(client,placeIn)

    while True:

        try:

            client,var = server.accept()

            connections += 1

            print("")
            print("")
            print("")
            print(client)


            print("connection ACCEPTED!")

            print("successful connnections:",connections)

            print("IP:" and var[0])
            print("Port:" and var[1])

            fileTransferServer = threading.Thread(target=clientHandler,args=(client,))

            fileTransferServer.start()

        except Exception as err:

            print(err)

            break


def handlePayload(client, placeIn):

    global buffer
    global toggle

    if toggle:

        value = client.recv(1020)

        buffer = int(value)

        print("file buffer is, %d" %buffer)

        toggle = False

        client.close()

    else:

        print("")
        print("")

        file_name = raw_input("Enter file name with correct extension... \nFile:")

        payload = client.recv(buffer)

        print("")
        print("")
        print("<--------------file location------------->")

        print(placeIn + file_name)

        file = open(placeIn + file_name, "wb")

        print("dumping a file with size %d" % buffer)

        file.write(payload)

        print("File transfer complete...")

        toggle = True

        file.close()

        client.close()

        os._exit(0)


#***********************************************************************************************************************

def clientSide():

    global target
    global port
    global pullFrom

    pullFrom = str(pullFrom)

    sendBuff(target, port, pullFrom)

    sendFile(target, port, pullFrom)


def sendBuff(target,port,pullFrom):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target, int(port)))

    data = open(pullFrom, "rb")

    payload = data.read()

    buffer = converToBuffer(payload)

    client.send((buffer))

    data.close()

    client.close()

def sendFile(target,port,pullFrom):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #

    client.connect((target, int(port)))

    data = open(pullFrom, "rb")

    payload = data.read()

    client.send(payload)

    data.close()

    client.close()

def converToBuffer(data):

    size = len(data)
    return str(size)

def main():

    global listen
    global target
    global port
    global pullFrom

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
            pullFrom = a

        elif o in ("-l"):
            listen = True

        else:
            print("selection%s"%o," not found")
            instruction()
            sys.exit(0)


    if listen == True:

        serverSide()

    else:

        clientSide()

    print("done")
    
 #***********************************************************************************************************************

main()
