#!/usr/bin/env python
from paramiko import SSHClient
import paramiko
import sys
import re

class SSH:
    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def exec_cmd(self,cmd,ip):
        self.ssh.connect(hostname=ip,username='user',password='$1$qw5kOVo3$YZZWQuxclGnUJCTnb13wQ.')
        stdin,stdout,stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print stderr.read()
        else:
            print stdout.read()



if __name__ == '__main__':
        ssh = SSH()
        with open('/home/user/CHAMADA/lista.txt','r+') as f:
          x = f.readlines()
          for y in x:
            print (y)
            ssh.exec_cmd("date",y)
