import tweepy
import json

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        tweet = json.loads(data)

        try:
            api.retweet(tweet['id'])
            print(tweet['id_str'] + ' rewteeted!')
        except:
            print('failed to retweet ' + tweet['id_str'])
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #print("Showing all new persian tweets for github:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    l = StdOutListener()
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['github com', 'gitlab com'], languages=['fa'])
