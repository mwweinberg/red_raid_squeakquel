from bs4 import BeautifulSoup
import urllib


#sets the URLs
h1 = "test_eng.html"
h2 = "test2_eng.html"


# need to either figure out how to skip "None" results or turn search_all into a string



def headliner(url):
	soup = BeautifulSoup((open(url)), "lxml")
	head1 = soup.find_all(['h1','h2','h3'])
	head2 = soup.h2.string
	
	head3 = soup.h3.string

	print head1
	
	print head1[0].get_text()
	
	#print head1[1].get_text()
	#print head2[2].get_text()
	
	
	#print head2
	
	#print head3
	
	print ""

headliner(h1)
	
