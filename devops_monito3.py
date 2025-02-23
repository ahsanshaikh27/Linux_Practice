import schedule
import time
import pywhatkit as kit

# Your WhatsApp number (change as needed)
phone_number = "+9172........."  # Replace with your number

# Define daily study plan
study_plan = {
    "8:30 AM": "📚 Study Linux Networking",
    "10:00 AM": "☁️ Practice AWS EC2 & S3",
    "12:00 PM": "🐳 Learn Docker & Kubernetes",
    "2:00 PM": "📖 Read about System Design",
    "4:00 PM": "📝 Hand on Practive",
    "5:30 PM": "💻 Work on DevOps Automation",
}

# Function to send study reminders
def send_study_reminder(task):
    message = f"🎯 Study Reminder: {task}\nStay focused and keep learning! 🚀"
    kit.sendwhatmsg_instantly(phone_number, message)
    print(f"✅ Reminder sent: {task}")

# Schedule study sessions
for time_slot, task in study_plan.items():
    schedule.every().day.at(time_slot).do(send_study_reminder, task)

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute

