# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:36:03 2016
@author: Jagannath Banerjee
Subject : Track the World Market
"""

import requests
import re
import datetime

# Function to pull out world market current standing
def checkMarket(marketName):
   "This prints a passed string into this function"
   worldMarketNameStart = re.search(marketName, requiredContent)
   startContent = int(worldMarketNameStart.start())
   endContent = startContent + 75
   #print(marketName, ":" ,startContent,":",endContent)
   rqdContent = requiredContent[startContent:endContent]
   
   newrqdContentStart = re.search('">', rqdContent)
   newrqdtStart = int(newrqdContentStart.start()) + 2
   newrqdContentend = re.search('</span>', rqdContent)
   newrqdtEnd = int(newrqdContentend.start())
   #print(marketName, "~" ,rqdContent[newrqdtStart:newrqdtEnd])
   
   marketValue = rqdContent[newrqdtStart:newrqdtEnd]
   return marketValue;

# Function to pull out world market todays changes
def marketDelta(marketName):

   "This prints a passed string into this function"
   worldMarketNameStart = re.search(marketName, requiredContent)
   
   startContent = int(worldMarketNameStart.start())
   endContent = startContent + 140
   rqdContent = requiredContent[startContent:endContent]
   #print("Main content:", rqdContent)
   
   newrqdContentStart = re.search('<td class="change">', rqdContent)
   newrqdtStart = int(newrqdContentStart.start()+40)
   newrqdtEnd = newrqdtStart + 150
   marketChange = rqdContent[newrqdtStart:newrqdtEnd]
   
   marketChangeContentStart = re.search('">', marketChange)
   marketChangeStart = int(marketChangeContentStart.start()) + 2
   marketChangeContentEnd = re.search('<', marketChange)
   marketChangeEnd = int(marketChangeContentEnd.start())
   
   #print(marketName,":" , marketChange[marketChangeStart:marketChangeEnd])
   marketDeltaChange = marketChange[marketChangeStart:marketChangeEnd]
   return marketDeltaChange ;

# Function to pull out world market current standing
def DomcheckMarket(DomMarketName):
   "This prints a passed string into this function"
   DomMarketNameStart = re.search(DomMarketName, DomRequiredContent)
   startContent = int(DomMarketNameStart.start())
   endContent = startContent + 100
   rqdContent = DomRequiredContent[startContent:endContent]
   #print("DomChekMarket:",rqdContent )
   newrqdContentStart = re.search('<span id=', rqdContent)
   newrqdtStart = int(newrqdContentStart.start()) + 5
   newrqdContentend = re.search('</span>', rqdContent)
   newrqdtEnd = int(newrqdContentend.start())+2
   
   rqdContentStart1 = rqdContent[newrqdtStart:newrqdtEnd]
   newrqdContentStart1 = re.search('">', rqdContentStart1)
   newrqdContentend1 = re.search('</', rqdContentStart1)
   
   DomNewStart = int(newrqdContentStart1.start()) +2 
   DomNewEnd = int(newrqdContentend1.start()) 
   
   #print(DomMarketName, "~" ,rqdContentStart1[DomNewStart:DomNewEnd])
   DomMarketValue = rqdContentStart1[DomNewStart:DomNewEnd]
   return DomMarketValue;

# Function to pull out domestic market todays changes
def DommarketDelta(DomMarketName):

   "This prints a passed string into this function"
   DomMarketNameStart = re.search(DomMarketName, DomRequiredContent)
   startContent = int(DomMarketNameStart.start())
   endContent = startContent + 140
   rqdContent = DomRequiredContent[startContent:endContent]
   #print(rqdContent)
   newrqdContentStart = re.search('<td><span class="bld chg"', rqdContent)
   newrqdtStart = int(newrqdContentStart.start()) + 5
   
   newrqdtEnd = newrqdtStart + 50
   
   rqdContentStart1 = rqdContent[newrqdtStart:newrqdtEnd]
   
   newrqdContentStart1 = re.search('">', rqdContentStart1)
   newrqdContentend1 = re.search('</', rqdContentStart1)
   
   DomNewStart = int(newrqdContentStart1.start()) +2 
   DomNewEnd = int(newrqdContentend1.start()) 
   
   #print(DomMarketName, "~" ,rqdContentStart1[DomNewStart:DomNewEnd])
   
   DomMarketDeltaChange = rqdContentStart1[DomNewStart:DomNewEnd]
   return DomMarketDeltaChange ;

#This is the main Para Master Contrlol. Function call are from here  
#today = datetime.date.today()
today = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

#print (today)
url = "https://www.google.com/finance"
urlContent = requests.get(url)

# Open a file
fileIntMarket = open("International_Market.txt", "a+")

DomMarketToTrack = ["Dow Jones","S&amp;P 500","Nasdaq"]
IntMarketToTrack = ["Shanghai","Nikkei 225","EURO STOXX 50","IPC","BSE Sensex",]

#Content Copy for International Market
worldMarketStart = re.search("<div id=markets>", urlContent.text)
startContent = int(worldMarketStart.start())

worldMarketEnd = re.search("<div id=currencies>", urlContent.text)
endContent = int(worldMarketEnd.start())

requiredContent = urlContent.text[startContent:endContent]

#Content Copy for Domestic Market
DomMarketStart = re.search('<table id="sfe-mktsumm">', urlContent.text)
DomStartContent = int(DomMarketStart.start())

worldMarketEnd = re.search('<div class="sfe-section clf"></div>', urlContent.text)
DomEndContent = int(worldMarketEnd.start())

DomRequiredContent = urlContent.text[DomStartContent:DomEndContent]

for index in range(len(IntMarketToTrack)):
   marketName = IntMarketToTrack[index]
   marketValue = checkMarket(marketName)
   marketDeltaChange = marketDelta(marketName)
   
   print(today,"~",marketName, "~",marketValue, "~",marketDeltaChange  )
   IntStringContent = today + "~" +"INT"+"~"+ marketName + "~" + marketValue + "~"+ marketDeltaChange
   fileIntMarket.write(IntStringContent)
   fileIntMarket.write("\n")
'''
for index in range(len(DomMarketToTrack)):
   DomMarketName = DomMarketToTrack[index]
   DomMarketValue = DomcheckMarket(DomMarketName)
   DomMarketDeltaChange = DommarketDelta(DomMarketName)
   
   print(today,"~",DomMarketName, "~",DomMarketValue, "~",DomMarketDeltaChange)
   DomStringContent = today + "~"+"DOM" +"~"+ DomMarketName + "~" + DomMarketValue + "~"+ DomMarketDeltaChange
   fileIntMarket.write(DomStringContent)
   fileIntMarket.write("\n")   
'''
# Close opend file
fileIntMarket.close()