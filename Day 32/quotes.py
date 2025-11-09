import smtplib
import datetime as dt
import random

MY_EMAIL = "a.lotankar304@gmail.com"
PASSWORD = "ufdmylmlpczjzinu"
TO_EMAIL = "atharvalotankar11@gmail.com"

now = dt.datetime.now()
week_day = now.weekday()
if week_day == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Fantastic Friday Motivation\n\n{quote}"
        )