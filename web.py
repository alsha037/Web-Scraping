import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.flipkart.com/search?q=sunscreen+spf+50&sid=g9b%2Cema%2C5la%2Cxrh&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_8_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=sunscreen+spf+50%7CSunscreen&requestId=5776db21-afcf-4f33-8b59-4f67086ada2b&as-searchtext=sunscree'
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")  # Using "html.parser" instead of "lxml"

names = soup.find_all("a", class_="s1Q9rs")
prices = soup.find_all("div", class_="_30jeq3")

# Create a CSV file and write the data into it
with open('tablet_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Price'])  # Write header

    for name, price in zip(names, prices):
        name_text = name.text.strip()
        price_text = price.text.strip()

        writer.writerow([name_text, price_text])

print("Data scraped and saved to tablet_data.csv")