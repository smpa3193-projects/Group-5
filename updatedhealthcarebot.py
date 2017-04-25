from twython import Twython
import csv
from textblob import TextBlob

CONSUMER_KEY = 'iA6b3VzBUdDbZcogcDxb4BBYH'
CONSUMER_SECRET = '4l68SWPeSnflSTBeim7zfw1efmED4PShJNWUJsVueYwWDTF7aE'
ACCESS_TOKEN = '851135412525559808-sGjvoX67pBymubMNcxS33Sp2OpQKCWu'
ACCESS_TOKEN_SECRET = 'O58emGQpJ1dsDmvT9JBRT7kZtOYzfFjj6yCcBXN8nNF5y'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

targetstring = ['health', 'obamacare', 'ACA', 'AHCA', 'medicare', 'medicaid']
all_health_tweets = []


fox_tweets = twitter.get_user_timeline(screen_name='foxnews', include_rts=False)

for tweet in fox_tweets:
    if any (str in targetstring for str in all_health_tweets): 
    	all_health_tweets.append(tweet)
	    
msnbc_tweets = twitter.get_user_timeline(screen_name='MSNBC', include_rts=False)

for tweet in msnbc_tweets:
    if any (str in targetstring for str in all_health_tweets): 
    	all_health_tweets.append(tweet)

health_tweets = []

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(['screenname', 'Tweet_Text', 'URL', 'time_stamp', 'polarity'])

    for result in all_health_tweets:
        tweet_text = TextBlob(tweet['text'])
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        health_tweets.append([result['user']['screen_name'], result['text'].encode('utf-8'), url, result['created_at'], tweet_text.sentiment.polarity])
        a.writerows(health_tweets)