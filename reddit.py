import json
import praw
import requests
import pandas as pd

credentials = 'reddit_secrets.json'
 
with open(credentials) as f:
    creds = json.load(f)

reddit = praw.Reddit(client_id=creds['client_id'],
                     client_secret=creds['client_secret'],
                     user_agent=creds['user_agent'],
                     redirect_uri=creds['redirect_uri'],
                     refresh_token=creds['refresh_token'])

subr = 'EffectiveAltruism' # Choose your subreddit

subreddit = reddit.subreddit(subr)

limit = 100
timeframe = 'week' #hour, day, week, month, year, all
listing = 'top' # controversial, best, hot, new, random, rising, top
 

# function to download reddit posts from a given subreddit
def get_reddit(subreddit,listing,limit,timeframe):
    try:
        base_url = f'https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}'
        print(base_url)
        request = requests.get(base_url, headers = {'User-agent': 'effective_jobs'})
    except:
        print('An Error Occured')
    return request.json()
 
r = get_reddit(subreddit,listing,limit,timeframe)

# function to get Title, URL, Score, Number of comments
def get_results(r):
    '''
    Create a DataFrame Showing Title, URL, Score and Number of Comments.
    '''
    myDict = {}
    for post in r['data']['children']:
        myDict[post['data']['title']] = {'url':post['data']['url'],'score':post['data']['score'],'comments':post['data']['num_comments']}
    df = pd.DataFrame.from_dict(myDict, orient='index')
    return df
 
df = get_results(r)

print(df)
