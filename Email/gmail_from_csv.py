import csv 
from .email_setup import send_email_gmail

def send_email_from_csv():
    try:
        with open('file.csv', mode ='r')as file:
            csvFile = csv.reader(file)
            for client in csvFile:
                send_email_gmail(client[1], name=client[0]) 
    except Exception as err:
        print(f"An errror has occured, {err}")


send_email_from_csv()
