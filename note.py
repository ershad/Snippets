#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       note.py
#       
#       Copyright 2011 Ershad K <ershad92@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import os
import time

#Configurations

username = "Ershad K"
email = "ershad92@gmail.com"
email = '<' + email + '>'
editor = "emacsclient "


# Every note must be in a format like

# Line 1: User Name <email ID>
# line 2: Date: dd-mm-yy HH:MM:SS (Of publishing)
# Line 3: -----------------------------------------------------------
# Line 4:
# Line 5: <note start here.....>


os.system (editor + " draft.tmp")

temp  = open("draft.tmp", "r")
lines = temp.readlines()
temp.close()
os.system("rm draft.tmp")

t = time.localtime()
year = str(t.tm_year)
month = str(t.tm_mon)
day = str(t.tm_mday)
hour = str(t.tm_hour)
minute = str( t.tm_min)
sec = str(t.tm_sec)

if len(month) == 1:
    month = "0" + month
    
if len(day) == 1:
    day = "0" + day

if len(hour) == 1:
    hour = "0" + hour

if len(minute) == 1:
    minute = "0" + minute

if len(sec) == 1:
    sec = "0" + sec
        
timeStamp = year + month + day + hour + minute + sec

header =  username + ' ' + email + '\n'
header += 'Date: ' + day + '-' + month + '-' + year
header += '  ' + hour + ':' + minute + ':' + sec + '\n'
header += '-' * 50
header += '\n\n'

note = open(timeStamp, "w")
note.write(header)

for line in lines:
    note.write(line)
note.close()

print "Note written to : " + timeStamp
