from create_api import create_api
from jobtweet import jobtweet

def post_tweet(event="", context=""):
    tweet = jobtweet()
    tweet.get_mentions()
    tweet.retweet()

post_tweet()