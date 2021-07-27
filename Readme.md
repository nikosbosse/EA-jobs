# A Twitter Bot that retweets job offers relevant to the EA community

This bot regularly checks whether it has been mentioned by someone in a tweet. 
- If the tweet that mentions [@effective_jobs](https://twitter.com/effective_jobs) is a stand-alone tweet, it will retweet that tweet
- If the tweet that mentions [@effective_jobs](https://twitter.com/effective_jobs) is a reply to some other tweet, it will retweet that other tweet to which the person mentioning [@effective_jobs](https://twitter.com/effective_jobs) has replied to (A posts tweet, B replies with "@effective_jobs", and the bot retweets the original tweet A made). 

This way you can tag job offers that are relevant to the EA community and make them more visible. 

## Feedback and feature requests
For feature requests and feedback, please open an issue on github (go to 'issues' and click 'new issue') or send me a direct message on Twitter @nikosbosse

## Contributions
All contributions welcome! Please open a PR or an issue or get in touch with me directly

## Acknowledgements
Thank you very much to [D0TheMath](https://twitter.com/D0TheMath) [nathanpmyoung](https://twitter.com/nathanpmYoung), [julianhazell](https://twitter.com/julianhazell) and [genuine_doubt](https://twitter.com/genuine_doubt)

## Running / testing the bot on your own

- clone this repository by running `git clone https://github.com/nikosbosse/ea-jobs`
- create a virtual python environment `python -m venv env` and activate it `source env/bin/activate`
- install dependencies `pip install -r requirements.txt`
- setup a new Twitter account and developer account. Instructions from a similar project [here](https://followtheargument.org/how-to-create-a-twitter-bot-that-posts-a-random-daily-article). Store your credentials in a file called .env
- make a tweet by running `python main.py`

The bot is deployed to google servers. Some instructions on how to do that [here](https://github.com/nikosbosse/DailyElectroSet)
