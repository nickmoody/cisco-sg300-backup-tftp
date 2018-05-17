#!/usr/bin/env python
# Copyright (C) 2018
# cisco_sg300_backup_tftp.py
# This script by default will backup Cisco SG300 switches to a tftp server
# Author - Nick Moody - netassured.co.uk
# Last Updated 13th February 2018
#
# REQUIRMENTS
# 1) Netmiko installed https://github.com/ktbyers/netmiko
# 2) Cisco SG300 switches must have ip 'ssh password-auth'configured to prevent the username being requested twice
# 3) TFTP server to send the running configs too

# Known limitations:
# TFTP is not encrypted so only execute this script on a dedicated management network or over a VPN

from netmiko import ConnectHandler
import time

# Configuration options
tftp_server = '10.10.10.10'
tftp_folder = 'cisco'

# specify the date and time for use in the filename created on the tftp server
hour=time.strftime('%H')
minute=time.strftime('%M')
day=time.strftime('%d')
month=time.strftime('%m')
year=time.strftime('%Y')
today=day+"-"+month+"-"+year+"-"+hour+minute

''' Define the list of switches to be backed up. IP addresses can be used in place of hostnames. For a large a number of switches
it might be neater to use an external file then import into the script'''
cisco_sg300_01 = { 'device_type':'cisco_s300', 'ip':'cisco_sg300_01', 'username':'cisco', 'password':'cisco'}
cisco_sg300_02 = { 'device_type':'cisco_s300', 'ip':'cisco_sg300_02', 'username':'cisco', 'password':'cisco'}
cisco_sg300_03 = { 'device_type':'cisco_s300', 'ip':'cisco_sg300_03', 'username':'cisco', 'password':'cisco'}
cisco_sg300_04 = { 'device_type':'cisco_s300', 'ip':'cisco_sg300_04', 'username':'cisco', 'password':'cisco'}

# Create a python list to include which switches to backup
switches = [cisco_sg300_01, cisco_sg300_02, cisco_sg300_03, cisco_sg300_04]

for device in switches:

 filename = device['ip']+'-' + today
 save_config = 'copy running-config tftp://'+tftp_server+'/'+tftp_folder+'/'+filename
 net_connect = ConnectHandler(**device)
 output = net_connect.send_command(save_config)
 time.sleep(10)
 print output
 net_connect.disconnect()
