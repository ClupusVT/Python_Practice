import subprocess
interface = "eth0"
new_mac = "00:11:22:33:44:55:66:77"
print ("[+] Change MAC hardware of " + interface + "to new mac address" + new_mac)

subprocess.call("ifconfig"+ interface + "down", shell=True)
subprocess.call("ifconfig hw" + interface + new_mac, shell=True)
subprocess.call("ifconfig"+ interface + "up", shell=True)    