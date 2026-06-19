#number of smart devices in the home network
device_count = 15

# total number of system configurations (2 to the power of devices)
#each device can be either 0 (Eco Mode) or 1 (Active Mode)
total_configurations = 2 ** device_count

print("--- SMART HOME CONFIGURATION REPORT ---")
print(f"Number of smart devices in the network: {device_count}")
print(f"Total system setup variations to evaluate: {total_configurations:,}")

#what happens if smart home ecosystem expands slightly
print("\n--- WHAT IF THE ECOSYSTEM EXPANDS? ---")
for extra_devices in [20, 25, 30]:
    expanded_configurations = 2 ** extra_devices
    print(f"For {extra_devices} devices: {expanded_configurations:,} system variations.")
