import requests
from bs4 import BeautifulSoup
n = input()
url = "https://news.ycombinator.com/"
content = requests.get(url)
soup = BeautifulSoup(content.content,'html.parser')
for i,tag in enumerate(soup.find_all('td',attrs = {'class':'title','align':''})):
	if tag.next != 0:
		print(str(i)+" "+tag.text)
