from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


#initiates the dictionary to hold the output

holder = {}


#sets the URLs
h1 = 'http://paper.people.com.cn/rmrb/html/2016-05/06/nw.D110000renmrb_20160506_2-01.htm'




#final version of this function will take two arguments: the URL and the unique identifier for the dict
def headliner(url):
	this_url = urllib.urlopen(url).read()
	#creates a new BS holder based on the URL
	soup = BeautifulSoup(this_url, 'lxml')
	#head1 is all of the headlines with their tags
	head1 = soup.find_all(['h1','h2','h3'])
	
	#gets all the encoding right	
	
	head1_fixed = str(head1)
	soup1 = BeautifulSoup(head1_fixed, 'lxml')
	gold = soup1.text.decode("unicode-escape").encode("utf-8")
	
	
	#appends a new pair in holder with the URL as they first part and head1 as 			the second
	holder["key"] = gold


	
	
	
#calls the function three times
headliner(h1)



#convert holder to a CSV and save it as a file. You need to change the formatting in calc and also flip X and Y axis

with open('rrs_csv.csv', 'wb') as f:
	w = csv.DictWriter(f, holder.keys())
	w.writeheader()
	w.writerow(holder)


