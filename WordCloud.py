# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 01:32:39 2017

@author: chait
"""
# WordCloud code taken from professors slides
from wordcloud import WordCloud
import matplotlib.pyplot as plt
#stopwords = nltk.corpus.stopwords.words('english')
stopwords=[]


with open('AZ_DataCleaned.txt','r') as f1:
    wordlist = f1.read().split()
    
   
#Removing nltk stopwords
words_no_stopwords=[]
for word in wordlist:        
    if word not in stopwords and len(word) > 1 : # 'trump' not in word and 'donald' not in word :
        words_no_stopwords.append(word.lower().encode('utf-8'))
        

#Removing user defined stop words
final_words=[]
madeup_stopwords=['donald','will','president','america','california','texas','arizona','flordia', 'new york','trumps','trump','donaldtrumps','newttrump','ll','retweet','donaldtrump','realdonaldtrump']
for un in  words_no_stopwords:
    if un not in madeup_stopwords:
        final_words.append(un)
        
text=''        
for word in final_words:
    text += ' {}'.format(word)

        
#Display WordCloud
wordcloud = WordCloud(max_font_size=40).generate(text) 
# Display the generated image:
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

