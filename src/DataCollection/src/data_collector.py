import tweepy
import os
from datetime import datetime


def get_api():
    api_key = os.environ['API_KEY']
    api_secret_key = os.environ['API_SECRET_KEY']
    access_token = os.environ['ACCESS_TOKEN']
    access_token_secret = os.environ['ACCESS_TOKEN_SECRET']
    
    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def collect_data(api):
    location_id = 1
    trends_res = api.get_place_trends(location_id)

    trends = []
    for trend in trends_res[0]["trends"]:
        trends.append({
        "name": trend["name"],
        "tweet_volume": trend["tweet_volume"],
        "timestamp": datetime.now()
    })



