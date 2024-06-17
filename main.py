import pandas as pd
import datetime as dt
import random
import os
import smtplib

now = dt.datetime.now()
current_date = now.date()


current_month = current_date.month
current_day = current_date.day

my_email = "sbxp1966@gmail.com"
password = "gogatmuwcjufqlet"


birthday_dates = pd.read_csv("birthdays.csv")
           
birthday_check = birthday_dates[(birthday_dates['month'] == current_month) & (birthday_dates['day'] == current_day)]

if not birthday_check.empty:
    for index, row in birthday_check.iterrows():
        random_file = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{random_file}", "r") as letter:
            letter_text = letter.read()

    birthday_wish = letter_text.replace("[NAME]", row['name'])
    


with smtplib.SMTP("smtp.gmail.com") as smtp:
    smtp.starttls()
    smtp.login(user=my_email, password=password)
    smtp.sendmail(
        from_addr=my_email,
        to_addrs= row['email'],
        msg=f"Subject: Happy Birthday !\n\n{birthday_wish}"
    )

with smtplib.SMTP("smtp.gmail.com") as smtp:
    smtp.starttls()
    smtp.login(user=my_email, password=password)
    smtp.sendmail(
        from_addr=my_email,
        to_addrs=my_email,
        msg=f"Subject: Birthday Notification\n\nHeads UP! Today is {row['name']} 's Birthday. Your BOT mailed {row['name']} already, But Wish {row['name']} personally"
        
    )



