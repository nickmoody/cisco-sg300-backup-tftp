# Python script for backing up Cisco SG300 switches

This script by default will backup Cisco SG300 switches to a tftp server
Author - Nick Moody - netassured.co.uk

# REQUIRMENTS
1) Netmiko installed https://github.com/ktbyers/netmiko
2) Cisco SG300 switches must have ip 'ssh password-auth'configured to prevent the username being requested twice
3) TFTP server to send the running configs too


# Known limitations:
TFTP is not encrypted so only execute this script on a dedicated management network or over a VPN
