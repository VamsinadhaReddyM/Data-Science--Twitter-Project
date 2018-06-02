# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:13:45 2017

@author: vamsinadha-M
"""
# All import and key syntax is taken from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
import tweepy
#import contextmanager
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json,time

#import pandas as pd
#import matplotlib.pyplot as plt
#import json
 
#Twitter API Keys and Tokens
#Twitter Id: cvgokhale
consumer_key = 'V1AGTCCI2ubP3eVHvIgcXDJo7'
consumer_secret = 'dkIAdJooEmEiX9a7pKVkUHROMwxzINoLUN4eaaUhMghMX2V5G8'
access_token = '835174325917519872-UiHTZEE40nytZOOme5SoOq9PUi2tG7a'
access_secret = 'cR6kQspO8OxeTODLyelgdC4ZZaf5HG1LB3jCXaxOeXMit'

 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)



# All import and key syntax is taken from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
class CollectTweets(StreamListener):
    
    def on_data(self, data):
       try:
           Tweet=json.loads(data)    
           if Tweet['lang']=='en': 
                    if Tweet['text'] is not None: #and Tweet['lang'] is 'en':
                        print Tweet['text']
                        with open('10K_Tweets.txt','a') as fj:
                            fj.write(Tweet['text'].encode('utf-8')+'\n\n')                                
       except:
            return True
            
    def on_error(self, status):
        self.time.sleep(10)
        return True
        #print status

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    #l = CollectTweets()
   # listener=MyStreamListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    l=CollectTweets()      
    stream = Stream(auth,l)    
    #This line filter Twitter Streams to capture data by the keywords:     
    stream.filter(track=['Trump'])#,stall_warnings=True)
    
    
    #help(stream.filter)
    # All import and key syntax is taken from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
