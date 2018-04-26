import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = 'cK8E1R1dau3QYfiDzRAx5yU'
consumer_secret ='l7pjCHkX75GuI7zRGcZH6F7w1m8JpBZh3QmaJqDGCubhK' 
access_token = '989003073610768384-XYG0jU4aJ8WXfDm5KjIGXwIXnuS'
access_secret ='vC2uCvYJgJA5IKDtq3EiemUGbSBNF41LwBlbZBcwT'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
  
  def on_data(self,data):
    try:
      with open("twitter_IPL2018",'a') as f:
        f.write(data)
        return True
    except BaseException as e:
      print("Error on_data:%s" % str(e))
    return True
  
  def on_error(self,status):
    print(status)
    return True

twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track=['IPL11','VIVOIPL','IPL2018','IPL 2018'])
