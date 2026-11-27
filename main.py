# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import random
import pandas
import datetime as dt
import smtplib
from email.message import EmailMessage
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MAIL")
MY_PASSWORD = os.environ.get("PASS")


def generate_email(person):
    birthday_name = person["name"]
    birthday_email = person["email"]

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt", "r") as file:
        letter_template = file.read()
        birthday_letter = letter_template.replace("[NAME]", birthday_name)

    with smtplib.SMTP("smtp.mail.me.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        msg = EmailMessage()
        msg["From"] = MY_EMAIL
        msg["To"] = birthday_email
        msg["Subject"] = f"Happy Birthday {birthday_name}!"
        msg.set_content(birthday_letter)
        connection.send_message(msg)

today = dt.datetime.now()
today_month = today.month
today_day = today.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    generate_email(birthday_person)


