#SSH CONNECTION WITH PASSWORD
import paramiko
import time

ssh  = paramiko.SSHClient()        #use SSHClient class from paramiko module to identify an SSH object
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)          #allow conenctions to unknown hosts,that is we do not need to type yer or no for ssh setup confirmation

ssh.connect(hostname='192.168.56.100',port=22,username='python',password='admin123')              #establish an SSH connection

cli = ssh.invoke_shell()      #open an interactive shell session which is a logical channel
cli.send('screen-length 0 temporary\n')        #display all command output in one screen instead of split screens
cli.send('display cur\n')
time.sleep(3)              #sets the time for command output complete

dis_cu = cli.recv(9999999).decode()          #capture the channel output information and assign the output into a variable.Also we use decode() method to encode output with UTF-8 format by default to see output well designed
print(dis_cu)

ssh.close()


#SSH CONNECTION WITH DIGITAL SIGNUTARE
import paramiko
import time

ssh  = paramiko.SSHClient()        #use SSHClient class from paramiko module to identify an SSH object
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)          #allow conenctions to unknown hosts,that is we do not need to type yer or no for ssh setup confirmation

ssh.connect(hostname='192.168.56.100',port=22,username='python',filename=r'C:\Users\admin\ssh\id_rsa')              #establish an SSH connection

cli = ssh.invoke_shell()      #open an interactive shell session which is a logical channel
cli.send('screen-length 0 temporary\n')        #display all command output in one screen instead of split screens
cli.send('display cur\n')
time.sleep(3)              #sets the time for command output complete

dis_cu = cli.recv(9999999).decode()          #capture the channel output information and assign the output into a variable.Also we use decode() method to encode output with UTF-8 format by default to see output well designed
print(dis_cu)

ssh.close()


