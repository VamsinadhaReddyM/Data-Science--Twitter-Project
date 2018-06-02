# -*- coding: utf-8 -*-
# LDA code taken from professors slides
import nltk
import logging
import gensim
from gensim import corpora
logging.basicConfig(format='%(levelname)s : %(message)s', level=logging.INFO)
stopwords = nltk.corpus.stopwords.words('english')
#stopwords=[]
madeup_stopwords=['donald','trumps','trumprussia','trump','donaldtrumps','newttrump','ll','retweet','donaldtrump','realdonaldtrump']

with open('NY_DataCleaned.txt','r') as f1:
    TweetList = f1.read().split('\n\n')
       
#Removing nltk stopwords and stemming
words_no_stopwords=[]

NoStopTweetList=[]
for tweet in TweetList:
    newtweet=[]
    for word in tweet.split():
        word =word.lower()
        if word not in stopwords and len(word) > 1 and word not in madeup_stopwords : # 'trump' not in word and 'donald' not in word :
            newtweet.append(word.encode('utf-8'))
    NoStopTweetList.append(newtweet)
#print NoStopTweetList[0:5]
#from nltk.stem.wordnet import WordNetLemmatizer

# Creating the term dictionary of our courpus, where every unique term is assigned an index.
#reduced11 is the cleaned list of list of tweet words
dictionary = corpora.Dictionary(NoStopTweetList)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above.
doc_term_matrix = [dictionary.doc2bow(doc) for doc in NoStopTweetList]
# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Trainign LDA model on the document term matrix.
ldamodel = Lda(doc_term_matrix, num_topics=20, id2word = dictionary, passes=100)

#print(ldamodel.print_topics(num_topics=15, num_words=15))
with open('10K_LDA.txt','a') as ff:
    #print("LDA model")
    topics_found = ldamodel.print_topics(15)
    counter = 1
    for t in topics_found:
        print("Topic #{} {}".format(counter, t))
        ff.write("Topic #{} {}".format(counter, t))
        ff.write('\n\n')
        counter += 1


