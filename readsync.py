#!/usr/bin/env python
#
# readsync.py
# Author: Ershad K <ershad92@gmail.com>
# License: GPL Version 3

import urllib2
import time

username = ''
password = ''
apikey = ''

header = """<!DOCTYPE html>\n<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />"""
header += """\n<title>Reading List</title>\n</head>\n<body>\n<h1>Articles</h1>\n<ul> \n"""

footer = """\n</ul>\n</body>\n</html>\n"""

while True:
    url = "http://readitlaterlist.com/v2/get?username=%s&password=%s&apikey=%s&format=xml" % (username, password, apikey)
    page = urllib2.urlopen(url)
    pageContent = page.readlines()

    lines = []
    for line in pageContent:
        if line.find('<title>') >= 0 or line.find('<url>') >= 0:
            tagRemoved = line.replace('<title>','')
            tagRemoved = tagRemoved.replace('</title>','')
            tagRemoved = tagRemoved.replace('<url>','')
            tagRemoved = tagRemoved.replace('</url>','')
            tagRemoved = tagRemoved.replace('\n','')
            lines.append(tagRemoved.replace('\t',''))

    i = 0
    htmlbody = ''
    while i < len(lines)-1:
        content = """<li><a href="%s">%s</a></li>\n""" % (lines[i+1], lines[i])
        htmlbody += content
        i += 2

    html =  header + htmlbody + footer
    htmlfile = open('index.html', 'w')
    htmlfile.write(html)
    htmlfile.close()

    time.sleep(60 * 5)

