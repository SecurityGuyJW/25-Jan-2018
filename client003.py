# this client was written 25-Jan-2018
# This client is an command based client
# Users will have to option to take or plant a file

#****this program is incomplete****



import socket


conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def connInfo(sock):

    netdata = list()

    ip = "172.17.79.243" #raw_input("Enter IP:")
    port = 5000 #int(input("Enter Port:"))

    netdata.append(sock)
    netdata.append(ip)
    netdata.append(port)

    return netdata

def connConnect(netdata):

    try:
        netdata[0].connect((netdata[1],netdata[2]))
        netdata[0].send("Connection has been established...")

    except socket.error as err:
        print(err)
        print("connection experienced an error and will close...")
        netdata[0].close()

def fileSend(netdata):

    filename = "sendthis.txt"  #input(Send file:)

    payload = open(filename, 'rb')

    payload.write("file has been replaced")

    data = payload.read(1020)

    netdata[0].send(data) # create a dir and rawfile

    print(payload,"transfer complete...")


def fileTake(payload):
    return 0

def userTakeControll(netdata):

    def print_menu():
        print
        30 * "-", "MENU", 30 * "-"
        print
        "1. take file"
        print
        "2. send file"
        print
        "5. Exit"
        print
        67 * "-"

    while True:  ## While loop which will keep going until loop = False
        print_menu()  ## Displays menu
        choice = input("Enter your choice [1,2,5]:")

        if choice == 1:

            fileSend(netdata)

        elif choice == 2:

            payload = input("take")
            fileTake(payload)

        elif choice == 5:

            connTerminate(netdata)
            break
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")
            userTakeControll(netdata)

def connTerminate(netdata):

    for i in netdata:
        print(i)
    print("This connection ran successfully and will be closed")


def main():

    data = connInfo(conn)
    connConnect(data)
    userTakeControll(data)

main()

