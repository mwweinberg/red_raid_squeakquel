import urllib

core1 = "http://paper.people.com.cn/rmrb/html/"
core2 = "/nw.D110000renmrb_"
core3 = "-01.htm"


#start all of these one below where you want to start because step 1 is +=1

#DON'T FORGET IF YOU CHANGE A VALUE HERE TO ALSO CHANGE IT AT THE END OF THE FOR
year_fixed = "2015"
month_fixed = "04"
day_fixed = "05"
story_fixed = "2"

#url = urllib.urlopen(core1+year+"-"+month_fixed+"/"+day_fixed+core2+year+month_fixed+day_fixed+"_"+story+core3).read()

url = core1+year_fixed+"-"+month_fixed+"/"+day_fixed+core2+year_fixed+month_fixed+day_fixed+"_"+story_fixed+core3

print url

urllib.urlretrieve(url, "text.html")
