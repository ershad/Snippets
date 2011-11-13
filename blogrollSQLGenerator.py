#!/usr/bin/env python
#
# blogrollSQLGenerator.py
# Author: Ershad K <ershad92@gmail.com>
# License: GPL Version 3

from BeautifulSoup import BeautifulSoup
import urllib2

url = raw_input('Enter blog url: ')
database = raw_input('Enter database name: ')

def convertToSQL(line):
    try:
        soup = BeautifulSoup(line)
        name = soup.contents[0].a.string
        link =  soup.find("a")["href"]

        try:
            target = soup.find("a")["target"]
        except:
            target = ''
 
        try:
            rel = soup.find("a")["rel"]
        except:
            rel = ''
        
        try:
            title = soup.find("a")["title"]
        except:
            title = ''

        sqlLine = 'INSERT into %s.wp_links (link_url, link_name, link_target, link_description, link_rel)' % database
        sqlLine += """ values ('%s','%s','%s','%s','%s');""" % (link, name, target, title, rel)

        print sqlLine
    except:
        pass

page = urllib2.urlopen(url)
pageContent = page.readlines()
index = 0
for line in pageContent:
    index += 1
    if line.find("<ul class='xoxo blogroll'>") > 0:
        while pageContent[index].find('</ul>') == -1:
             convertToSQL(pageContent[index])
             index += 1
