# Google Ngram

As designed in the research question, the next step is using Google Ngram frequencies as features. The processes conclude frequency acquisition, model tests, and feature engineering(selection).

## Frequency Acquisition

​	For every record in the dataset, the lemmas of the synsets are listed by WordNet library correspondingly. They can include all the words of their concept so that the frequency of a concept is more complete to represent its feature. 

​	Then, frequencies of each lemma can be obtained by access Google Ngram viewer. There is actaully no official API for getting the frequency. Here we use a web crawl to post a request and get its response. The response can be parsed and analysed to get valid data which then is formed into a dataframe. Therefore, it is easy to calculate the mean and maximal values of lemmas as well as concepts. 

​	The maximum can directly be one of the features. The mean values still need deviding by the year period and the result can be another feature. This processing can be regarded as 'local' feature engineering.

### Optimal crawler

​	It is found that continuous requests to Google Ngram viewer would trigger an exception that **`503 Service Unavailable`** and respond no valid frequency data. The reason is that Google set a limitation to protect its server and services. It can be found out that the policy of Google server request limit is likely 75 requests every 560 seconds. Therefore, we reschedule the sleep strategy to 72 requests then wait 580 seconds every round instead of sleeping 10 seconds each requests. After a time checker as a benchmark, the new strategy can have 21% speed up on the dataset.
