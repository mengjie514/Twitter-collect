# ENGVIRE 6Nations Rugby 2018 Final 
# Time slots
# pre 9.45pm (NZT 3.17 Sat) - 3.45am (GMT 8.45am - 2.45pm 3.17 Sat)
# mid 3.45am (NZT 3.18 Sun) - 6.15am (GMT 2.45pm - 5.15pm 3.17 Sat)
# pos 6.15am (NZT 3.18 Sun) - 12.15pm (GMT 5.15pm - 12.15pm 3.17 Sat)

import tweepy
import sched, time
from tweepy import OAuthHandler

s = sched.scheduler(time.time, time.sleep)

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener
import time

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            print(data)
            saveFile = open('atirish.json','a')
            saveFile.write(data)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            time.sleep(5)
        

    def on_error(self,status):
        print(status)

def StreamProcess():
    print("SP")
    twitter_Stream = Stream(auth, MyListener())
    twitter_Stream.filter(track=["@irishrugby"])

def StreamStarter():
    print("SS")
    s.enter(1,1,StreamProcess,())
    #s.enter(170,10,print(time.time()))
    s.run()

StreamStarter()


