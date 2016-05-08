import urllib

core1 = "http://paper.people.com.cn/rmrb/html/"
core2 = "/nw.D110000renmrb_"
core3 = "-01.htm"


#start all of these one below where you want to start because step 1 is +=1

#DON'T FORGET IF YOU CHANGE A VALUE HERE TO ALSO CHANGE IT AT THE END OF THE FOR
year = 2015
month = 4
day = 5
story = 2



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

				#this is the url to send
				url = urllib.urlopen(core1+year_fixed+"-"+month_fixed+"/"+day_fixed+core2+year_fixed+month_fixed+day_fixed+"_"+story_fixed+core3).read()
			
			story = 2

		year = 2015

	#this resets the month to the starting point so it stays in the right 		range	
	month = 4
