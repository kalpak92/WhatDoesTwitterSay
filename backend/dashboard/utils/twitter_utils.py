import twitter
from textblob import TextBlob
def get_tweets(query):
    """
    returns twitter feed with settings as described below, contains all related twitter settings
    """
    api = twitter.Api(consumer_key='9LZ9RbPMl3aTkLTNcdwsRCDpi',
                      consumer_secret='FiV3fPzcQFauANYMwERskhFiBsCnXDkRs8iR7ZVuxbdfpFXmkP',
                      access_token_key='3065919224-Jf4V1BtWWwyhv40tr7qqhvLIYGNq8h0jmN4xWw0',
                      access_token_secret='Ts68OoMWadDb0WCYFLWPSgewbeQxCaj85Lbd3twkJBGX0')

    res = api.GetSearch(raw_query="q={0}&result_type=recent&since=2014-07-19&count=100".format(query))
    
    return [{"user": s.user.screen_name,
            "text": s.text,
            "created_at": s.created_at,
            "polarity": TextBlob(s.text).sentiment.polarity
            } for s in res]