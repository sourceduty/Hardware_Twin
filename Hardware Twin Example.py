import random
import psutil
import time

# Define the Hardware Components

class CPU:
    def __init__(self, cores, base_clock, max_clock):
        self.cores = cores
        self.base_clock = base_clock
        self.max_clock = max_clock
        self.current_load = 0.0  # Percentage

    def simulate_load(self, load):
        self.current_load = load
        # Simulate clock speed adjustment based on load
        if load < 50:
            return self.base_clock
        else:
            return self.max_clock

class RAM:
    def __init__(self, total_memory):
        self.total_memory = total_memory
        self.used_memory = 0.0  # GB

    def simulate_usage(self, usage):
        self.used_memory = min(self.total_memory, usage)

class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.used_space = 0.0  # GB

    def simulate_io(self, read_write_speed):
        # Simulate I/O operations
        return f"Performing I/O at {read_write_speed} MB/s"

class NetworkInterface:
    def __init__(self, bandwidth):
        self.bandwidth = bandwidth
        self.current_usage = 0.0  # MB/s

    def simulate_network_load(self, load):
        self.current_usage = min(self.bandwidth, load)

# Simulate System Behavior Over Time

def simulate_system_behavior_over_time(cpu, ram, storage, network, duration, interval):
    start_time = time.time()
    elapsed_time = 0

    while elapsed_time < duration:
        # Simulate CPU load
        cpu_load = random.uniform(10, 100)
        cpu_speed = cpu.simulate_load(cpu_load)
        print(f"[{elapsed_time:.1f}s] CPU Load: {cpu.current_load:.2f}% - Clock Speed: {cpu_speed} GHz")

        # Simulate RAM usage
        ram_usage = random.uniform(1, ram.total_memory)
        ram.simulate_usage(ram_usage)
        print(f"[{elapsed_time:.1f}s] RAM Usage: {ram.used_memory:.2f} GB / {ram.total_memory} GB")

        # Simulate Storage I/O
        io_speed = random.uniform(50, 500)
        print(f"[{elapsed_time:.1f}s] {storage.simulate_io(io_speed)}")

        # Simulate Network Load
        network_load = random.uniform(0, network.bandwidth)
        network.simulate_network_load(network_load)
        print(f"[{elapsed_time:.1f}s] Network Usage: {network.current_usage:.2f} MB/s / {network.bandwidth} MB/s")

        time.sleep(interval)  # Wait for the specified interval before next simulation
        elapsed_time = time.time() - start_time

    print("\nSimulation completed.\n")

# Integrate Real-Time Data

def monitor_real_time_data(cpu, ram, storage, network):
    # Real-time CPU load
    cpu_load = psutil.cpu_percent(interval=1)
    cpu.simulate_load(cpu_load)
    print(f"Real-time CPU Load: {cpu.current_load}%")

    # Real-time RAM usage
    ram_info = psutil.virtual_memory()
    ram.simulate_usage(ram_info.used / (1024 ** 3))  # Convert to GB
    print(f"Real-time RAM Usage: {ram.used_memory:.2f} GB")

    # Real-time Disk I/O (simplified example)
    io_counters = psutil.disk_io_counters()
    print(f"Real-time Disk Read/Write Count: {io_counters.read_count}/{io_counters.write_count}")

    # Real-time Network usage (simplified example)
    net_io = psutil.net_io_counters()
    network.simulate_network_load(net_io.bytes_sent / (1024 ** 2))  # Convert to MB
    print(f"Real-time Network Usage: {network.current_usage:.2f} MB/s")

# Monitor and Predict Future Behavior

def monitor_and_predict(cpu, ram, storage, network):
    # Simple prediction based on current state
    if cpu.current_load > 80:
        print("Warning: High CPU load, performance may degrade.")
    if ram.used_memory > ram.total_memory * 0.8:
        print("Warning: High RAM usage, consider adding more memory.")
    if network.current_usage > network.bandwidth * 0.8:
        print("Warning: Network bandwidth is nearly saturated.")

# Display Available Commands

def display_commands():
    print("\nAvailable Commands:")
    print("1: Simulate System Behavior Over Time")
    print("2: Monitor Real-Time Data")
    print("3: Monitor and Predict")
    print("4: Exit\n")

# Main Function to Run the Digital Twin with Commands

def main():
    # Initialize hardware components
    cpu = CPU(cores=8, base_clock=2.6, max_clock=4.5)
    ram = RAM(total_memory=32)  # GB
    storage = Storage(capacity=1000)  # GB
    network = NetworkInterface(bandwidth=100)  # MB/s

    while True:
        display_commands()
        command = input("Enter a command number: ").strip()

        if command == "1":
            try:
                duration = float(input("Enter the duration of the simulation in seconds: "))
                interval = float(input("Enter the interval between updates in seconds: "))
                print("\nSimulating System Behavior Over Time:")
                simulate_system_behavior_over_time(cpu, ram, storage, network, duration, interval)
            except ValueError:
                print("Invalid input. Please enter numerical values for duration and interval.")
        elif command == "2":
            print("\nMonitoring Real-Time Data:")
            monitor_real_time_data(cpu, ram, storage, network)
        elif command == "3":
            print("\nMonitoring and Predicting:")
            monitor_and_predict(cpu, ram, storage, network)
        elif command == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please enter a valid command number.")

if __name__ == "__main__":
    main()
