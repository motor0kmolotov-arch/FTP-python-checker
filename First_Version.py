import ftplib as ftp
import socket;

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
    elif Choice.lower() == "run":
        try:
            ftp_connection = ftp.FTP()
            ftp_connection.connect(Ip,Port)
            ftp_connection.login(Username,Password)
            while ftp_connection:
                Commands = input("FTyrionP:")
                if Commands == "exit" or Commands == "quit":
                    ftp_connection.quit()
                    break
                elif Commands.upper() == "LIST":
                    ftp_connection.retrlines("LIST")
                    continue
                elif Commands.upper() == "PWD":
                    print(ftp_connection.pwd())
                    continue

        except ConnectionRefusedError:
            print("---Connection Refused error check if ftp works again---")
            continue
        except socket.timeout:
            print("---You got timedout it may be port is closed---")
            continue