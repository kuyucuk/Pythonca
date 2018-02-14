import urllib.request
import bs4 as bs
import datetime
import difflib

from openpyxl import Workbook
wb = Workbook()
ws = wb.active

sauce = urllib.request.urlopen('https://www.instagram.com/').read()

soup = bs.BeautifulSoup(sauce,'lxml')

data=soup.title.text



print(str(data))