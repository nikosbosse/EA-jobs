from create_api import create_api
from create_api import get_api_rate_status
import tweepy

class jobtweet:    

    def __init__(self):
        self.api = create_api()
        get_api_rate_status(self.api)
        self.my_last_tweet_id = tweet = self.api.user_timeline(id = self.api.me().id, count = 1)[0]._json['id']      
        print("got my last tweet")  
          
    def get_mentions(self):

        self.tweet_ids = []
        tweets = tweepy.Cursor(self.api.mentions_timeline, since_id = self.my_last_tweet_id).items()
        print("loaded mentions since my last tweet\n\n")        
        get_api_rate_status(self.api)

        for tweet in tweets:            
            # get ID of the tweet. If the tweet was in reply to something, get the ID of that instead
            tweet_id = tweet._json['id']
            print(tweet_id)
            in_reply_to_id = tweet._json['in_reply_to_status_id'] 
            
            # get the top level tweet by iteratively checking whether a tweet was posted in reply to another tweet
            while in_reply_to_id: 
                tweet_id = in_reply_to_id
                try: 
                    tweet = self.api.get_status(tweet_id)
                    get_api_rate_status(self.api)
                    in_reply_to_id = tweet._json['in_reply_to_status_id']
                except: 
                    continue
                
            if in_reply_to_id:
                tweet_id = in_reply_to_id
            
            self.tweet_ids.append(tweet_id)
        self.tweet_ids = set(self.tweet_ids)
        print(self.tweet_ids)


    def retweet(self):
        
        for id in self.tweet_ids: 
            print(self.tweet_ids)
            retweeted = self.api.get_status(id).retweeted
            get_api_rate_status(self.api)
            
            
            if not retweeted: 
                self.api.retweet(id)


