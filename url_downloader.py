import urllib2
import argparse
from bs4 import BeautifulSoup
import codecs
import chardet

parser = argparse.ArgumentParser(description='Process word to translate')
parser.add_argument('word', type=str, help='word to be translated')
args = parser.parse_args()

url='https://translate.google.com/#en/ru/{}'
user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
headers = {'User-Agent': user_agent}

print url.format(args.word)
request = urllib2.Request(url.format(args.word), headers=headers)
response = urllib2.urlopen(request)
html_page = response.read()
encoding = chardet.detect(html_page)
html_page = html_page.decode(encoding['encoding'])

with codecs.open('html_down.html', 'wb') as file1:
    file1.write(html_page)

soup = BeautifulSoup(html_page.decode('utf-8'), 'html.parser')
with codecs.open('html_downed.html', 'wb') as file1:
    file1.write(soup.prettify().encode('utf-8'))
file1.close()

for link in soup.find_all('gt-baf-cell gt-baf-word-clickable'):
    print link
