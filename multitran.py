import urllib2
import argparse
import codecs
import json
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Process word to translate')
parser.add_argument('word', type=str, help='word to be translated')
args = parser.parse_args()

url='http://www.multitran.ru/c/m.exe?CL=1&s={}&l1=4'
user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
headers = {'User-Agent': user_agent}

print url.format(args.word)
request = urllib2.Request(url.format(args.word), headers=headers)
response = urllib2.urlopen(request)
translate = response.read().decode('cp1251')
soup = BeautifulSoup(translate, 'html.parser')
with codecs.open('elle.html', 'wb') as html:
    html.write(soup.prettify().encode('utf-8'))    

html.close()
