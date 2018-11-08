import tweepy
import pandas as pd
import datetime

consumer_key = "<put_consumer_key_here>"
consumer_secret = "<put_consumer_secret_here"
access_token = "<put_access_token_here>"
access_token_secret = "<put_access_token_secret_here>"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The search term you want to find
query = "diskon"
# Language code (follows ISO 639-1 standards)
lang = "id"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=lang, tweet_mode='extended', rpp=100)

#create list of tweets
user = []
tweet_textlist = []

#save tweet from results to list of tweets
for tweet in results:
    if hasattr(tweet, 'retweeted_status'):
        user_name = tweet.retweeted_status.user.screen_name
        try:
            tweet_text = tweet.retweeted_status.full_text
        except:
            tweet_text = tweet.retweeted_status.text
    else:
        user_name = tweet.user.screen_name
        try:
            tweet_text = tweet.full_text
        except AttributeError:
            tweet_text = tweet.text
    tweet_text = tweet_text.replace('\n', ' ')
    user.append(user_name)
    tweet_textlist.append(tweet_text.encode("utf8"))
    
tweet_data = {'user': user,
             'tweet': tweet_textlist}

df = pd.DataFrame(data=tweet_data)

time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
df.to_csv(time+".csv")
