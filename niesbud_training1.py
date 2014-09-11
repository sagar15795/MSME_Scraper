import urllib2
from bs4 import BeautifulSoup
import json


class Scraper:
    def webscraper(self):
        url='http://www.msmetraining.gov.in/LinkImplementingAgency.aspx'
        print 'scraping %s '%(url)
        arr =[]
	dict = {}
	url_dict={}
	soup = BeautifulSoup( urllib2.urlopen(url).read() )
	i=soup.find("table",{"class":"MyGridView"} )
	i1=0
	for m in i.find_all("tr"):
		if(i1==0):
			i1=1
			
		else: 
			l=m.find_next("td")
			t1=l.get_text()
			m11=l.find_next("td")
			url1="http://www.msmetraining.gov.in/"+m11.find_next("a").get("href")
			t2=m11.get_text()
			t3=l.find_next("td").find_next("td").get_text()
			t4=l.find_next("td").find_next("td").find_next("td").get_text()
			t5=l.find_next("td").find_next("td").find_next("td").find_next("td").get_text()
			t6=l.find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
			t7=l.find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
			t1=' '.join([segment for segment in t1.split()])
			t2=' '.join([segment for segment in t2.split()])
			t3=' '.join([segment for segment in t3.split()])
			t4=' '.join([segment for segment in t4.split()])
			t5=' '.join([segment for segment in t5.split()])
			t6=' '.join([segment for segment in t6.split()])
			t7=' '.join([segment for segment in t7.split()])
			#print url1
			url_dict=urlinside(url1)
			dict=return_dict(t1.strip(),t2.strip(),t3.strip(),t4.strip(),t5.strip(),t6.strip(),t7.strip(),url_dict)
			arr.append(dict)
	return arr
	
def urlinside(url1):
	print 'Now Going in inside %s'%(url1)
	arr =[]
	dict = {}
	soup = BeautifulSoup( urllib2.urlopen(url1).read() )
	i=soup.find("table",{"class":"MyGridView"} )
	i1=-1
	for m in i.find_all("tr"):
		if(i1==-1):
			i1=0
			
		else: 
			l=m.find_next("td")
			t1=l.get_text()
			m11=l.find_next("td")
			t2=m11.get_text()
			t3=l.find_next("td").find_next("td").get_text()
			t4=l.find_next("td").find_next("td").find_next("td").get_text()
			t5=l.find_next("td").find_next("td").find_next("td").find_next("td").get_text()
			t6=l.find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
			t7=l.find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").find_next("td").get_text()
			t1=' '.join([segment for segment in t1.split()])
			t2=' '.join([segment for segment in t2.split()])
			t3=' '.join([segment for segment in t3.split()])
			t4=' '.join([segment for segment in t4.split()])
			t5=' '.join([segment for segment in t5.split()])
			t6=' '.join([segment for segment in t6.split()])
			t7=' '.join([segment for segment in t7.split()])
			dict=return_dict_inside(t1.strip(),t2.strip(),t3.strip(),t4.strip(),t5.strip(),t6.strip(),t7.strip())
			arr.append(dict)
		i1=i1+1
	print arr
	return arr

def return_dict(sno,iacode,ianame,Add,Ph,Eid,Website,url_inside):

    dict = {}
    dict['sno'] = sno
    dict['iacode']=iacode
    dict['ianame']=ianame
    dict['Address'] = Add
    dict['Phone']=Ph
    dict['Email']=Eid
    dict['Website']=Website
    dict['Inside_data']=url_inside
    try:
	print ''
	#print '++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
        #print ' %s |||||| %s ||||||||| %s|||||| %s ||||||||| %s|||||||||%s|||||| %s ||||||%s'%(sno,iacode,ianame,Add,Ph,Eid,Website,url_inside)
    except:
        pass
    return dict
def return_dict_inside(sno,tccode,tcname,Add,Ph,Eid,Website):

    dict = {}
    dict['sno'] = sno
    dict['tccode']=tccode
    dict['tcname']=tcname
    dict['Address'] = Add
    dict['Phone']=Ph
    dict['Email']=Eid
    dict['Website']=Website

    try:
	print ''
	#print '--------------------------------------------------------------------------------'
        #print ' %s |||||| %s ||||||||| %s|||||||||%s|||||| %s ||||||||| %s|||||||||%s'%(sno,tccode,tcname,Add,Ph,Eid,Website)
    except:
        pass
    return dict

def main():
    scrape = Scraper()
    arr1=scrape.webscraper()
    #del arr1[-2:]
    #del arr1[6]
    #print arr1
    with open("niesbud_training1.txt", "w") as f:
        f.write(json.dumps(arr1))

if __name__ == '__main__':
    main()
    #print gen_favicon('flipkart')

