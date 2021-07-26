from create_api import create_api
import tweepy

class jobtweet:    

    def __init__(self):
        self.api = create_api()
          
    def get_mentions(self):

        self.tweet_ids = []
        for tweet in tweepy.Cursor(self.api.mentions_timeline).items():
            
            # get ID of the tweet. If the tweet was in reply to something, get the ID of that instead
            tweet_id = tweet._json['id']
            in_reply_to_id = tweet._json['in_reply_to_status_id']

            if in_reply_to_id:
                tweet_id = in_reply_to_id
            
            self.tweet_ids.append(tweet_id)


    def retweet(self):
        for id in self.tweet_ids: 
            retweeted = self.api.get_status(id).retweeted
            
            if not retweeted: 
                self.api.retweet(id)
