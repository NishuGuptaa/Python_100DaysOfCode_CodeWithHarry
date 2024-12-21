# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send or send desktop notifications for a specific operating system.

import time
from plyer import notification

# Function to send water reminders
def water_reminder(interval):
    while True:
        notification.notify(
            title="Time to Drink Water 💧",
            message="Stay hydrated! Drinking water regularly is important for your health.",
            app_name="Water Reminder",
            timeout=10  # Notification stays on screen for 10 seconds
        )
        print("Notification sent! Next reminder in", interval // 60, "minutes.")
        time.sleep(interval)  # Wait for the interval before sending the next reminder

# Set the interval for reminders in seconds
interval = int(input("Enter the interval between reminders (in minutes): ")) * 60
water_reminder(interval)
