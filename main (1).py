import requests
from bs4 import BeautifulSoup

def searchiceland(searchitem):
  
  temp = 'https://www.iceland.co.uk/search?q=' + searchitem
  
  res = requests.get(temp)
  
  soup = BeautifulSoup(res.content, 'html.parser')
  find = soup.find_all('span', {'class': 'product-sales-price'})
  find2 = soup.find_all('div', {'class': 'product-name'})
  
  finds = []
  
  for i in range(0,len(find)-1):
    
    title = str(find2[i:i+1])
    
    x = title.find('<span>')
    y = title.find('</span>')
    
    title = title[x+6:y]
    
    price = str(find[i:i+1])
  
    x1 = price.find('<span>')
    y1 = price.find('</span>')
  
    price = price[x1+7:y1]
  
    finds.append([title,float(price)])
  
  finds.sort(key=lambda x: x[1])
  
  return finds


def searchtesco(searchitem):
    
  temp = 'https://www.tesco.com/groceries/en-GB/search?query=' + searchitem

  print(temp)
  
  res = requests.get(temp)

  print("TERDT")
  
  soup = BeautifulSoup(res.content, 'html.parser')
  
  find2 = soup.find_all('div', {'class': 'product-details--wrapper'})
  

  print(find2)

print(searchiceland("paper"))

