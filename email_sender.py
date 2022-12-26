import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
SEND_TO = os.environ.get("SEND_TO")


class EmailSender:
    def __init__(self):
        self.connection = smtplib.SMTP("smtp.gmail.com", 587)
        self.connection.starttls()

    def send_email(self, price, link, name):
        self.connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        self.connection.sendmail(from_addr=MY_EMAIL,
                                 to_addrs=SEND_TO,
                                 msg=f"Subject: from Python Amazon Tracker App\n\n"
                                     f"The price of your desired product fell to {price}\n"
                                     f"Product Name: {name}\n"
                                     f"Click here for the link:\n"
                                     f"{link}")
        self.connection.close()
