# redditquiz

Redditquiz is a game where you have to connect memes and images to the correct subreddit.

## deployment
Image urls and subreddits have to be preparsed. This can be done with the redditparser python crawler. Since the crawler doesn't use any API it saves its progress into the latesturl file to help with reddits tight restrictions on http requests.

> python redditparser.py > src_large/data/images.json

The website can be minimized into a single html file by running the minimization script

> chmod +x minimize.sh
> ./minimize.sh

This will minimize all code with gulp as well as embed it into a single index.html in the root directory.

## tech
jQuery, html5, css3
