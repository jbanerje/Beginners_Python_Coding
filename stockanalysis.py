import re
import urllib

#Grabbing the html data
url = "http://finance.yahoo.com/q/hp?s=CTSH&a=05&b=19&c=1998&d=06&e=7&f=2016&g=w"
data= urllib.urlopen(url).read()
urlData = data.decode("utf-8")
#print (urlData)

#search for price - Parsing the required string
searchPrice = re.search('<td class="yfnc_tabledata1" align="right">',urlData)
start = searchPrice.start()
end = start + 48
newString= urlData[start:end]
#print (newString)

#Parsing the amount string
searchPrice1 = re.search('"right">',newString)
start1 = searchPrice1.end()
NewString1 = newString[start1:]
print(NewString1)

searchPrice2 = re.search('<',NewString1)
start2 = searchPrice2.end()
NewString2 = newString[start2:]
print(NewString2)
    
