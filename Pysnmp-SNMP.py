#CONNECT DEVICE VIA SSH AND PUT SNMP CONFIG INTO DEVICE VIA INVOKE SHELL OPENED IN SSH SESSION
import paramiko
import time
from pysnmp.hlapi import *

# Switch Info
ip = '192.168.56.100'
username='python'
password='Huawei12#$'

# SSH login
ssh = paramiko.client.SSHClient()
ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
ssh.connect(hostname=ip,port=22,username=username,password=password)
print(ip+' login succesfully')

# Open a channel and enter the configuration.
cli = ssh.invoke_shell()
cli.send('N\n')
time.sleep(0.5)
cli.send('screen-length 0 temporary\n')
time.sleep(0.5)

# Run the following command to go to the system view:
cli.send('system-view immediately\n')
time.sleep(0.5)

# Read the snmp.txt file in the same local folder line by line and write the file to the SSH channel.
f = open('snmp.txt','r')
snmp_config_list = f.readlines()
for i in snmp_config_list:
 cli.send(i)
 time.sleep(0.5)

# Set up an SNMP channel.

UdpTransportTarget((ip,161))
g = getCmd(SnmpEngine(),

# Obtain the host name of the device.
 UsmUserData('admin','Huawei@123','Huawei@123',authProtocol=usmHMACSHAAuthProtocol,privProtocol=usmAesCfb128Protocol),
            UdpTransportTarget((ip, 161)),
            ContextData(),
            ObjectType(ObjectIdentity('SNMPv2-MIB','sysName',0)))
errorIndication, errorStatus, errorIndex, varBinds =next(g)
for i in varBinds:               #The varBinds variable is a tuple, including the returned message in an SNMP query ( SNMPv2-MIB::sysName.0 = CE1)
    print (i)
    print (str(i).split('=')[1].strip())       #get the device name by splitting from = sign and take the only that valu after 1st "=" sign)

dis_this = cli.recv(999999).decode() # View the script interaction process.
print (dis_this)
# Close the session.
ssh.close()

"""
Invoke UdpTransportTarget() in pysnmp. The parameters include the destination IP address and port number.
Invoke getCmd() to implement the GET operation of SNMP and assign the value to g.
●	UsmUserData indicates SNMP user information, including SNMP user name, password, encryption mode, and authentication mode. The SNMP user information must be consistent with the SNMP configurations on the device.
●	UdpTransportTarget is the transport layer information.
●	ContextData is used in asynchronous mode. Leave this parameter empty.
●	ObjectType indicates the device MIB object to be queried. You can use either the object name or OID. The object name is used here.
You can query the MIB information of Huawei devices at:
https://support.huawei.com/onlinetoolsweb/infoM/index.do?domain=1&lang=en&t opicType=mib
The name of the MIB object file to be queried is SNMPv2-MIB.

Create variables errorIndication, errorStatus, errorIndex, and varBinds to obtain the returned information of next(g).
For details about the returned information, see the official document at http://snmplabs.com/pysnmp/docs/hlapi/asyncore/sync/manager/cmdgen/getcmd. html. You can customize the variable names

"""