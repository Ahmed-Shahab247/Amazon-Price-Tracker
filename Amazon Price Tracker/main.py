import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

URL = "https://www.amazon.in/Razer-Basilisk-Customizable-Ergonomic-Gaming/dp/B09C13PZX7/ref=sr_1_14"


load_dotenv(".env")





email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
address = os.environ.get("ADDRESS")
user_a = os.environ.get("USER_AGENT")

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": user_a,
}

#Data is taken from Cookies found in chrome dev tools Application section
#This may be required to bypass the "NOT A ROBOT" check
cookies = {

    "session-token": ""
                     ""
                     ""
                     ""
                     "",
    "session-id-time":"",
    "csm-hit":"",
    "session-id":"",
    "i18n-prefs": "",
    "ubid-acbin": "",
}



#To send an email if the price is below or equal to the price set by user
def send_mail():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(from_addr=email, to_addrs=address, msg=f"Price has reduced to {price}")
    connection.close()





response = requests.get(URL,headers=header,cookies=cookies)
soup = BeautifulSoup(response.content,"html.parser")



find_price = soup.find(name="span", class_="a-price-whole").getText()

price = find_price.split(".")[0]
num = price.split(",")
price = "".join(num)
price = float(price)

print(price) #Current price of the product

if price<=10000: #Enter the price your willing to pay for the product
    send_mail()