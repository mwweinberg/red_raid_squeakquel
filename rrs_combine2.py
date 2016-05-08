from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv




core1 = "http://paper.people.com.cn/rmrb/html/"
core2 = "/nw.D110000renmrb_"
core3 = "-01.htm"
#start all of these one below where you want to start because step 1 is +=1
#DON'T FORGET IF YOU CHANGE A VALUE HERE TO ALSO CHANGE IT AT THE END OF THE FOR
year = 2013
month = 4
day = 5
story = 2

#initiates the dictionary to hold the output

holder = {}

def headliner(url, uid):
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
	holder[uid] = gold
	



for i in range(0,2):
	day += 1
	#turns day into a string
	day_fixed = str(day).zfill(2)
	
	for i in range(0,2):
		month += 1
		month_fixed = str(month).zfill(2)

		for i in range(0,2):
			
			year += 1
			year_fixed = str(year)
			
			for i in range(0,2):
		
				story += 1
				story_fixed = str(story)

				unique_ID = year_fixed+"-"+month_fixed+"-"+day_fixed+"-"+story_fixed

				#this is the url 
				url_name = core1+year_fixed+"-"+month_fixed+"/"+day_fixed+core2+year_fixed+month_fixed+day_fixed+"_"+story_fixed+core3				
				#this opens the url
				target_url = urllib.urlopen(url_name).read()
				print url_name
				print unique_ID
				print ""
				print ""
				print ""
				headliner(url_name, unique_ID)
			
			story = 2

		year = 2013

	#this resets the month to the starting point so it stays in the right 		range	
	month = 4

with open('rrs_csv.csv', 'wb') as f:
	w = csv.DictWriter(f, holder.keys())
	w.writeheader()
	w.writerow(holder)
