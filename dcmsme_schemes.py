import urllib2
from bs4 import BeautifulSoup
import json


class Scraper:
    def webscraper(self):
        url='http://dcmsme.gov.in/schemes/sidoscheme.htm'
        print 'scraping %s '%(url)
        arr =[]
	dict = {}
	soup = BeautifulSoup( urllib2.urlopen(url).read() )
	i=soup.find("ol" )
	#print i
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
		#print m.find_next("p").find_next("p").get_text()
	#for m in i.find_all("p"):
	#	print "------------------------------------------------------------------------------------"
	#	print m.get_text()
	'''
	title=''
	data=''
	for m in i.find_all("h3"):
		title=(m.get_text()).strip()
		data=(m.find_next("p").get_text()).strip()
		data=' '.join([segment for segment in data.split()])
		dict=return_dict(data,title)
		arr.append(dict)
	return arr
	'''

def removeAfter(string, suffix):
    return string[:string.index(suffix) + len(suffix)]
       
def return_dict(des,title,url):

    dict = {}
    dict['description'] = des
    dict['title']=title
    dict['url']=url
    try:
        print ' %s |||||| %s ||||||||| %s'%(des,title,url)
    except:
        pass
    return dict

def main():
    scrape = Scraper()
    arr1 = scrape.webscraper()
    del arr1[-2:]
    #del arr1[6]
    #print arr1
    with open("dcmsme_schemes.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    #print gen_favicon('flipkart')

