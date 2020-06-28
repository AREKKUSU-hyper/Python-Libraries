import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')    
print('Retrieving', url)
data = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
# counts = tree.findall('.//count') # use an XPath selector string to look through the entire tree of XML for any tag named 'count'
comments = tree.findall('comments/comment')
count=0
sum=0
for comment in comments:
    num=int(comment.find('count').text)
    count+=1
    sum+=num

print('Count:', count)
print('Sum:', sum)

# Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
# Retrieved 4189 characters
# Count: 50
# Sum: 2...