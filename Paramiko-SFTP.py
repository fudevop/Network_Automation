#FILE TRANSFER VIA SFTP BY PASSWORD
import paramiko

tran = paramiko.Transport('192.168.56.100',22)
tran.connect(username='python',password='admin123')

sftp = paramiko.SFTPClient.from_transport(tran)
localpath = r'C:\Users\F84131242\Desktop\ssh\vrptest.cfg'
remotepath = 'flash:/vrpcfg.zip'
sftp.get(remotepath,localpath)
sftp.put(localpath,'flash:/vrpconfignew.zip')

tran.close()

#FILE TRANSFER VIA SFTP BY DIGITAL SIGNATURE
import paramiko

key=paramiko.RSAKey.from_private_key_file(r'C:\Users\admin\ssh\id_rsa')
tran = paramiko.Transport('192.168.56.100',22)
tran.connect(username='python',pkey=key)

sftp = paramiko.SFTPClient.from_transport(tran)
localpath = r'C:\Users\F84131242\Desktop\ssh\vrptest.cfg'
remotepath = 'flash:/vrpcfg.zip'
sftp.get(remotepath,localpath)
sftp.put(localpath,'flash:/vrpconfignew.zip')

tran.close()

