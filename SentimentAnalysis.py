# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 02:04:43 2017

@author: vamsinadha-M
"""

#import textblob
from textblob import TextBlob


sub_list = []
pol_list = []
with open('AZ_DataCleaned.txt') as f1:
    linelist = f1.read().split('\n\n')
#print linelist
modifyLL=[]

#Removing /n
for line in linelist:
    if line=='':
        continue
    line.replace('\n',' ')
    modifyLL.append(line)
        
#print linelist
#print len(modifyLL)
for s in modifyLL:
    if s =='':
        continue
    
    tb = TextBlob(s)
    sub_list.append(tb.sentiment.subjectivity)
    pol_list.append(tb.sentiment.polarity)
#print sub_list
#print pol_list

#Graph part
# we are removing tweets with 0.0 subjectivity
score_sub_count=[]
for sub in sub_list:
    if sub==0:
        continue
    else:
        score_sub_count.append(sub)
        
 
#subjectivity graph    

import matplotlib.pyplot as plt

plt.hist(score_sub_count, bins=50)#, normed=1, alpha=0.75)
plt.xlabel('subjectivity score')
plt.ylabel('Tweet count')
plt.grid(True)
#plt.savefig('subjectivity.pdf')
plt.show()

# Polarity Graph
plt.hist(pol_list, bins=50)#, normed=1, alpha=0.75)
plt.xlabel('Polarity score')
plt.ylabel('Tweet count')
plt.grid(True)
#plt.savefig('subjectivity.pdf')
plt.show()

#print len(sub_list)
#print len(pol_list)

#Average of Polarity and Subjectivity
AvgSubPol=[]
for i in range(0,len(sub_list)):
    avg=(sub_list[i]+pol_list[i])/2
    AvgSubPol.append(avg)
    

plt.hist(AvgSubPol, bins=50)#, normed=1, alpha=0.75)
plt.xlabel('Average of Polarity and Subjectivity score')
plt.ylabel('Tweet count')
plt.grid(True)
#plt.savefig('subjectivity.pdf')
plt.show()




