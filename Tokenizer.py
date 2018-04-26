from collections import Counter
import re
import json

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
regex_str = [
        emoticons_str,
        r'<[^>]+>',
        r'(?:@[\w_]+)',
        r"(?:\#[\w_]+[\w\'_\-]*[\w_]+)",
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[1*\(\),]|(?:%[0-9a-f][0-9a-f]))+',
        
        r'(?:(?:\d+,?)+(?:\.?\d+)?)',
        r"(?:[a-z][a-z'\-_]+[a-z])",
        r'(?:[\w_]+)',
        r'(?:\S)'
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')',re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$',re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s,lowercase = False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english')+ punctuation + ['rt','RT','via','6']
fname = '/home/cloudera/Twitter/twitter_IPL2018'

with open(fname,'r',newline='\r\n') as f :
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list of all terms
        terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
        # Count terms only once ,equivalent to document frequency
        terms_single = set(terms_stop)
        #Count hashings only
        terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
                      #Count terms only (no mentions,no hashtags)
        terms_only = [term for term in preprocess(tweet['text'].lower()) if term not in stop ]
        # mind the ((double brackets))
        # startswith() takes a tuple(not in list) if we pass a list of inputs
        
        terms_all = [term for term in  preprocess(tweet['text'])]
        # print(terms_all)
        new_terms = []
        for term in terms_only:
            if len(term)>3:
                new_terms.append(term)
        
        # Update the counter
        count_all.update(new_terms)
        #count_all.update(terms_only)
        #Print the first 3 most frequent words
        print(count_all.most_common(50))

import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS
import pandas as pd

data = count_all.most_common(50)
df = pd.DataFrame(data)
df.columns = ('terms','frec')
print(df.head())
word_string = ' '
for index, row in df.iterrows():
    word_string +=(row['terms']+ ' ')*row['frec']    

#print(word_string)

wordcloud = WordCloud(font_path='/home/cloudera/Twitter/Aaargh.ttf',
                      stopwords=STOPWORDS,
                      background_color='white',
                      width=1200,
                      height = 1000
                      ).generate(word_string)
plt.imshow(wordcloud)
plt.axis('off')
plt.show()











    