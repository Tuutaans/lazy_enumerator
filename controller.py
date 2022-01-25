import subprocess
from scans.ssh_bf import ssh_bf
from scans.http import http
from scans.https import https
from scans.nikto import nikto
from scans.ftp_conn import ftp_conn
from scans.enum4linux import enum4linux
from scans.smbclient import smbclient
from scans.showmount import showmount

class Controller:
    def __init__(self, port, target):
        self.port = port
        self.target = target

    def nmap(self):
        command = f"nmap -sVC -p {self.port} -T4 {self.target}"
        subprocess.call(command, shell=True)

    def web(self):
        http(self.target)
        nikto(self.target)
        https(self.target)

    def ftp(self):
        ftp_conn(self.target)

    def ssh():
        print("SSH brute forcing using hydra!!!!   HAIL HYDRA....")

    def samba(self):
        enum4linux(self.target)
        smbclient(self.target)
        showmount(self.target)

def controller(target, port):
    controller = Controller(port, target)
    if port == 80:
        http(target)
        nikto(target)
    elif port == 443:
        https(target)
        nikto(target)
    elif port == 21:
        ftp_conn(target)
    elif port == 22:
        ssh_bf(target)
    elif port == 443:
        enum4linux(target)
        smbclient(target)
        showmount(target)