import socket

#common ports list
ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]
target = input("Enter target IP or domain: ")

print(f"\nScanningtarget: {target}")
print("-"*40)

#loop for port
for port in ports:
	#create new socket object using IPv4 address(AF_INET) with TCP connection (SOCK_STREAM)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#if didnt responeded within 1sec move to next
	socket.setdefaulttimeout(1)
	
	#tries to connect to that specific port where (connect_ex) attempts connection
	result =s.connect_ex((target, port))
	
	if result == 0:
		print(f"port {port} is OPEN")
	
	s.close()
	
print("\n Scan completed")
