#!/usr/bin/env python
# -*- coding: utf-8 -*-

from HTMLParser import HTMLParser
from time import sleep
import urllib2
import os

images = []

if (os.path.exists('latesturl')):
    f = open('latesturl', 'r')
    url = f.readline()
    urls = [url]
    f.close()
else:
    urls = ["http://reddit.com/?limit=100"]

def viableImgur(url):
    if ("imgur.com" in url and "/a/" not in url):
        return True
    return False

def parseImgur(url):
    if ('.' not in url.split('/')[-1]):
        url = url + ".jpg"
        return url
    return url

def parseContent(attrs):
    url = ""
    acceptable = False
    #Define url
    if (contains(attrs, 'data-url')):
        url = value(attrs, 'data-url')
    else:
        url = value(attrs, 'data-href-url')

    #Define if image
    pageName = url.split('/')[-1]
    pageType = pageName.split('.')[-1]
    acceptedTypes = ['jpg', 'jpeg', 'png', 'gifv', 'mp4', 'webm']
    if (pageType in acceptedTypes):
        acceptable = True
    elif (viableImgur(url)):
        url = parseImgur(url)
        acceptable = True

    #Save if image
    if (acceptable):
        obj = {}
        obj['sub'] = str(value(attrs, 'data-subreddit'))
        obj['url'] = str(url)
        images.append(obj)

def contains(pairList, attr):
    if (value(pairList, attr) != None):
        return True
    return False

def value(pairList, attr):
    for pair in pairList:
        if (pair[0] == attr):
            return pair[1]
    return None

class RedditParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == "div"):
            if(contains(attrs, 'class')):
                htmlClass = value(attrs, 'class')
                if ("thing" in htmlClass and contains(attrs, 'data-subreddit')):
                    if (contains(attrs, 'data-url') or contains(attrs, 'data-href-url')):
                        parseContent(attrs)
        elif (tag == "a"):
            if (contains(attrs, "href")):
                href = value(attrs, "href")
                if ("count" in href and "after" in href):
                    f = open('latesturl', 'w')
                    f.write(href)
                    f.close()

def loadPage():
    url = urls[-1]
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    page = res.read().decode('utf-8')
    #with open('index.html.1', 'r') as content_file:
	#       page = content_file.read()
    return page

def main():
    pageCount = 1
    parser = RedditParser()
    while (pageCount > 0):
        page = loadPage()
        parser.feed(page)
        pageCount -= 1

main()
print str(images).replace("'", '"')
