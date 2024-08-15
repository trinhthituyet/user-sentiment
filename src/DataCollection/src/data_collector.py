import tweepy
import os


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
    trends = api.get_place_trends(location_id)

    for trend in trends[0]["trends"]:
        print(trend)



