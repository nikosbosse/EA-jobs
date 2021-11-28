import tweepy
from dotenv import load_dotenv
import os
import pandas as pd

def create_api():

    tweepy.debug(True)
    load_dotenv()
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(
        auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    """ try:
        api.verify_credentials()
    except Exception as e:
        raise e """
    return api


def get_api_rate_status(api): 
    status = (api.rate_limit_status())

    limits = []
    print(status['rate_limit_context'])
    for key in status['resources'].keys():
        df = pd.DataFrame.from_records(status['resources'][key]).transpose()
        limits.append(df)

    out = pd.concat(limits)
    out = out[(out['limit'] != out['remaining'])]
    print(out)