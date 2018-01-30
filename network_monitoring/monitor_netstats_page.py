from selenium import webdriver
from bs4 import BeautifulSoup
import time, re, string
import time


#def import_to_google():
	#add import function
	
#def remove_repeated_data():
	#every 30 seconds we get about 40 block times, but only 7-8 blocks are new. Need a way to skip same data and not log it again
	
#def get_uptime():
#	uptime_class = ## Add clas name for uptime section
#	uptime = soup.body.find('span',  attrs={ 'class' : uptime_class})
	
##def check_for_changes():
	##

from splinter.browser import Browser

browser = webdriver.Firefox()

def get_data_snapshot():
	url = "https://sokol-netstat.poa.network/"
	browser.get(url)
	
	time.sleep(30)
	
	soup=BeautifulSoup(browser.page_source, "html.parser")
	
	number_of_nodes = soup.body.find('span',  attrs={ 'class' : 'small-value'})
	block_time = soup.body.find('span',  attrs={ 'class' : 'ng-binding ng-isolate-scope big-details'})
	t = number_of_nodes.text
	print "Number of active nodes is: " +t
	
	#print block_time
	
	for d in block_time['data'].split(','):
		print d
	
	def get_average_block_time():
		data_class = 'big-details ng-binding'
		data = soup.body.find_all('span',  attrs={ 'class' : data_class})
		i = 1
		for d in data:
			#print d
			d1 = d.text
			if i == 3:
				print "Average Block time is: "+d1
			i=i+1
	
	get_average_block_time()
	
a = 0
while a == 0: ## Run until interrupted
	get_data_snapshot()