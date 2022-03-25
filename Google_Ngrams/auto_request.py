import time
import csv
import nltk
import re
import requests
import pandas as pd
import numpy as np
from ast import literal_eval

import warnings
warnings.filterwarnings("ignore")

import nltk
nltk.data.path.append('../')
from nltk.corpus import wordnet as wn

# function to get the frequency of a synset in google ngrams
# set 72 requests and wait 580 seconds every time
corpora = dict(eng_2019=26, eng_us_2012=17, eng_us_2009=5, eng_gb_2012=18, eng_gb_2009=6,
               chi_sim_2012=23, chi_sim_2009=11, eng_2012=15, eng_2009=0,
               eng_fiction_2012=16, eng_fiction_2009=4, eng_1m_2009=1,
               fre_2012=19, fre_2009=7, ger_2012=20, ger_2009=8, heb_2012=24,
               heb_2009=9, spa_2012=21, spa_2009=10, rus_2012=25, rus_2009=12,
               ita_2012=22)
def ngram_by_year_sleep(synset, corpus, startYear, endYear, smoothing, caseInsensitive):
    global counter
    m = 0
    m_max = 0
    synset = wn.synset(synset[8:-2])
    for i in synset.lemmas():
        query = i.name()
        query = query.replace('_',' ') # recovery phrase from _
        params = dict(content=query, year_start=startYear, year_end=endYear,
                      corpus=corpora[corpus], smoothing=smoothing,
                      case_insensitive=caseInsensitive)
        if params['case_insensitive'] is False:
            params.pop('case_insensitive')
        if '?' in params['content']:
            params['content'] = params['content'].replace('?', '*')
        if '@' in params['content']:
            params['content'] = params['content'].replace('@', '=>')
        ## set a counter
        counter += 1
        if counter == 73:
            time.sleep(580)
            counter = 0
        req = requests.get('https://books.google.com/ngrams/graph', params=params)
        res = re.findall('ngrams.data = (.*?);\\n', req.text)
        if res:
            data = {qry['ngram']: qry['timeseries'] for qry in literal_eval(res[0])}
            df = pd.DataFrame(data)
            df.insert(0, 'year', list(range(startYear, endYear + 1)))
        else:
            df = pd.DataFrame()
        if df.shape[1] > 1: # if the query exists in google ngrams.
            ngramsum = df.iloc[:,1].sum(axis = 0, skipna = True) # sum of percentage of the lemmas each year
            m += ngramsum
            ngrammax = df.iloc[:,1].max(axis = 0, skipna = True) # max
            if ngrammax > m_max:
                m_max = ngrammax
        else:
            m += 0 # irrelevant, obviously.
            m_max += 0

    m_mean = m/(endYear-startYear+1)
    return m_mean, m_max

def produce_ngram(dataset, feature_name, startYear, endYear):
    global counter
    time.sleep(580)
    start = time.time()
    feature_mean = feature_name + '_mean'
    feature_max = feature_name + '_max'
    dataset[feature_mean], dataset[feature_max] = zip(*dataset['Synsets'].apply(lambda syn: ngram_by_year_sleep(syn, 'eng_2019', startYear, endYear, 0, True)))
    dataset.to_csv('./features_google_ngram.csv', index=False)
    end = time.time()
    period = end - start
    string = 'Done: ' + feature_name + ' ' + str(period) + ' sec.\n'
    with open('time_checker.txt', 'a+') as f:
        f.write(string)

if __name__ == '__main__':
    ngram_GS_adopt = pd.read_csv('./features_google_ngram.csv', index_col=None)

    print('start\n')

    # 1y: 2018 - 2019
    print('1y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_1y', 2018, 2019)

    # 5y: 2014 - 2019
    print('5y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_5y', 2014, 2019)

    # 10y: 2009 - 2019
    print('10y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_10y', 2009, 2019)

    # 20y: 1999 - 2019
    print('20y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_20y', 1999, 2019)

    # 50y: 1969 - 2019
    print('50y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_50y', 1969, 2019)

    # 100y: 1919 - 2019
    print('100y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_100y', 1919, 2019)

    # 200y: 1819 - 2019
    print('200y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_200y', 1819, 2019)

    # 400y: 1619 - 2019
    print('400y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_400y', 1619, 2019)

    # 500y: 1500 - 2019
    print('500y requesting...\n')
    counter = 0
    produce_ngram(ngram_GS_adopt, 'ngram_500y', 1500, 2019)
