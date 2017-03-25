from HTMLParser import HTMLParser
import urllib2

images = []

def parseImgur(url):
    if (url.contains("imgur.com") and not url.contains("/a/")):
        return True
    return False

def parseConent(attrs):
    url = ""
    acceptable = False
    #Define url
    if (hasattr(attrs, 'data-url')):
        url = attrs['data-url']
    else:
        url = attrs['data-href-url']

    #Define if image
    if (url.contains('.')):
        acceptable = True
    elif (parseImgur(url)):
        acceptable = True

    #Save if image
    if (acceptable):
        obj = {}
        obj['sub'] = attrs['data-subreddit']
        obj['url'] = url


class RedditParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if (tag == div):
            if( hasattr(attrs, 'class')):
                if (attrs['class'].contains('thing ') and hasattr(attrs, 'data-subreddit')):
                    if (hasattr(attrs, 'data-url') or hasattr(attrs, 'data-href-url')):
                        parseContent(attrs)

def main():
    url = "http://reddit.com"
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    page = res.read()
    print "Parsing", page
    parser = RedditLParser()
    parser.feed(page)

main()
print images
