import pandas as pd
import datetime as dt
import random
import os

now = dt.datetime.now()
current_date = now.date()


current_month = current_date.month
current_day = current_date.day


birthday_dates = pd.read_csv("birthdays.csv")

def check_if_birthday():
    global birthday_check           
    birthday_check = birthday_dates[(birthday_dates['month'] == current_month) & (birthday_dates['day'] == current_day)]
    return birthday_check

while check_if_birthday == True:
    if not birthday_check.empty:
        for index, row in birthday_check.iterrows():
            random_file = random.choice(os.listdir("letter_templates"))
            with open(f"letter_templates/{random_file}", "r") as letter:
                letter_text = letter.read()

        birthday_wish = letter_text.replace("[NAME]", row['name'])
        print(birthday_wish)



# 4. Send the letter generated in step 3 to that person's email address.



