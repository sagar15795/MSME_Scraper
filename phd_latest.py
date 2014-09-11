import urllib2
from bs4 import BeautifulSoup
import json


class Scraper:
    def webscraper(self):
        url='http://www.phdcci.in/'
        print 'scraping %s '%(url)
        arr =[]
	dict = {}
	soup = BeautifulSoup( urllib2.urlopen(url).read() )
	i=soup.find("div",{"class":"newsticker-jcarousellite"})
	#print i
	#print "love"
	for m in i.find_all("li"):
		z=m.get_text()
		z=' '.join([segment for segment in z.split()])
		print z
		dict["news"]=z
		arr.append(dict)
	print arr
	return arr

def main():
    scrape = Scraper()
    arr1=scrape.webscraper()
    #del arr1[-2:]
    #del arr1[6]
    #print arr1
    with open("phd_latest.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    #print gen_favicon('flipkart')

