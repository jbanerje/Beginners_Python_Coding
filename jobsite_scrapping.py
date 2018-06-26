import urllib.request
with urllib.request.urlopen('https://www.google.com/finance') as response:
   html = response.read()
