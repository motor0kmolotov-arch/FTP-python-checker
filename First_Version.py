import ftplib as ftp

Ip = "127.0.0.1"
Port = 21
Username = "User"
Password = "changeme"

def Edit(ip,port,user,passwd):
    Edit_Choice = input(":")
    if Edit_Choice.lower() == "ip":
        ip = input("New IP: ")
    elif Edit_Choice.lower() == "port":
        port = int(input("New Port: "))
    elif Edit_Choice.lower() == "username":
        user = input("New Username: ")

    return ip,port,user,passwd

while True:
    Choice = input("->")
    if Choice.lower() == "help":
        print("| edit | run |")
    elif Choice.lower() == "edit":
        try:
            Ip,Port,Username,Password = Edit(Ip,Port,Username,Password)
        except ValueError:
            print("Pls write normal value")
            continue