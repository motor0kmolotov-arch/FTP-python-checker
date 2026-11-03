from ftplib import FTP, error_perm, error_temp, all_errors
import socket

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
            ftp_connection = FTP()
            ftp_connection.connect(Ip,Port)
            ftp_connection.login(Username,Password)
            while ftp_connection:
                try:
                    Commands = input("FTyrionP:")
                    if Commands.upper() == "exit" or Commands.upper() == "quit":
                        ftp_connection.quit()
                        break
                    elif Commands.upper() == "LIST":
                        ftp_connection.retrlines("LIST")
                        continue
                    elif Commands.upper() == "PWD":
                        print(ftp_connection.pwd())
                        continue
                    elif Commands.upper() == "CD":
                        FolderToSwitch = input("Folder->")
                        ftp_connection.cwd(FolderToSwitch)
                    elif Commands.upper() == "NLST" or Commands.upper() == "FILES":
                        print(ftp_connection.nlst())
                    else:
                        print("---unknown command---")
                        continue
                except error_perm:
                    print("---No Folder/File found---")
        except ConnectionRefusedError:
            print("---Connection Refused error check if ftp works again---")
            continue
        except socket.timeout:
            print("---You got timedout it may be port is closed---")
            continue
        except error_perm:
            print("---False login please try again---")
            continue
        except error_temp:
            print("---The Server is overloaded please try again later---")
            continue
        