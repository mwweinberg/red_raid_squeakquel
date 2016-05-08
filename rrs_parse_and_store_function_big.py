from bs4 import BeautifulSoup
import urllib

#initiates the dictionary to hold the output

holder = {}


#sets the URLs
h1 = "test_eng.html"
h2 = "test2_eng.html"


def headliner(url):
	soup = BeautifulSoup((open(url)), "lxml")
	#head1 is all of the headlines with their tags
	head1 = soup.find_all(['h1','h2','h3'])
	
	#appends a new pair in holder with the URL as they first part and head1 as 			the second
	holder[url] = head1
	
	
#calls the function twice
headliner(h1)
headliner(h2)

#prints out holder for troubleshooting purposes

print holder
