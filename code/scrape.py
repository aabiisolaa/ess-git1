from bs4 import BeautifulSoup
import requests
url = open('index.html')
# with open('index.html') as html:
soup = BeautifulSoup(url,'lxml')
match = soup.find('h2',class_ ='second') 

print(match)
