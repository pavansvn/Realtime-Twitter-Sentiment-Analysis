import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from textblob import TextBlob
import json

consumer_key = 'corE1R1dau3fiDzRAx5yU'
consumer_secret ='eaRl7pjCuI7zRGcZH6F7w1Ppm8JpBZh3QmaJqDGCubhK' 
access_token = '989003073610768384-XYuMd8G0jU4aXfDm5KjIGXwIXnuS'
access_secret ='vC2uCvJgJA5IKDtq3tFBemUGbSBNF41LwBlbZBcwT'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
  
  def on_data(self,data):
    try:
        all_data = json.loads(data)
        tweet = all_data["text"]
        txtblb = TextBlob(tweet).sentiment
        print(tweet,txtblb.polarity,txtblb.subjectivity)
        if(txtblb.subjectivity*100 >=40):
           output = open("twitter_KA_Polls.txt",'a') 
           output.write(str(txtblb.polarity))
           output.write('\n')
           output.close()
           return True
    except BaseException as e:
      print("Error on_data:%s" % str(e))
    return True
  
  def on_error(self,status):
    print(status)
    return True

twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track=['KarnatakaElections2018','KarnatakaOpinionPoll','KarnatakaElections','KarnatakaAssemblyElection'])
