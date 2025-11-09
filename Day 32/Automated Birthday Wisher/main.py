#Automated Birthday Reminder Project
from datetime import datetime
import pandas
import random
import smtplib

# TODO 1: Change MY_EMAIL/MY_PASSWORD to your own details.
MY_EMAIL = "a.lotankar304@gmail.com"
MY_PASSWORD = "ufdmylmlpczjzinu"

today = datetime.now()
today_tuple = (today.month, today.day)

# TODO 4: Update birthdays.csv to contain today's month and day.
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# TODO 2: Go to your email provider and make it allow less secure apps.
# TODO 3: Update the SMTP ADDRESS to match your email provider.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
