import urllib2
from bs4 import BeautifulSoup
import json


class Scraper:
    def webscraper(self):
        url='http://niesbud.nic.in/training.htm'
        print 'scraping %s '%(url)
        arr =[]
	dict = {}
	soup = BeautifulSoup( urllib2.urlopen(url).read() )
	i=soup.find("div",{"class":"module"} )
	title=''
	data=''
	for m in i.find_all("h3"):
		title=m.get_text()
		data=m.find_next("p").get_text()
		dict=return_dict(data,title)
		arr.append(dict)
	return arr
       
def return_dict(des,title):

    dict = {}
    dict['description'] = des
    dict['title']=title
    try:
        print ' %s | %s '%(des,title)
    except:
        pass
    return dict

def main():
    scrape = Scraper()
    arr1 = scrape.webscraper()
    with open("file1.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    #print gen_favicon('flipkart')

