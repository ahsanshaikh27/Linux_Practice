import pywhatkit as kit

# Send a WhatsApp message
phone_number = "+917219366167"  # Replace with your friend's number (include country code)
message = "Hello! This is an automated message from Python 🚀"
hour = 1  # 24-hour format
minute = 5

# Schedule message
kit.sendwhatmsg(phone_number, message, hour, minute)
print("Message scheduled successfully!")
print("My First Automatically Send Message Script")

