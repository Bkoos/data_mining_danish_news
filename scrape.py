# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup as BS
import requests
from afinn import Afinn
from datetime import date, timedelta
import csv

afinn = Afinn("da")
today = date.today()
dates = 3000

columns = ["date", "title", "url", "afinn"]
items = []

with open("3000days_of_DR.csv", "w", encoding="utf-8") as csv_file:
    for i in range(dates):
        delta = timedelta(days=i)
        date_i = today - delta
        date_string = date_i.strftime("%d%m%Y")
        print(date_string)
        req = requests.get("https://www.dr.dk/nyheder/allenyheder/politik/%s" % date_string)
        html = BS(req.text, 'html.parser')
        section = html.select('.dr-list')[0]
        for h in section.find_all("article"):
            title = h.find("a").get_text()
            url = h.find("a")["href"]
            #print(title)
            #print("%d \t%s" % (afinn.score(title), title))
            item = [date_string, title, url, afinn.score(title)]
            item_writer = csv.writer(csv_file)
            item_writer.writerow(item)
