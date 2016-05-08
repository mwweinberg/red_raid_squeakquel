from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv
#pickle is to save the dictionary
import pickle

#initiates the dictionary to hold the output

holder = {}


#sets the URLs
h1 = "test_eng.html"
h2 = "test2_eng.html"
h3 = "test3_eng.html"

#final version of this function will take two arguments: the URL and the unique identifier for the dict
def headliner(url):
	#creates a new BS holder based on the URL
	#TODO: this will need to be slightly fancier when you are importing an actual
		#URL
	soup = BeautifulSoup((open(url)), "lxml")
	#head1 is all of the headlines with their tags
	head1 = soup.find_all(['h1','h2','h3'])
	
	#appends a new pair in holder with the URL as they first part and head1 as 			the second
	holder[url] = head1
	
	
#calls the function three times
headliner(h1)
headliner(h2)
headliner(h3)

#prints out holder for troubleshooting purposes

print holder


#convert holder to a CSV and save it as a file. You need to change the formatting in calc and also flip X and Y axis

with open('rrs_csv.csv', 'wb') as f:
	w = csv.DictWriter(f, holder.keys())
	w.writeheader()
	w.writerow(holder)

#save the dictionary
#I don't know if this works
pickle.dump(holder, open("rrs_pickledump", "wb"))
