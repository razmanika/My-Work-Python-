from bs4 import BeautifulSoup
import requests
import re

#user_input = input("Search words ")

web = requests.get('https://www.top.ge')
soup = BeautifulSoup(web.content, 'html.parser')

Find_Tag = soup.findAll("tg", {"class": "tr_paddings desc_pd hidden-xs ipad_hidden"}).get_text()

myTG = [link for link in Find_Tag]
myA = [here.get('href') for here in soup.findAll('a', attrs={'href': re.compile("^http://")})]

print(Find_Tag)