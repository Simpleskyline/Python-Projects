import os

subnet = "192.168.1."
devices_found = []  # store only the online devices

for i in range(1, 255):
    ip = subnet + str(i)
    response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")

    if response == 0:  # ✅ device replied
        devices_found.append(ip)
        print(f"{ip} --> Online ✅")

# After scanning all 254 addresses
if not devices_found:
    print("\nNo devices found on the network ❌")
else:
    print(f"\nScan complete. {len(devices_found)} device(s) found ✅")
