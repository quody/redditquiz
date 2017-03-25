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
        if (tag == "div"):
	    print "Tag was div"
            if( hasattr(attrs, 'class')):
		print "Div has class"
                if ("thing" in attrs['class'] and hasattr(attrs, 'data-subreddit')):
		    print "Class has thing and subreddit"
                    if (hasattr(attrs, 'data-url') or hasattr(attrs, 'data-href-url')):
			print "CLASS ALSO HAS data"
                        parseContent(attrs)

def main():
    #url = "http://reddit.com"
    #req = urllib2.Request(url)
    #res = urllib2.urlopen(req)
    #page = res.read()
    with open('index.html.1', 'r') as content_file:
	page = content_file.read()
    print "Parsing", page
    parser = RedditParser()
    parser.feed(page)

main()
print images
