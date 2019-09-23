'''
Subject :- n.wikipedia.org/wiki

Status :- Done

Author :- anoopk

Date :- 7/2/19
'''
import urllib
import csv
import sys
import re
import time
import random
#import os
#os.environ['http_proxy']=''
import urllib2
import ctypes
from HTMLParser import HTMLParser

x=0
y=0
temp_list = []
headers_list = [
    'URL','Title', 'Brand' ,'Location'
]
h = HTMLParser()

#def get_Html(url):
#	html_source = urllib.urlopen(url);
#	html_data = html_source.read()
#	return html_data


file = open(sys.argv[1], "r")
contant = file.read()
urls_listing = contant.split("\n")

#urls_listing=["http://vikings.wikia.com/wiki/Alfred"]
for url in urls_listing:
	#print url
	d = {"URL": url}
	key_list=[]
		
	if url:
	    
		html_source = urllib2.urlopen(url);
		html_of_url  = html_source.read()
		#print html_of_url
	

#----------------------------------------Title ---------------------------------------------------------------
		try:
			regex_title = '<h6 class="winners-tag">(.*?)</'
			if regex_title: 
				title_name = re.search(regex_title,html_of_url, re.DOTALL).group(1)
				title_name = re.sub("<.*?>","",title_name).strip() #https://www.youtube.com/watch?v=KCPDJ3YV6eU
				#title_name = re.sub(" \| StarWars.com","",title_name)

		        #print h.unescape(title_name)
			d['Title'] = h.unescape(title_name)
		except Exception as e:
			pass
#----------------------------------------Title ---------------------------------------------------------------
		try:
			regex_brand = '<h5 class="winners-tag">(.*?)</'
			if regex_brand: 
				brand_name = re.search(regex_brand,html_of_url, re.DOTALL).group(1)
				brand_name = re.sub("<.*?>","",brand_name).strip() #https://www.youtube.com/watch?v=KCPDJ3YV6eU
				#brand_name = re.sub(" \| StarWars.com","",brand_name)

		        #print h.unescape(brand_name)
			d['Brand'] = h.unescape(brand_name)
		except Exception as e:
			pass



#----------------------------------------Description-----------------------------------------------------------
		try:
			regex_des = '<p class="location">(.*?)</p>'
			if regex_des: 
				des_name = re.search(regex_des,html_of_url, re.DOTALL).group(1)
				des_name = re.sub("<.*?>","",des_name).strip()
                        #print "Type : it is executed"
			#print "Type : "+type(des_name.)	
			#print h.unescape(des_name)
			d['Location']=des_name


		except Exception as e:
			pass
#----------------------------------------Attributes ---------------------------------------------------------
		try:
			regex_att = '<th>(.*?)</th>'
			if regex_att: 
				att_name = re.findall(regex_att, html_of_url)
		        #print h.unescape(att_name)
		except Exception as e:
			pass

#----------------------------------------Keys ---------------------------------------------------------------
		#try:
		for att in att_name :
			#att = att.replace('(s):','')
			if att not in headers_list:
				headers_list.append(att)

#			att = re.sub(":","",att).strip()
			# regex='<h3 class="pi-data-label pi-secondary-font">Occupation(s):</h3>.*?</div>'
			regex='<th>'+ att + '</th>.*?<td>(.*?)</'
                        #regex = u' '.join((regex)).encode('utf-8').strip()
			# # print '\n\n\nRegex: ', regex
			html=''
			try:
				html = re.search(regex,html_of_url, re.DOTALL).group(1)
			except Exception as e:
				pass
			# # print html
			#regex_split = html.split('<br />')
			#key_list = []
			#for key in regex_split :
			keys = re.sub("<.*?>","",html).strip()
			keys = re.sub('\t','',keys)
			keys = re.sub('\n','',keys)
			keys = re.sub(',\s+',', ',keys)
			keys = re.sub(',$','',keys)
			keys=re.sub("&#39;","'",keys)
			#final_keys=h.unescape(str(keys.force_encoding('utf-8'))
			#print '\n\n Keys : ' + att + ': '+  keys
			#print '\n\n Final_Keys : ' + att + ': '+  final_keys
			
			#key_list.append(keys)
		# print key_list
                        try:
                            d[att] = h.unescape(keys)
                        except Exception as e:
                            d[att] = keys
                            y=y+1
                            print str(x)+" : "+str(y)
		# except Exception as e:
			# pass

		temp_list.append(d)
		x=x+1
		print x
                #print '\n\n'+ "Description : "+d['Description']

## print random.uniform(2, 5)
		time.sleep(random.uniform(1, 7))	

#file.close()



with open(sys.argv[2], 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, headers_list)
    dict_writer.writeheader()
    dict_writer.writerows(temp_list)

#if __name__ == "__main__":
