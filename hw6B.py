import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Eileen.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
listElems = soup('a')
for x in range(0,7):
	print(listElems[17].get('href', None))
	html = urllib.request.urlopen(listElems[17].get('href', None), context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	listElems = soup('a')