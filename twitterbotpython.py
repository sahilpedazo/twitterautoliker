import tweepy
import json
from time import sleep
from re import search
from itertools import cycle
from random import shuffle
from settings import *
from datetime import datetime, timedelta

class TwitterBot(object):
    """docstring for TwitterBot"""
    def __init__(self):
        # authorization from values inputted earlier, do not change.
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        self.api = tweepy.API(auth)
        self.followers = self.api.followers_ids(screen_name)
        self.following = self.api.friends_ids(screen_name)
        self.blacklisted_users = blacklisted

    def likebykeyword(self):
        for i in keywords:
            print("selected search text:", i)
            for twi in tweepy.Cursor(self.api.search, q=i).items(results_search):
                try:
                    # twi.retweet()
                    twi.favorite()
                    sleep(3)
                    print ("Liked")
                except tweepy.TweepError as e:
                    print(e)
                except:
                    print("Unknow Exception come!!")
                # if not twi.user.following and twi.user.screen_name!=screen_name:
                #     twi.user.follow()
                #     print('Followed user. Sleeping 15 seconds.')
                #     sleep(15)
        print("Complted")


    @staticmethod
    def error_handling(e):
        error = type(e)
        if error == tweepy.RateLimitError:
            print("You've hit a limit! Sleeping for 30 minutes.")
            sleep(60 * 30)
        elif error == tweepy.TweepError:
            print('Uh oh. Could not complete task. Sleeping 10 seconds.')
            sleep(20)
        else:
            print('Uh oh. Could not get exception type. Sleeping 10 minutes.')
            sleep(60*10)