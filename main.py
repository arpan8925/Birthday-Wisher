##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt

now = dt.datetime.now()
current_date = now.date()


current_month = current_date.month
current_day = current_date.day


birthday_dates = pd.read_csv("birthdays.csv")


birthday_check = birthday_dates[(birthday_dates['month'] == current_month) & (birthday_dates['day'] == current_day)]

if not birthday_check.empty:
    for index, row in birthday_check.iterrows():
        print(f"Ajke {row['name']} er birthday")

else:
    print("Karo Birthday nai ajke")


# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




