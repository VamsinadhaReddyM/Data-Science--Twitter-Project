# -*- coding: utf-8 -*-

## NMF code taken from professors slides
#!pip install gensim
from __future__ import division, print_function

import numpy as np

import logging
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
logging.root.level = logging.INFO  # ipython sometimes messes up the logging setup; restore
import nltk
stopwords = nltk.corpus.stopwords.words('english')
#stopwords=[]
madeup_stopwords=['donald','trumps','trump','trumprussia','donaldtrumps','newttrump','ll','retweet','donaldtrump','realdonaldtrump']

with open('10K_DataCleaned.txt','r') as f1:
    TweetList = f1.read().split('\n\n')
    
   
#Removing nltk stopwords and stemmingta

words_no_stopwords=[]

NoStopTweetList=[]

print (len(TweetList))

for tweet in TweetList:
    newtweet=''
    for word in tweet.split():

        word =word.lower()
        if word not in stopwords and len(word) > 1 and word not in madeup_stopwords : # 'trump' not in word and 'donald' not in word :
            newtweet=newtweet+ ' '+ (word.encode('utf-8'))
            #newtweet=newtweet+ ' '+ (ps.stem(word.encode('utf-8')))
    NoStopTweetList.append(newtweet)

#print (NoStopTweetList)


#NMF code starts





corpus = []

for tweet in NoStopTweetList:
    corpus.append(tweet)

#print (corpus)
#print names[:30]
#CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words='english', min_df=1)
doc_term_matrix = vectorizer.fit_transform(corpus)
#print doc_term_matrix.shape
#print doc_term_matrix[0][0]
print (doc_term_matrix)
vocab = vectorizer.get_feature_names() # list of unique vocab, we will use this later
print (len(vocab))

#print (vocab[3])
#print (len(vocab)), '# of unique words'
#print (vocab[-10:])
#print (vocab[:10])

from sklearn import decomposition

print ('num of documents, num of unique words')
print (doc_term_matrix.shape)

num_topics = 10

clf = decomposition.NMF(n_components=num_topics, random_state=1)
doctopic = clf.fit_transform(doc_term_matrix)
print (doctopic)

topic_words = []
num_top_words = 5
#print vocab[100]

for topic in clf.components_:
    #print topic.shape, topic[:10]
    word_idx = np.argsort(topic)[::-1][:num_top_words]
    #print word_idx
    #for idx in word_idx:
        #print vocab[idx],
    #print
for topic in clf.components_:
    #print topic.shape, topic[:5]
    word_idx = np.argsort(topic)[::-1][0:num_top_words] # get indexes with highest weights
    #print 'top indexes', word_idx
    topic_words.append([vocab[i] for i in word_idx])
    #print topic_words[-1]
    #print
#print '__lol__' * 10        
with open('AZ_NMF.txt','a') as ff:
    for t in range(len(topic_words)):
        print ("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))
        ff.write("Topic {}: {}".format(t, ' '.join(topic_words[t][:15])))
        ff.write('\n\n')























        
        