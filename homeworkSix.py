from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_35653.html"
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

totalComments = 0
# Retrieve all of the table data tags
tags = soup('tr')
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)
    print('Contents:', tag.contents[1])
    print(type(tag.contents[1]))
    for num in re.findall('([0-9]+)', str(tag.contents[1])):
    	totalComments += int(num)
print(totalComments)