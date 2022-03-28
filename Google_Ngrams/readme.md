# Google Ngram

As designed in the research question, the next step is using Google Ngram frequencies as features. The processes conclude frequency acquisition & feature engineering, model tests, and feature selection.

## Frequency Acquisition

​	For every record in the dataset, the lemmas of the synsets are listed by WordNet library correspondingly. They can include all the words of their concept so that the frequency of a concept is more complete to represent its feature. 

​	Then, frequencies of each lemma can be obtained by access Google Ngram viewer. There is actaully no official API for getting the frequency. Here we use a web crawl to post a request and get its response. The response can be parsed and analysed to get valid data which then is formed into a dataframe. Therefore, it is easy to calculate the mean and maximal values of lemmas as well as concepts. 

​	The maximum can directly be one of the features. The mean values still need deviding by the year period and the result can be another feature. This processing can be regarded as 'local' feature engineering.

### Optimal crawler

​	It is found that continuous requests to Google Ngram viewer would trigger an exception that **`503 Service Unavailable`** and respond no valid frequency data. The reason is that Google set a limitation to protect its server and services. It can be found out that the policy of Google server request limit is likely 75 requests every 560 seconds. 

​	Therefore, we reschedule the sleep strategy to 72 requests then wait 580 seconds every round instead of sleeping 10 seconds each requests. After a time checker as a benchmark, the new strategy can have 21% speed up on the dataset.

### Frequency as a feature

​	The newly introduced features will be several frequencies of concepts. As disscussed before, they are mean and maximal frequencies from Google Ngram corpus in the recent 1 year, 5, 10, 20, 50, 100, 200, 400, and 500 years. At the first glance, the frequency of the concept at the basic level is likely higher than that at non-basic level.

## Model Tests

​	Similar to the tests in Corpora Size for the Hypothesis 1, there are also three model test settings: GlobalModel, LocalModel, and TransferModel. The classifier is also Ramdom Forest with SMOTE algorithm. All experiment settings keep the same except for the feature selection of frequency. That is to say, the structural features remain as the base and pop each frequency feature to test.

​	Feature schema:

``` tex
- base: 
	-- # direct hypernyms
	-- # hyponyms
	-- normalized part-whole relations
	-- normalized depth from top synset
	-- normalized gloss char length
	-- the shortest lemma char length
	-- # lemmas
	-- maximal # polysemies of lemmas

- candidates:
	-- mean frequency: 1, 5, 10, 20, 50, 100, 200, 400, and 500 years
	-- maximal frequency: 1, 5, 10, 20, 50, 100, 200, 400, and 500 years

- target:
	-- all agreed vote: (bin) basic or non-basic
```

​	The results of each model test are as follow in plots. The variance is not large.

### GlobalModel Test

**Kappa**:

![global_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/GlobalMode_kappa.png?raw=true)

​	Maximal frequency mainly behaves better kappa except 1 year. It is expected to select maximal 100 year as a frequency feature. A weird phenomenon is that 5 year and 100 year have a totally different trend. Moreover, max 100y has the best score while mean 100y does the worst. 

**Balanced accuracy**:

![global_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/GlobalMode_balanced%20accuracy.png?raw=true)

​	Balanced accuracy shows a similar trend to the kappa. Also, maximal 100y is the most proper one.

### LocalModel Test

**Kappa**:

![local_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/LocalMode_kappa.png?raw=true)

​	Mean frequency would have more better scores and exceed more compared with the maximal, which is different from GlobalModel results. The peak score is contributed by mean 20y. Mean 100y has the second place.

**Balanced accuracy**:

![local_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/LocalMode_balanced%20accuracy.png?raw=true)

​	Mean 20y again show the best balanced accuracy and the second place comes to maximal 500y.

### TransferModel Test

**Kappa**:

![transfer_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/TransferMode_kappa.png?raw=true)

​	

​	Lines od mean and maximal are interweaved. Mean 20y has the best score then mean 100y and maximal 100y similar do the next. However, the average value of kappas is poor than GlobalModel's and LocalModel's. 

**Balanced Accuracy**:

![transfer_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/TransferMode_balanced%20accuracy.png?raw=true)

​	

A similar trend to the kappa's shows that mean 20y and mean 100y are the best two features.

### Conclusion

 1. Neither kappa nor balanced accuracy has direct relation with the time period. It means that the frequency features from Google Ngram can be used without considaring the corpus size (the size of Ngram in 1 year is large enough). Therefore, we want to only select the best ones to train.
 2. Frequency in mean or maximum does not matter too much in the most cases. Only GlobalModel in the experiment, maximums do better than means. The final best frequency features would come from the next step: Feature selection.
 3. Mentioned in the first research question, Hypothesis 1, and the presentation, GlobalModel and Transfermodel are more meaningful to refer when predicting in the large-scale WordNet. Therefore, I prefer to adopting maximal 100y as one of the frequency features when trainning models.
