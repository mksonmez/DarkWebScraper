import requests
#import pandas as pd
from bs4 import BeautifulSoup

page = requests.get('URL')
soup = BeautifulSoup(page.content, 'html.parser')

#ambien = soup.find(id='footer')

#class_items = ambien.find_all(class_ = 'container')
#target = soup.find('home-default-top-sellers')
guns_id = soup.find(id='box_price')
guns_a = guns_id.find_all('a' + '\n')
#items = div.find_all('span')


print(guns_a)


"""
all_data = pd.DataFrame(
	{
		one = '',
		two = '', 
		three = ''
	})


all_data.to_csv('all_data.csv')
"""
