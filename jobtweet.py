from create_api import create_api
from create_api import get_api_rate_status
from webhook import Webhook
import tweepy

class jobtweet:    

    def __init__(self):
        self.api = create_api()
        self.webhook = Webhook()
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

    def post(self, tweet):
        status = self.api.get_status(tweet, tweet_mode="extended")
        get_api_rate_status(self.api)
        tweet_data = {"id": tweet}
        # if hasattr(status, "retweeted_status"):
        #     status = status.retweeted_status
        if hasattr(status, "full_text"):
            tweet_data["text"] = status.full_text
        elif hasattr(status, "text"):
            tweet_data["text"] = status.text
        else:
            # This line is being left for debugging.
            # This code uses outdated dependancies and older Twitter API
            # calls so the documentation isn't as good.  Will remove once
            # I'm sure it works properly, and probably make this a return.
            tweet_data["text"] = "Failed to get text to post."
        self.webhook.post(tweet_data)

    def retweet(self):
        
        for id in self.tweet_ids: 
            print(self.tweet_ids)
            retweeted = self.api.get_status(id).retweeted
            get_api_rate_status(self.api)
            
            
            if not retweeted: 
                self.api.retweet(id)
                self.post(id)
