from selenium import webdriver
from selenium.webdriver.common.keys import Keys                                     
from selenium.webdriver.support.ui import Select  
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome(executable_path='/home/ruslan/drivers/chromedriver') 



BASE_STR = 'https://duckduckgo.com/?q='

END_BASE_STR = '&t=h_&iar=images&iax=images&ia=images'





class  Search_images:
	def __init__(self,name_collections,deep):
		self.name_collections = name_collections
		self.deep = deep
		self.collections = []


	def get_images(self,name):
		page = browser.get(BASE_STR  +  name.strip().replace(' ','+') + END_BASE_STR )
		time.sleep(0.5)
		soup=BeautifulSoup(browser.page_source)
		
		for block_image  in  soup.findAll('div',class_="tile"):
			data = {}
			img = block_image.find('img')
			if img:
				data['data-src'] = img.get('data-src')
			if (block_image.find('div',class_='tile--img__dimensions')):
				data['original_size'] =   block_image.find('div',class_='tile--img__dimensions').text
			block_data =  block_image.find('a', class_='tile--img__sub')
			if  block_data:
				data['link'] = block_data.get('href')
				data['descriptions'] = block_data.find('span',class_='tile--img__title').text
			# domain =  block_data.find('span.tile--img__domain')
			print(data)
			self.collections.append(data)
		





if __name__=='__main__':
	a = Search_images("Поиск по фото",1)
	images =a.get_images("Собака")
	print(a.collections)
	print(images)