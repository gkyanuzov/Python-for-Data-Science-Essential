from bs4 import BeautifulSoup
import urllib.request
import re
from IPython.display import HTML

r = urllib.request.urlopen('https://dsport.bg/proektat-za-rekonstrukcia-na-balgarska-armia-poluchi-odobrenieto-na-edna-ot-komisiite-v-sos~124430.html').read()
soup = BeautifulSoup(r, 'lxml')

print(type(soup))
print(soup.prettify()[:100])
# get all links
for link in soup.find_all('a'):
    print(link.get('href'))
# get all text
print(soup.get_text())

print(soup.prettify()[:1000])

# get all links with http
for link in soup.find_all('a', attrs={'href':re.compile('http')}):
    print(link)

# add links to file
file = open('parsed_data.txt', 'w', encoding='utf-8')
for link in soup.find_all('a', attrs={'href':re.compile('http')}):
    soup_link = str(link)
    print(soup_link)
    file.write(soup_link)
file.flush()
file.close()

