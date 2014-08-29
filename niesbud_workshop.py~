import urllib2
from bs4 import BeautifulSoup
import json

class Scraper:
    def webscraper(self):
        url='http://niesbud.nic.in/workshop.htm'
        print 'Now scraping %s '%(url)
        arr =[]
	dict = {}
	soup = BeautifulSoup( urllib2.urlopen(url).read() )
	i=soup.find("div",{"id":"jaipur-workshop"} )
	#print i.find_next("div").find_next("div").get_text()
	title=''
        des=''
	title= i.find_next("div").get_text()
	#print "----------------------------------------"
        des=i.find("p",{"align":"justify"}).get_text()
	dict=return_dict(des,title)
	arr.append(dict)
	i=soup.find("div",{"id":"workshop_on_Brainstorming"} )
	#print "-------------------------------------------"
	title= i.find_next("h2").get_text()
	#print "-------------------------------------------"
	des= i.find_next("p").get_text()
	dict=return_dict(des,title)
	arr.append(dict)        
	return arr
       
def return_dict(des,title):
    global count
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
    with open("file2.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    
