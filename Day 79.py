#Day 79: Automate emails


#Automate sending emails using Python.

import schedule
import time

def send_email():
    #Include the email-sending code here
    print("Email sent successfully")


#Schedule the email to be sent every day at 9:00 AM
schedule.every().day.at("9:00").do(send_email)

while True:
    schedule.run_pending()
    time.sleep(60) #Check every minute 