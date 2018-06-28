# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 00:04:34 2017

@author: vamsinadha-M
"""

import string
#from textblob import Word

f2=open('AZ_DataCleaned.txt','w') 

#splitting the tweets by \n\n character spacing
with open('AZ.txt','r') as f1:
    linelist = f1.read().split('\n\n')
    modifyLL=[]
try:   
    for line in linelist:
        if line=='':    
            continue
        modifyLL.append(line)
except:
    print
   # print modifyLL

count=1
#going through each tweet
for line in modifyLL:
    try:
        if count==10000:
            break
        
        WordList= line.split()
        nl=''
        for word in WordList:
            if word.startswith('RT') or word.startswith('@') or word.startswith('http') :
                continue
            
            a=string.punctuation
            try:
                word= word.encode('utf-8')
            except:
                continue
            word = word.replace("'","")
            #nw=''
            #http://stackoverflow.com/questions/12437667/how-to-replace-punctuation-in-a-string-python
            replace_punctuation = string.maketrans(a, ' '*len(a))
            word = word.translate(replace_punctuation)
            word = word.translate(string.maketrans(string.digits,' '*len(string.digits)))
            # this function is spell check function and replace by correct spelling word
            #word = Word(word)
            #word.spellcheck()
            #word =word.translate(q,string.punctuation)
            #print word
            nl=nl+word+' '
            
            
        print nl
        count +=1    
        f2.writelines(nl+'\n\n')
        
            
    except:
        continue
f2.close()
                   

        
        
