import urllib2
from bs4 import BeautifulSoup
import json

class Scraper:
    def webscraper(self):
        global count
        url='http://niesbud.nic.in/pressnew.html'
        print 'scraping %s '%(url)
        arr =[]
	dict = {}
	m=1
        soup = BeautifulSoup( urllib2.urlopen(url).read() )
	for i in soup.find_all("td",{"class":"press_relaese"} ):
		x= i.find("a")
		#print '-----------------------------------------'
		url_goto=''
		url_goto='http://niesbud.nic.in/'+x.get('href')
		text1=''
		text2=''
		url_image=''
		count=0
		for m in i.find_all('b'):
			count=count+1
			if count == 1:
      				text1=m.get_text()
			else:
				text2=m.get_text()
		if text2=='':
			url_image= 'http://niesbud.nic.in/'+i.find("img").get("src")
			dict=return_dict("null",url_image,text1,url_goto)
			arr.append(dict)
		else:
			dict=return_dict(text2,"null",text1,url_goto)
			arr.append(dict)
	return arr 

        
def return_dict(des,image_url,date,url_goto):
    global count
    dict = {}
    dict['description'] = des
    dict['date']=date
    dict['url_goto']=url_goto
    dict['image_url'] =image_url
    try:
        print ' %s | %s | %s | %s'%(des,image_url,date,url_goto)
    except:
        pass
    return dict

def main():
    scrape = Scraper()
    arr1 = scrape.webscraper()
    with open("file.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    
