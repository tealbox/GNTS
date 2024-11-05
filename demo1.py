from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime


def parseShowVersionHostname(cmd_output_showversion):
    template = open(r'cisco_nxos_show_version.textfsm')
    parsedText = textfsm.TextFSM(template)
    # print(parsedText.header)
    res = parsedText.ParseText(cmd_output_showversion)
##    print(res)
##    return res[0][0]
    return res



cisco1 = {
    "device_type": "cisco_ios",
    "host": "sbx-nxos-mgmt.cisco.com",
    "username": "admin",
    "password": "Admin_1234!",
    }

## print(cisco1)
# Show command that we execute.
command = "show version"
try:
    with ConnectHandler(**cisco1) as net_connect:
        # output = net_connect.send_command(command)
        # print(output)
        net_connect.find_prompt()
        # net_connect.send_command("term width 500")
        # net_connect.send_command("term length 500")
        output = net_connect.send_command(command)
##        print(output)
##        output = net_connect.send_command("show int status")
##        print(output)
        thishost = parseShowVersionHostname(output)
        print(thishost)

except Exception as e:
    print(f"Authentication Failed on {cisco1['host']}")
    # print(e)

