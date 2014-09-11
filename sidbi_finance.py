import urllib2
from bs4 import BeautifulSoup,Comment
import re
import json


class Scraper:
    def webscraper(self):
        url='http://sidbi.in/?q=finance-upgradation-modernisation#overlay-context=front-page%3Fq%3Dfront-page'
        print 'scraping %s '%(url)
        arr =[]
	dict = {}
	soup = BeautifulSoup( urllib2.urlopen(url).read() )
	i=soup.find("div",{"class":"field-item even"} ).find_next("div",{"class":"field-item even"} ).find_next("ul")
	for m in i.find_all("li"):
		z=m.find("h4").get_text()
		l="http://sidbi.in"+m.find("h4").find("a").get("href")
		dict=return_dict(z,l)
		arr.append(dict)
	#print arr
	return arr
	#print i
	#for m in  
'''
	for m in i.find_all("li"):
		print "------------------------------------------------------------------------------------"
		z=(m.find_next("p").get_text()).strip()
		x= m.find_next("p").find_next("b").get_text()
		x=' '.join([segment for segment in x.split()])
		i=m.find_next("p").find_next("a").get("href")
                
		if z=='':
			z= m.find_next("div").get_text()
			x= m.find_next("div").find_next("a").find_next("b").get_text()	
			x=' '.join([segment for segment in x.split()])
			i=m.find_next("div").find_next("a").find_next("a").get("href")
		if i[0]=="/":
			i="http://dcmsme.gov.in"+i
 		z=' '.join([segment for segment in z.split()])
		m=z.split()
		m=m[:-2]
		z=" ".join(m)
		if 'Participation in the International Exhibitions/ Fairs ' in z:
		 		z=removeAfter(z,'Participation in the International Exhibitions/ Fairs ')
				m=z.split()
				m=m[:-9]	
				#print " ".join(m)
		dict=return_dict(z,x,i)
		arr.append(dict)
		
	return arr
'''
def removeAfter(string, suffix):
    return string[:string.index(suffix) + len(suffix)]
       
def return_dict(title,url):

    dict = {}
    dict['title']=title
    dict['url']=url
    try:
        print ' |||||| %s ||||||||| %s'%(title,url)
    except:
        pass
    return dict

def main():
    scrape = Scraper()
    arr1 = scrape.webscraper()
    with open("sidbi_finance.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    
