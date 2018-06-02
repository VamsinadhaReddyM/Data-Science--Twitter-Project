# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:13:45 2017

@author: chait
"""
# All import and key syntax is taken from http://adilmoujahid.com/posts/2014/07/twitter-analytics/
import tweepy
#import contextmanager
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
import json

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
    def __init__(self):
        #super(StdOutListener, self).__init__()
        self.c1 = 0
        self.c2 = 0
        self.c3 = 0
        self.c4 = 0
        self.c5 = 0
        
        
    def on_data(self, data):
        
            
                #if (time.time() - self.start_time) < self.limit:
                #if 'lang' in data and data['lang'] == 'en':
            Tweet=json.loads(data)
                    #print type(Tweet)
                    #http://stackoverflow.com/questions/33498975/unable-to-stop-streaming-in-tweepy-after-one-minute                
            
            try:  
                    Tweet_user=Tweet["user"]
                    if Tweet_user['location'] is not None:
                        loc= Tweet_user['location'].encode().split()
                        for locn in loc:
                            if locn in ['TX','Texas']:      
                                
                                    print Tweet_user['location']
                                    with open('Texas.txt','a') as fj:
                                        fj.write(Tweet['text']+'\n\n')                                
                                        break                            
                            if locn in ['CA','California']:
                              
                                     with open('CA.txt','a') as fl:
                                        fl.write(Tweet['text']+'\n\n')
                                     print Tweet_user['location']
                                     break
                            if locn in ['AZ','Arizona']:
                            
                                     with open('AZ.txt','a') as fll:
                                        fll.write(Tweet['text']+'\n\n')
                                     print Tweet_user['location']
                                     break
                            if locn in ['NY','New York']:
                                 
                                     with open('NY.txt','a') as ny:
                                        ny.write(Tweet['text']+'\n\n')
                                     print Tweet_user['location']
                                     break
                            if locn in ['FL','Florida']:
                                 
                                     with open('FL.txt','a') as nj:
                                        nj.write(Tweet['text']+'\n\n')
                                     print Tweet_user['location']
                                     break  
                    
            except:
                return True
       
    def on_error(self, status):
        #self.time.sleep(10)
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
    stream.filter(track=['Trump'], async=True,stall_warnings=True)
    
    
    #help(stream.filter)
    # All import and key syntax is taken from http://adilmoujahid.com/posts/2014/07/twitter-analytics/