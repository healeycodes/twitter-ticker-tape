import tweepy
from emoji import demojize
from time import sleep
from collections import OrderedDict

import config
import posprint

auth = tweepy.OAuthHandler(
    config.consumer_key,
    config.consumer_secret
)
auth.set_access_token(
    config.access_token,
    config.access_token_secret
)

api = tweepy.API(auth)

# we use an ordered dictionary so we can remove old tweets
# from the data structure. Our program may be long-running
# and we don't want to run out of memory
seen_statuses = OrderedDict()

while True:
    public_tweets = api.home_timeline(tweet_mode='extended')
    for status in public_tweets:

        # we're interested in statuses we haven't seen before
        if status.id not in seen_statuses:

            # store the statuses we use
            seen_statuses[status.id] = status

            # dump old statuses that can't appear again
            if len(seen_statuses) > 20:
                seen_statuses.popitem()

            user = status.user.screen_name + ':\n'

            # get the full tweet text regardless of type
            # https://github.com/tweepy/tweepy/issues/935
            if hasattr(status, 'retweeted_status'):
                tweet = user + status.retweeted_status.full_text
            else:
                tweet = user + status.full_text

            # trim unprintable characters that POS58 can't output
            # by turning emojis into textual representation.
            # 😅 becomes :grinning_face_with_sweat:
            tweet = demojize(tweet).encode(
                encoding='ascii',
                # throwaway non ascii characters
                errors='ignore'
            ).decode()

            posprint.output(tweet)

    # twitter restricts statuses/home_timeline to once per minute
    sleep(65)
