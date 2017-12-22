from twython import Twython

# using Twython for querying twitter via Search API 

TWITTER_APP_KEY = '' 
TWITTER_APP_KEY_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET = ''

# Obtain an OAuth2 Access Token
twitter = Twython(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

# Use the Access Token
twitter = Twython(TWITTER_APP_KEY, access_token=ACCESS_TOKEN)

# Search
searches = twitter.search(q = '$CERN', count = 102)

print searches
tweets = searches['statuses']
i = 0
for tweet in tweets:
	print tweet['text'], '\n'
	i+=1
	print i


#tweet['id_str'], '\n', tweet['text'], '\n\n\n'
