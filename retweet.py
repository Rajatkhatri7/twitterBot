import tweepy
import time

consumer_key  = ''
consumer_sec = ''
acces_token = ''
accestoken_sec =''


auth  =  tweepy.OAuthHandler(consumer_key,consumer_sec)
auth.set_access_token(acces_token,accestoken_sec)
api = tweepy.API(auth)
user = api.me()

queries = ''
tweets_per_day = 1000

for tweet in tweepy.Cursor(api.search, q=queries).items(tweets_per_day ):
	try:
		tweet.retweet()
		print("Retwitted Successfully")
		time.sleep(1)
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

