import pywhatkit as kit
import psutil
import time

# Function to get system stats
def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return f"📊 System Monitoring Report:\nCPU: {cpu}%\nMemory: {memory}%\nDisk: {disk}%"

# WhatsApp number (include country code)
phone_number = "+9172........"  # Replace with actual recipient

while True:
    message = get_system_stats()
    kit.sendwhatmsg_instantly(phone_number, message)
    print("✅ Report sent successfully!")
    print("My first automate script")

    time.sleep(300)  # Wait for 5 minutes (300 seconds) before sending again

