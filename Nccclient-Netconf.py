# -*- coding: utf-8 -*-
from ncclient import manager
from ncclient import operations
import paramiko
import time

#WE WILL DELIVER IP ADDRESS TO AN INTERFACE VIA NETCONF & PREVIOUSLY WE CONNECT DEVICE VIA SSH AND CONFIGURE NETCONF USER/CONNECTIONS PARAMETERS WITH netconf_config_file file

# Device parameters
ip = '192.168.56.100'
ssh_user = 'python'
ssh_password = 'Huawei12#$'
netconf_port = '830'
netconf_user = 'netconf'
netconf_password = 'Huawei12#$'
filename='netconf.txt'

# Define the SSH class to configure NETCONF on the device.
class ssh():
    def ssh_connect(ip,username,password):
        ssh = paramiko.client.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.client.AutoAddPolicy())
        ssh.connect(hostname=ip,port=22,username=username,password=password)
        print(ip+' login succesfully')
        return ssh

    def ssh_config(netconf_config_file,ip,username,password):
        a = ssh.ssh_connect(ip,username,password)
        cli = a.invoke_shell()
        cli.send('N\n') time.sleep(0.5)
        cli.send('screen-length 0 temporary\n')
        time.sleep(0.5)

        f = open(file,'r')
        config_list = f.readlines()
        for i in config_list:
            cli.send(i)
            time.sleep(0.5)

        dis_this = cli.recv(999999).decode()
        print (dis_this)
        a.close()

# Define the huawei_connect function to establish a NETCONF connection.
def huawei_connect(host, port, user, password):
    return manager.connect(host=host,
                    port=port,
                    username=user,
                    password=password,
                    hostkey_verify = False,
                    device_params={'name': "huawei"},
                    allow_agent = False,
                    look_for_keys = False)
#manager.connect is used to establish a NETCONF connection. The parameters are defined in RFC4741. device_params has two options for Huawei devices. That is, the value can be huawei or huaweiyang, corresponding to the IETF YANG model or Huawei YANG model, respectively.
#Construct an XML configuration file by referring to the NETCONF Schema API Reference on the Huawei official website. https://support.huawei.com/enterprise/en/switches/cloudengine-12800-pid- 7542409
# Use NETCONF to send XML data and configure an IP address for an interface on the device.
CREATE_INTERFACE = '''
     <config>
        <ethernet xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
            <ethernetIfs>
                <ethernetIf operation="merge">
                    <ifName>GE1/0/2</ifName>
                    <l2Enable>disable</l2Enable>
              </ethernetIf>
            </ethernetIfs>
        </ethernet>
        <ifm xmlns="http://www.huawei.com/netconf/vrp" content-version="1.0" format-version="1.0">
          <interfaces>
            <interface operation="merge">
                <ifName>GE1/0/2</ifName>
                <ifDescr>Config by NETCONF</ifDescr>
                <ifmAm4>
                    <am4CfgAddrs>
                        <am4CfgAddr operation="create">
                            <subnetMask>255.255.255.0</subnetMask>
                            <addrType>main</addrType>
                            <ifIpAddr>192.168.2.1</ifIpAddr>
                        </am4CfgAddr>
                    </am4CfgAddrs>
                </ifmAm4>
            </interface>
          </interfaces>
        </ifm>
    </config>'''
#NETCONF uses XML files to send configurations. XML is a commonly used text format that allows you to nest and expand data. A complete NETCONF session consists of the transport layer, message layer, operation layer, and content layer. The current XML configuration file contains only the operation layer and content layer.
#In this example, the operation layer information is edit-config, and the operation attribute is merge. This operation edits the target data, which may exist or not in the database. If the target data does not exist, target data is created; if the target data exists, the target data is edited.
#The NETCONF content layer is used to edit specific parameters. In this example, disable the Layer 2 function on GE 1/0/2 by running the undo portswitch command, change the description to Config by NETCONF, and set the IP address to 192.168.2.1/24.

# Execute the main functions in sequence.
if name == ' main ':
    ssh.ssh_config(filename,ip,ssh_user,ssh_password)
    m = huawei_connect(ip,netconf_port,netconf_user,netconf_password)
    m.edit_config(target='running',config=CREATE_INTERFACE)
