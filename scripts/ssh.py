#! /Users/aguda/opt/anaconda3/bin/python3

import getpass
import sys
import time
import paramiko
from scp import SCPClient


class Ssh:
    """
    docstring for Ssh Class
    Ssh(hostname, user, password)
    hostname should host IP
    user should be username of host
    password should password of host
    """
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password      

    def ssh(self, command):
        """
        docstring for ssh function
        ssh(command)
        command should input for this function to get the results of remote host
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, port="22", username=self.user, password=self.password, timeout='5')
        (stdin, stdout, stderr) = ssh.exec_command(command)
        stdin.write(password + '\n')
        stdin.flush()
        #print(stdout.readlines())
        print("".join(stdout.readlines()))
        ssh.close()

class Scp(Ssh):
    """
    docstring for SCP Class
    SCP(hostname, user, password)
    inherited from source Ssh class
    hostname should host IP
    user should be username of host
    password should password of host
    """
    def scp(self, file):
        """
        docstring for scp function
        scp(file)
        file should input for this function to copy the file to remote host
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, port="22", username=self.user, password=self.password, timeout='5')
        scp = SCPClient(ssh.get_transport())
        print("Copy {} from local to {}".format(file, self.host))
        scp.put(file, recursive=True, remote_path='/tmp/')
        # copy from remote host to local
        # scp.get(file)
        ssh.close()



if __name__ == '__main__':
    user = "nvidia"
    if len(sys.argv) < 3:
        print("Please pass arguments to scirpt as 'python ssh.py hostip command filename'")
        sys.exit()
    elif len(sys.argv) == 3:
        password = getpass.getpass(prompt='Enter password: ')
        hostname = sys.argv[1]
        cmd = sys.argv[2]
        HOST = Ssh(hostname, user, password)
        HOST.ssh(cmd)
    elif len(sys.argv) == 4:
        password = getpass.getpass(prompt='Enter password: ')
        hostname = sys.argv[1]
        cmd = sys.argv[2]
        file = sys.argv[3]
        HOSTONE = Scp(hostname, user, password)
        HOSTONE.scp(file)
        time.sleep(10)
        HOST = Ssh(hostname, user, password)
        HOST.ssh(cmd)
