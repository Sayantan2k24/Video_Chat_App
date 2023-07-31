import subprocess

# Step 1: Run the respective command and save its filtered output to a text file
# file handling
output_file = "ipconfig_output.txt"
try:
    with open(output_file, "w") as file:
        subprocess.run("ipconfig | find \"IPv4 Address. . . . . . . . . . . :\"", stdout=file, shell=True, text=True)
except subprocess.CalledProcessError as e:
    print("Error running ipconfig:", e)
    exit()

# Step 2: Read the file and extract all IPv4 addresses
ip_addresses = []
with open(output_file, "r") as file:
    for line in file:
        ip_address = line.split(":")[1].strip()
        ip_addresses.append(ip_address)

# Step 3: Check if IPv4 addresses were found and retrieve the last one
if ip_addresses:
    last_ip_address = ip_addresses[-1]
    print(last_ip_address)
else:
    print("No IPv4 Address found in the output.")
