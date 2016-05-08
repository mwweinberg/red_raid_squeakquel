from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


holder = {}  

url = urllib.urlopen('http://paper.people.com.cn/rmrb/html/2016-05/06/nw.D110000renmrb_20160506_2-01.htm').read()

soup = BeautifulSoup(url, 'lxml')

head1 = soup.find_all(['h1','h2','h3'])

print head1
print ""

head1_fixed = str(head1)

soup1 = BeautifulSoup(head1_fixed, 'lxml')

gold = soup1.text.encode("utf-8").decode("unicode-escape")
print(soup1.text.encode("utf-8").decode("unicode-escape"))
print "***"
print gold
print ""
print ""

holder["key"] = gold


print holder["key"]

print(bs4.__version__)



