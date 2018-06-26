import re
import urllib

#Grabbing the html data
url = "https://www.google.com/finance?q=CTSH"
data= urllib.urlopen(url).read()
urlData = data.decode("utf-8")

#search for price - Parsing the required string
searchPrice = re.search('itemprop="price"',urlData)
start = searchPrice.start()
end = start + 40

newString= urlData[start:end]


#Parsing the amount string
searchPrice1 = re.search('content="',newString)
start1 = searchPrice1.end()
NewString1 = newString[start1:]
print(NewString1)

    
