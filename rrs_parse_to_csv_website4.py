from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


#initiates the dictionary to hold the output

holder = {}


#sets the URLs
h1 = urllib.urlopen('http://paper.people.com.cn/rmrb/html/2016-05/06/nw.D110000renmrb_20160506_2-01.htm').read()
h2 = urllib.urlopen('http://paper.people.com.cn/rmrb/html/2016-05/06/nw.D110000renmrb_20150506_2-01.htm').read()
#h3 = "test3_eng.html"



#final version of this function will take two arguments: the URL and the unique identifier for the dict
def headliner(url):
	#creates a new BS holder based on the URL
	soup = BeautifulSoup(url, 'lxml')
	#head1 is all of the headlines with their tags
	head1 = soup.find_all(['h1','h2','h3'])
	print unicode(head1)
	
	#appends a new pair in holder with the URL as they first part and head1 as 			the second
	#TODO: the key has to be the uniqueID
	
	holder["fart"] = head1
	print holder

def headliner1(url):
	#creates a new BS holder based on the URL
	soup = BeautifulSoup(url, 'lxml')
	#head1 is all of the headlines with their tags
	head1 = soup.find_all(['h1','h2','h3'])
	print unicode(head1)
	
	#appends a new pair in holder with the URL as they first part and head1 as 			the second
	#TODO: the key has to be the uniqueID
	
	holder["fart1"] = head1
	print holder
	
	
	
#calls the function three times
headliner(h1)
headliner1(h2)
#headliner(h3)

#prints out holder for troubleshooting purposes

#print holder


#convert holder to a CSV and save it as a file. You need to change the formatting in calc and also flip X and Y axis

with open('rrs_csv.csv', 'wb') as f:
	w = csv.DictWriter(f, holder.keys())
	w.writeheader()
	w.writerow(holder)


