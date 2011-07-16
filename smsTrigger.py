#!/usr/bin/env python
# 
# getnew.py
# Author: Ershad K <ershad92@gmail.com>


import gammu
import time
import os

def checkAndStart(str1, str2):
        if str1 == "start" or str1 == "Start" or str1 == "START":
                num = str2[:4]
                num += '---'
                num += str2[-3:]
                os.system("pkill -9 eog") #Killing eog that displayed an image
                                          # with number in full screen mode 
                os.system("clear")
                os.system("figlet -f banner Thank you,")
                print
                print
                numspaced = ""
                for i in num:
                        numspaced += i + " "
                print
                print
                os.system("figlet -f big %s -w 500" % numspaced)
                print "\n\nThe presentation will start in 5 seconds!\n\n\n"
                time.sleep(5)
                os.system("ooimpress -show Presentation.odp")
                exit(0)

sm = gammu.StateMachine()
sm.ReadConfig()
print "Init: GSM Device (Connecting..)"
sm.Init()
print "Success: GSM Device Connected!"


while True:
        #        print "Started new cycle!"
	status = sm.GetSMSStatus()

	remain = status['SIMUsed'] + status['PhoneUsed'] + status['TemplatesUsed']

	sms = []
	start = True
        
        count = 0
        timecount = time.time()
        command = ""
        number = ""
	try:
                while remain > 0:
                        if start:
                        
                                cursms = sm.GetNextSMS(Start = True, Folder = 0)
                                command = cursms[0]['Text']
                                number = cursms[0]['Number'][-10:]
                                checkAndStart(command, number)
                                start = False
                        else:
                                cursms = sm.GetNextSMS(Location = cursms[0]['Location'], Folder = 0)
                                command = cursms[0]['Text']
                                number = cursms[0]['Number'][-10:]
                                checkAndStart(command, number)

        	try:
                        remain = remain - len(cursms)
                        sms.append(cursms)
                except:
                        pass
	except gammu.ERR_EMPTY:
    		pass

        time.sleep(1)
