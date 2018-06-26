#Learning regex
import re
strInput = "Hello World"

match = re.search("W", strInput)

# If-statement after search() tests if it succeeded
if match:                      
    print ('found', match.group()) ## 'found word:cat'
else:
    print ('did not find')
