import pywhatkit as kit
import schedule
import time

# Define your study schedule with time and messages
study_schedule = {
    "08:30": "📖 Study Networking: Learn OSI Model",
    "10:00": "🐧 Linux Practice: File Management & Scripting",
    "12:00": "☁ AWS Practice: EC2 & S3 Hands-on",
    "15:00": "📜 DevOps Tools: Learn Docker Basics",
    "18:00": "🗣 English Speaking Practice",
    "21:00": "🔄 Revise & Practice Previous Topics"
}

# Your and your friend's WhatsApp number (Format: "+CountryCodeNumber")
my_number = "+919145209421"  # Replace with your number
friend_number = "+917219366167"  # Replace with your friend's number

# Function to send WhatsApp messages
def send_study_reminder(task):
    print(f"Sending Reminder: {task}")
    kit.sendwhatmsg_instantly(my_number, task)  # Send to yourself
    kit.sendwhatmsg_instantly(friend_number, task)  # Send to your friend

# Schedule each study task
for time_slot, task in study_schedule.items():
    schedule.every().day.at(time_slot).do(send_study_reminder, task)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(10)  # Check every 10 seconds

