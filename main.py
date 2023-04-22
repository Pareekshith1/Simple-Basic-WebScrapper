from bs4 import BeautifulSoup
import requests

pickuplines = requests.get('https://www.womansday.com/relationships/dating-marriage/a41055149/best-pickup-lines/').text
soup=BeautifulSoup(pickuplines,'lxml')
pickups= soup.find('div', class_='article-body-content')
lines = pickups.find_all('li')
print(lines)

pickuplines2 = requests.get('https://pickuplines.myshopify.com/blogs/funny-pickup-lines').text
soup=BeautifulSoup(pickuplines2,'lxml')
pickups2 = soup.find('div', class_='page-container')
lines2=pickups2.find_all('strong')

print(lines2)

with open('pickuplines.txt', 'w') as file:
    for item in lines:
       file.write(item.text + '\n')

with open('pickuplines.txt', 'w', encoding='utf-8') as file:
    for item in lines2:
        file.write(item.text.replace('\U0001f440', '-') + '\n')







