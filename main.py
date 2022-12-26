import requests
from bs4 import BeautifulSoup
import email_sender

# for taking data from Amazon links you need to pass the below parameters from headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"
                  "108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,es;q=0.7,tr;q=0.6",
}

# sample link
link_to_product = input("Paste the link from the page of your desired product from AMAZON here: ")
maximum_price = int(input("Which price you will buy this? : "))

# tested link
# link_to_product = "https://www.amazon.com/Sceptre-Curved-Monitor-Speakers-C248W-1920RN/
# dp/B07KXSR99Y/ref=zg_bs_1292115011_sccl_3/141-9220179-3763057?th=1"
response = requests.get(link_to_product, headers=headers)
contents = response.text
soup = BeautifulSoup(contents, "html.parser")
today_price_tag = soup.select_one(selector=".a-price-whole")
product_title_tag = soup.select_one(selector="#productTitle")
today_price = int(today_price_tag.text.strip("."))
product_title = product_title_tag.text
# desired price for the purchase
if today_price < maximum_price:
    email_sender.EmailSender().send_email(price=today_price, link=link_to_product, name=product_title)
print(today_price)
