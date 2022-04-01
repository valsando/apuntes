import subprocess

interface = input("interface > ")
new_mac = input("nuevo MAC > ")

print("[+] Cambiando Direccion MAC Para " + interface + " a " + new_mac)

subprocess.call("ipconfig " + interface + " down", shell=True)
subprocess.call("ipconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ipconfig " + interface + " up", shell=True)