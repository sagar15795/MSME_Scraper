import urllib2
from bs4 import BeautifulSoup
import json

class Scraper:
    def webscraper(self):
        global count
        url='http://msme.gov.in/Web/Portal/Media.aspx'
        print 'Now scraping %s '%(url)
        arr =[]
	dict = {}
	m=1
        soup = BeautifulSoup( urllib2.urlopen(url).read() )
	x= soup.find("table",{"cellpadding":"8" ,"cellspacing":"3" ,"width":"100%", "border":"0" ,"class":"td-border1"} )
	description=''
	image_url=''	
	for i in x.find_all("tr"):		
		if (m==2):
			m=1
			description= i.find("td",class_="home-contentNew").get_text()
			description=description[43:-34]
			dict=return_dict(description,image_url)
			arr.append(dict)
		else:
			m=m+1
			z= i.find("td",{"align":"center"})
			image_url= z.find("img").get("src")
			image_url="http://msme.gov.in"+image_url[5:]
			
	return arr		
            
def return_dict(name,code):
    global count
    dict = {}
    dict['description'] = name
    dict['image_url'] =code
    try:
        print ' %s : %s'%(name,code)
    except:
        pass
    return dict

def main():
    scrape = Scraper()
    arr1 = scrape.webscraper()
    with open("file0.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    
