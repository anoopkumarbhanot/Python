import re
import csv
import time
import random
import urllib
import urllib2


movie_url = []
music_url = ['https://clios.com/awards/winners?page=1']
att_name = []
pg_num = 0
ul = []
x = 0

headers_list = [
    'URL',
    'Movie_url',
    'Movie_name',
    'Organisations',
    'City',
    'Award',
    'Year',
    ]
regex_url = ''
for url in music_url:
    # print url
    d = {"URL": url}
    key_list = []
    temp_list = []
    if url:
	z = {}
        html_source = urllib2.urlopen(url);
        html_of_url = html_source.read()
        # name=""
        # print html_of_url
        print "Main url:- "+url
        print "*---------------------------------------------------------------------------------------------*"
        # ----------------------------------------Attributes ---------------------------------------------------------
        try:
            regex_ul = '<a class="photo photo-column" href="(.*?)">'
            # print "It is executing"
            if regex_ul:
                ul = re.findall(regex_ul, html_of_url)
                #print ul
            # print 'start: ',att.startswith('<a href="/wiki/Category:'),': Parameter: ',att
        except Exception as e:
            pass

        for ull in ul:

            # ------------Get all info----------------
            
            if ull:
            
                #print "*---------------------------------------------------------------------------------------------*"
                h_s = urllib2.urlopen(ull)
                h_u = h_s.read()
                #print h_u
                d["Movie_url"] = ull
                #print "Main url:- "+url
                
                print "Movie url:- "+ull
                try:  # organisation_names
                    regex_org = '<h2 class="winners-tag">(.*?)</h2>'
                    if regex_org:
                        orgs = re.search(regex_org, h_u, re.DOTALL).group(1)
                        org = re.sub("<.*?>", "", orgs)
                        d["Organisations"] = org
                        #print "Organistion:- "+org
                except Exception as e:
                    pass

                try:  # city name
                    regex_cty = '<span class="location">(.*?)</span>'
                    if regex_cty:
                        city = re.search(regex_cty, h_u, re.DOTALL).group(1)
                        cty = re.sub("<.*?>", "", city)
                        d["City"] = cty
                        #print "City:- "+cty

                except Exception as e:
                    pass
                try:  # award <h1 class="winners-tag">
                    regex_awa = '<div class="winners-trophy (.*?)"></div>'
                    if regex_awa:
                        award = re.search(regex_awa, h_u, re.DOTALL).group(1)
                        awa = re.sub("<.*?>", "", award)
                        d["Award"] = awa
                        #print "Award:- "+awa

                except Exception as e:
                    pass

                try:  # Movie name
                    regex_mn = '<h1 class="winners-tag">(.*?)</h1>'
                    if regex_mn:
                        movie = re.search(regex_mn, h_u, re.DOTALL).group(1)
                        mn = re.sub("<.*?>", "", movie)
                        d["Movie_name"] = movie
                        print "Movie_name:- "+mn

                except Exception as e:
                    print e#

                try:  # year
                    regex_y = '<div class="year">(.*?)</div>'
                    if regex_y:
                        yr = re.search(regex_y, h_u, re.DOTALL).group(1)
                        #mn = re.sub("<.*?>", "", movie)
                        d["Year"] = yr
                        #print "Year:- "+yr

                except Exception as e:
                    print e                    

 
                try:  # Table data
                    regex_tb1 = '<dl class="winners-meta">(.*?)</div>'
                    parameters = []
                    if regex_tb1:

                        table1 = re.search(regex_tb1, h_u, re.DOTALL).group(1)
                        #tb1 = re.sub("<.*?>", "", table1)
                        parmeters = re.findall('<dt>(.*?)</dt>', table1)
                        #print table1
                        #print parameters

                        for w in parmeters:

                            y = re.sub("<.*?>", "", w)
                            if y not in headers_list:
                            
                                headers_list.append(y)
                                                          
                            regex_params = "<dt>.*?" + y + "</dt>.*?<dd>(.*?)</dd>"
                            if regex_params:
                                tab_vl = re.search(regex_params, table1, re.DOTALL).group(1)
                                #value =  re.sub("<.*?>", "", tab_vl)
                                # writing code for small table in upper half                          
                                d[y] = tab_vl
                                #print y,":- ", tab_vl
                except Exception as e:
                    print e
                

                x = x + 1
                print x
                #d = d[:] + [ull]
                temp_list.append(d.copy())
                print temp_list

                time.sleep(random.uniform(1, 7))

                
                #print d["URL"]
        pg_num = pg_num + 1
        name = 'Music_winners'
        print "*---------------------------------------Temp_list------------------------------------------------------*"
        print temp_list
with open('Awards_winners_final22.csv', 'wb') as output_file:

    dict_writer = csv.DictWriter(output_file, headers_list)
    dict_writer.writeheader()
    dict_writer.writerows(temp_list)

