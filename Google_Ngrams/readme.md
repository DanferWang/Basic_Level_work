# Google Ngram

As designed in the research question, the next step is using Google Ngram frequencies as features. The processes conclude frequency acquisition & feature engineering, model tests, and feature selection.

## Frequency Acquisition

ngram_frequency.ipynb

grid_search_GlobalModel.py

Grid_search_TransferModel.py

​    For every record in the dataset, the lemmas of the synsets are listed by WordNet library correspondingly. They can include all the words of their concept so that the frequency of a concept is more complete to represent its feature. 

​    Then, frequencies of each lemma can be obtained by access Google Ngram viewer. There is actaully no official API for getting the frequency. Here we use a web crawl to post a request and get its response. The response can be parsed and analysed to get valid data which then is formed into a dataframe. Therefore, it is easy to calculate the mean and maximal values of lemmas as well as concepts. 

​    The maximum can directly be one of the features. The mean values still need deviding by the year period and the result can be another feature. This processing can be regarded as 'local' feature engineering.

### Optimal crawler

auto_request.py

​    It is found that continuous requests to Google Ngram viewer would trigger an exception that **`503 Service Unavailable`** and respond no valid frequency data. The reason is that Google set a limitation to protect its server and services. It can be found out that the policy of Google server request limit is likely 75 requests every 560 seconds. 

​    Therefore, we reschedule the sleep strategy to 72 requests then wait 580 seconds every round instead of sleeping 10 seconds each requests. After a time checker as a benchmark, the new strategy can have 21% speed up on the dataset.

### Frequency as a feature

​    The newly introduced features will be several frequencies of concepts. As disscussed before, they are mean and maximal frequencies from Google Ngram corpus in the recent 1 year, 5, 10, 20, 50, 100, 200, 400, and 500 years. At the first glance, the frequency of the concept at the basic level is likely higher than that at non-basic level.

## Model Tests

year_period_test.ipynb

result_plot.ipynb

​    Similar to the tests in Corpora Size for the Hypothesis 1, there are also three model test settings: GlobalModel, LocalModel, and TransferModel. The classifier is also Ramdom Forest with SMOTE algorithm. All experiment settings keep the same except for the feature selection of frequency. That is to say, the structural features remain as the base and pop each frequency feature to test.

​    Feature schema:

```tex
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

​    The results of each model test are as follow in plots. The variance is not large.

### GlobalModel Test

**Kappa**:

![global_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/GlobalMode_kappa.png?raw=true)

​    Maximal frequency mainly behaves better kappa except 1 year. It is expected to select maximal 100 year as a frequency feature. A weird phenomenon is that 5 year and 100 year have a totally different trend. Moreover, max 100y has the best score while mean 100y does the worst. One possible reason is that the value of the maximal frequency of 100y is relatively much larger than the mean frequency and then it would has a dominant effect.

**Balanced accuracy**:

![global_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/GlobalMode_balanced%20accuracy.png?raw=true)

​    Balanced accuracy shows a similar trend to the kappa. Also, maximal 100y is the most proper one.

### LocalModel Test

**Kappa**:

![local_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/LocalMode_kappa.png?raw=true)

​    Mean frequency would have more better scores and exceed more compared with the maximal, which is different from GlobalModel results. The peak score is contributed by mean 20y. Mean 100y has the second place.

**Balanced accuracy**:

![local_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/LocalMode_balanced%20accuracy.png?raw=true)

​    Mean 20y again show the best balanced accuracy and the second place comes to maximal 500y.

### TransferModel Test

**Kappa**:

![transfer_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/TransferMode_kappa.png?raw=true)

​    

​    Lines od mean and maximal are interweaved. Mean 20y has the best score then mean 100y and maximal 100y similar do the next. However, the average value of kappas is poor than GlobalModel's and LocalModel's. 

**Balanced Accuracy**:

![transfer_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/Google_Ngrams/readme.assets/TransferMode_balanced%20accuracy.png?raw=true)

​    

A similar trend to the kappa's shows that mean 20y and mean 100y are the best two features.

### Conclusion

1. Neither kappa nor balanced accuracy has direct relation with the time period. It means that the frequency features from Google Ngram can be used without considering the corpus size (the size of Ngram in 1 year is large enough). Therefore, we want to only select the best ones to train.
2. Frequency in mean or maximum does not matter too much in the most cases. Only GlobalModel in the experiment, maximums do better than means. The final best frequency features would come from the next step: Feature selection.
3. Mentioned in the first research question, Hypothesis 1, and the presentation, GlobalModel and Transfermodel are more meaningful to refer when predicting in the large-scale WordNet. Therefore, I prefer to adopting maximal 100y as one of the frequency features when trainning models.

## Frequency Feature Selection

feature_selection.ipynb

​    To discover the best frequency features setting, a wrapper method of feature selection is performed. We can deploy bottom-up and top-down approach to check which setting would perform the highest kappa value. We consider all three model tests. However, there is no Grip Search for LocalModel because the running time is too long and make no significant contribution to the final large-scale prediction.

### GlobalModel

#### Bottom-up

​    After selection of three rounds, the highest kappa value reaches **0.70208**. The selected frequency features are ['ngram_100y_max', 'ngram_200y_max']. The importance is ranked as follows:

| feature                         | importance |
|:------------------------------- |:----------:|
| depthfromtopsynset_normalised_x | 0.39058    |
| glosslength_normalised_x        | 0.15243    |
| minwordlength_x                 | 0.11309    |
| nrpartrels_normalised_x         | 0.07871    |
| ngram_100y_max                  | 0.06703    |
| ngram_200y_max                  | 0.06691    |
| nrhypos_x                       | 0.05024    |
| polyscore_max_x                 | 0.04744    |
| nroflemmas_x                    | 0.03083    |
| nrdirhypers_x                   | 0.00275    |

#### Top-down

​    Two rounds selection, the highest kappa is **0.69925** and it uses all the frequency features except ['ngram_200y_mean']. The importance is ranked as follows:

| feature                         | importance |
|:------------------------------- |:----------:|
| depthfromtopsynset_normalised_x | 0.322882   |
| glosslength_normalised_x        | 0.125023   |
| minwordlength_x                 | 0.085909   |
| nrpartrels_normalised_x         | 0.069496   |
| ngram_500y_max                  | 0.049746   |
| nrhypos_x                       | 0.031885   |
| ngram_400y_max                  | 0.031766   |
| polyscore_max_x                 | 0.029908   |
| ngram_100y_max                  | 0.0239     |
| ngram_200y_max                  | 0.02339    |
| nroflemmas_x                    | 0.022488   |
| ngram_50y_max                   | 0.016483   |
| ngram_5y_max                    | 0.016481   |
| ngram_1y_max                    | 0.016045   |
| ngram_20y_max                   | 0.015947   |
| ngram_1y_mean                   | 0.014342   |
| ngram_10y_max                   | 0.014059   |
| ngram_5y_mean                   | 0.013772   |
| ngram_400y_mean                 | 0.013606   |
| ngram_100y_mean                 | 0.012761   |
| ngram_10y_mean                  | 0.012401   |
| ngram_50y_mean                  | 0.012392   |
| ngram_500y_mean                 | 0.012062   |
| ngram_20y_mean                  | 0.010859   |
| nrdirhypers_x                   | 0.002399   |

#### Grid Search

​    Learning from hyper-parameter tuning in machine learning, I design a brute force grid search among 18 frequency features which consumes a huge computation. It is a valid method to find the best selection of frequency features. One of the best combination is ['ngram_50y_max', 'ngram_100y_max', 'ngram_400y_mean', 'ngram_500y_max'] which contributes to the kappa of 0.71443.

### LocalModel

#### Bottom-up

    Three rounds selection can reach the top kappa: **0.71150**. The selected frequency features are ['ngram_20y_mean', 'ngram_100y_max', 'ngram_400y_mean']. The importance of each feature are as follows:

| feature                         | importance |
|:------------------------------- |:----------:|
| depthfromtopsynset_normalised_x | 0.264289   |
| minwordlength_x                 | 0.173495   |
| glosslength_normalised_x        | 0.166164   |
| nrhypos_x                       | 0.165204   |
| ngram_100y_max                  | 0.088688   |
| polyscore_max_x                 | 0.052278   |
| ngram_400y_mean                 | 0.04684    |
| nroflemmas_x                    | 0.029758   |
| nrpartrels_normalised_x         | 0.010771   |
| nrdirhypers_x                   | 0.002513   |

#### Top-down

    Four rounds remove ['ngram_200y_max', 'ngram_10y_max', 'ngram_100y_mean', 'ngram_10y_mean'] and select out the rest frequency features. The best kappa is **0.68451**. The importance of each feature are as follows:

| feature                         | importance |
|:------------------------------- |:----------:|
| depthfromtopsynset_normalised_x | 0.184621   |
| minwordlength_x                 | 0.12032    |
| glosslength_normalised_x        | 0.116253   |
| nrhypos_x                       | 0.107713   |
| ngram_1y_mean                   | 0.050102   |
| ngram_5y_mean                   | 0.042889   |
| ngram_5y_max                    | 0.038203   |
| polyscore_max_x                 | 0.037909   |
| ngram_400y_max                  | 0.035455   |
| ngram_500y_max                  | 0.034278   |
| ngram_1y_max                    | 0.031795   |
| ngram_20y_max                   | 0.030439   |
| ngram_50y_max                   | 0.027937   |
| ngram_100y_max                  | 0.025723   |
| ngram_20y_mean                  | 0.025324   |
| nroflemmas_x                    | 0.023035   |
| ngram_50y_mean                  | 0.017522   |
| ngram_200y_mean                 | 0.014718   |
| ngram_400y_mean                 | 0.014466   |
| ngram_500y_mean                 | 0.014122   |
| nrpartrels_normalised_x         | 0.006009   |
| nrdirhypers_x                   | 0.001169   |

### TransferModel

#### Bottom-up

​    After a selection of five rounds, the kappa reaches to the highest at **0.58824**. The selected frequency features are ['ngram_20y_mean', 'ngram_500y_max', 'ngram_50y_mean', 'ngram_100y_mean']. The importance is ranked as follows:

| feature                         | importance |
|:------------------------------- |:----------:|
| depthfromtopsynset_normalised_x | 0.35870    |
| glosslength_normalised_x        | 0.14826    |
| minwordlength_x                 | 0.12008    |
| ngram_500y_max                  | 0.08411    |
| nrpartrels_normalised_x         | 0.06752    |
| polyscore_max_x                 | 0.04343    |
| ngram_100y_mean                 | 0.03964    |
| ngram_50y_mean                  | 0.03949    |
| ngram_20y_mean                  | 0.03827    |
| nrhypos_x                       | 0.03214    |
| nroflemmas_x                    | 0.02598    |
| nrdirhypers_x                   | 0.00239    |

#### Top-down

After six rounds of the selection, 14 frequency features left contribute the best kappa, **0.57917**. The removed features are ['ngram_1y_mean', 'ngram_200y_max', 'ngram_20y_max', 'ngram_10y_max']. The importance is ranked as follows:

| feature                         | importance |
|:------------------------------- |:----------:|
| depthfromtopsynset_normalised_x | 0.32094    |
| glosslength_normalised_x        | 0.12513    |
| minwordlength_x                 | 0.10098    |
| nrpartrels_normalised_x         | 0.06637    |
| ngram_500y_max                  | 0.06274    |
| polyscore_max_x                 | 0.03733    |
| ngram_400y_max                  | 0.03627    |
| ngram_100y_max                  | 0.02885    |
| ngram_50y_max                   | 0.02511    |
| nrhypos_x                       | 0.02478    |
| nroflemmas_x                    | 0.02124    |
| ngram_100y_mean                 | 0.01992    |
| ngram_50y_mean                  | 0.01871    |
| ngram_1y_max                    | 0.01725    |
| ngram_5y_max                    | 0.01723    |
| ngram_20y_mean                  | 0.01685    |
| ngram_400y_mean                 | 0.01546    |
| ngram_10y_mean                  | 0.01526    |
| ngram_5y_mean                   | 0.01427    |
| ngram_500y_mean                 | 0.01333    |
| nrdirhypers_x                   | 0.00199    |

#### Grid Search

​    Similar to the grid search setting in GlobalModel, we deploy another one for TransferModel. One of the best combination is ['ngram_5y_mean', 'ngram_50y_mean', 'ngram_100y_mean', 'ngram_200y_max', 'ngram_500y_max'] which contributes to the kappa of 0.58955. 
