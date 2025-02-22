import psutil
import time

def get_system_stats():
    """Fetch system CPU, Memory, and Disk Usage."""
    stats = {
        "CPU Usage": f"{psutil.cpu_percent(interval=1)}%",
        "Memory Usage": f"{psutil.virtual_memory().percent}%",
        "Disk Usage": f"{psutil.disk_usage('/').percent}%",
    }
    return stats

def log_system_stats():
    """Log system stats every 5 seconds."""
    with open("system_logs.txt", "a") as log_file:
        while True:
            stats = get_system_stats()
            log_entry = f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}, {stats}\n"
            print(log_entry.strip())  # Print to console
            log_file.write(log_entry)
            time.sleep(5)  # Log every 5 seconds

if __name__ == "__main__":
    log_system_stats()

