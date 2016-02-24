from twython import Twython

# using Twython for querying twitter via Search API 

TWITTER_APP_KEY = 'GH09zTCmgzTY5EB4U4wHP6jdG' 
TWITTER_APP_KEY_SECRET = 'JdMUeCxsQdwOaQPdiieLWEddVybGlHMLZ5Sk04AAPdcI2ZmXyl'
TWITTER_ACCESS_TOKEN = '3040614638-b5YAY9dXnHUnOC6zcwqh5AypggTrzj6vJMpiau7'
TWITTER_ACCESS_TOKEN_SECRET = 'KDlimmrvr6tWWk5uyF0X1aIijuLnMY16HCpHIE3I6y3Gb'

# Obtain an OAuth2 Access Token
twitter = Twython(TWITTER_APP_KEY, TWITTER_APP_KEY_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

# Use the Access Token
twitter = Twython(TWITTER_APP_KEY, access_token=ACCESS_TOKEN)

# Search
searches = twitter.search(q = '$CERN', count = 100)

print searches
tweets = searches['statuses']
i = 0
for tweet in tweets:
	print tweet['text'], '\n'
	i+=1
	print i


#tweet['id_str'], '\n', tweet['text'], '\n\n\n'
