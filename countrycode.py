#!/usr/bin/env python
#
# countrycode.py
# Author: Ershad K <ershad92@gmail.com>
# License: GPL Version 3

import urllib2
ccode = raw_input('Enter country code (Eg: +91): ')
page = urllib2.urlopen('http://www.countrycallingcodes.com/Reverse-Lookup.php?calling-code=%s' % ccode.replace('+',''))
pageContent = page.readlines()

flag = 0
for line in pageContent:
    if line.find("""<TABLE BORDER='0'""") >= 0:
        cline = line
        flag = 1

if flag is 0:
    print 'Invalid country code.'
    exit(1)
    
countryName = cline.split('<i>')[1].split('<')[0]
print countryName

headers = { 'User-Agent' : 'Mozilla/5.0' }
req = urllib2.Request('http://www.google.com/search?q=%s+time' % countryName, None, headers)
timePageContent = urllib2.urlopen(req).readlines()

tline = ''
for line in timePageContent:
    if line.find('<b>Time</b> in <b>') >= 0:
        tline = line

endIndex = tline.find('<b>Time</b> in <b>') - 3
startIndex = tline.find('e:medium">') + len('e:medium">')
timeString = ''
while startIndex <= endIndex:
    timeString += tline[startIndex]
    startIndex += 1

timeString = timeString.replace('<b>','')
timeString = timeString.replace('</b>','')
print 'Time: ' + timeString
