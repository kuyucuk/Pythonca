import urllib.request
import bs4 as bs
import csv
from datetime import datetime

quote_page = 'http: // www.bloomberg.com / quote / SPX: IND'
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([datetime.now()])