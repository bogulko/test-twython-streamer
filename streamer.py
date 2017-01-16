# -*- coding: utf-8 -*-

from twython import TwythonStreamer

from auth_fin import (consumer_key, consumer_secret,
                      access_token, access_token_secret)


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            username = str(data['user']['screen_name'])
            tweet = str(data['text'])
            print("@%s: %s" % (username, tweet))

stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
hashtag = str(input("Search:"))
stream.statuses.filter(track=hashtag)
