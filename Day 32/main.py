#SMTP - Simple Mail Transfer Protocol
"""
import smtplib

my_email = "a.lotankar304@gmail.com"
password = "ufdmylmlpczjzinu"   #Python Mail
to_email = "atharvalotankar11@gmail.com"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()   #securing connection
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg="Subject: Hello \n\nThis is the body of my Email. Sent by PyCharm")
"""

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
#Monday-0, Tuesday-1, Wednesday-2, Thursday-3, Friday-4, Sat-5, Sun-6
print(day_of_week)

date_of_birth = dt.datetime(year=2004, month=11, day=3, hour=17, minute=15)
print(date_of_birth)