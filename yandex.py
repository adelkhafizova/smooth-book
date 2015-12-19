import urllib2
import argparse
import codecs
import json

parser = argparse.ArgumentParser(description='Process word to translate')
parser.add_argument('word', type=str, help='word to be translated')
args = parser.parse_args()

url='https://dictionary.yandex.net/dicservice.json/lookup?ui=ru&srv=tr-text&sid=7b6a5af6.56954acc.7b769f34&text={}&lang=en-ru&flags=23'
user_agent='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
headers = {'User-Agent': user_agent}

print url.format(args.word)
request = urllib2.Request(url.format(args.word), headers=headers)
response = urllib2.urlopen(request)
translation_full_info = json.loads(response.read())

tr_dict = {}
translation = translation_full_info['def']
for variant in translation:
    meaning = variant['tr']
    pos = variant['pos']
    tr_dict[pos] = list()
    for m in meaning:
        tr_dict[pos].append(m['text'])
        if m.get('syn') is not None:
            for syn in m['syn']:
                tr_dict[pos].append(syn['text'])


for key, value in tr_dict.iteritems():
    print key.encode('utf-8')
    for word in value:
        print word.encode('utf-8')
json.dump(tr_dict, open("translation.txt",'w'))
