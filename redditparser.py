from HTMLParser import HTMLParser
from time import sleep
import urllib2

images = []
urls = ["http://reddit.com"]

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
    if ('.' in url.split('/')[-1]):
        acceptable = True
    elif (viableImgur(url)):
        url = parseImgur(url)
        acceptable = True

    #Save if image
    if (acceptable):
        obj = {}
        obj['sub'] = value(attrs, 'data-subreddit')
        obj['url'] = url
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
                    urls.append(href)

def loadPage():
    url = urls[-1]
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    page = res.read()
    #with open('index.html.1', 'r') as content_file:
	#       page = content_file.read()
    sleep(30)
    return page

def main():
    pageCount = 2
    parser = RedditParser()
    while (pageCount > 0):
        page = loadPage()
        parser.feed(page)
        pageCount -= 1

main()
print str(images).replace("'", '"')
