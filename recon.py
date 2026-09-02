import subprocess

target = input("Enter target IP or hostname: ")

print("\nStarting Network Reconnaissance...")
print("-" * 40)

print(f"Target: {target}")
print("\nScanning common ports...\n")

result = subprocess.run(
    ["nmap", "-sV", target],
    capture_output=True,
    text=True
)

print(result.stdout)

print("-" * 40)
print("Scan completed.")
