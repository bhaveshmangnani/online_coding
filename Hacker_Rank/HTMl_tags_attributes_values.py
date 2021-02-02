#URL: https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print('-> {} > {}'.format(*attr)) 
parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())
parser.close()
