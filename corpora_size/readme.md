# Corpora size feature
## Splitting corpora 
- BNC: 100 million, 5.7 million, 2.4 million, and 1 million
- CHILDES: 5.7 million, 2.4 million, and 1 million
- CABNC: 2.4 million and 1 million
- KBNC: 1 million

## Feature engineering
- BNC Sum: The sum of all instances of each lemma per synset in the BNC full text
- CHILDES_Rel_Sum: The sum of all instances of each lemma per synset in the CHILDES corpus, divided by the total number of words in the corpus
- CABNC_Per_100k: The frequency occurrence of all lemmas per synset, per 100,000 words of the CABNC
- KBNC_Sum: The sum of all instances of each lemma per synset in the KBNC

## GlobalModel test
**The results is being processed...** The importance of each random forest can be found in the notebook.

### Results on kappa

|             |     1M     |    2.4M    |    5.7M    |    100M    |
| :---------: | :--------: | :--------: | :--------: | :--------: |
|   **BNC**   |  0.698233  |  0.709009  |  0.712823  | *0.714009* |
| **CHILDES** |  0.685825  |  0.683559  | *0.660334* |            |
|  **CABNC**  |  0.685486  | *0.699077* |            |            |
|  **KBNC**   | *0.691517* |            |            |            |
| **NGrams**  |            |            |            | *0.677357* |

Results in *italics* are the baseline performing Niamh's

![image-20211217130301493](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/image-20211217130301493.png?raw=true)

CHILDES is distinct from others. It uses the relative sum as feature.

### Results on balanced accuracy

|             |    1M     |    2.4M    |    5.7M    |    100M    |
| :---------: | :-------: | :--------: | :--------: | :--------: |
|   **BNC**   | 0.853742  |  0.860044  |  0.860965  | *0.859528* |
| **CHILDES** | 0.854018  |  0.853283  | *0.840341* |            |
|  **CABNC**  | 0.851834  | *0.853742* |            |            |
|  **KBNC**   | *0.85023* |            |            |            |
| **NGrams**  |           |            |            | *0.838679* |

Results in *italics* are the baseline performing Niamh's

![image-20211217130450989](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/image-20211217130450989.png?raw=true)

The influence to balanced accuracy is slight.

## Discussion

- There are many punctuations in corpora. Considering the efficiency and performance of using such features, whether should we eliminate them from the corpora?
- The content from spoken corpora, like CABNC and CHILDES, there are some oral expressions, abbreviations, and some cultural habits of speakers. How do we deal with these?
- The words or lemmas in corpora are with multiple meanings. For example, 'bill' in the domain of tool is not basic level however it might be a basic level in other domains. What to do so our model can differ them?
- The bottleneck would be memory now maybe and future.

## 10 times sampling CHILDES

Because of the unexpected results that kappa values decrease with incremental size of sampled CHILDES. Therefore, we try 10 times sampling for each 1 million, 2.4 million, and 5.7 million from CHILDES and do the same experiments as the pervious.

We have the results saved in _10_times_sampling_CHILDES.npy_ and plot them in the following figure:


The trends are not in regular. There are only two groups that kappa values go up with the size of corpus. And they have no regular patten like 7, 8, 9.

- I guess the reason might be the choice of the feature, relative sum of occurrence counts. But, after my verify this hypothesis, the result plots as follows:

They show a worse situation that only one set agrees to the hypothesis. Most of them are even irregular.

When we turn to the importance of each random forest, the feature of CHILDES sum contributes around 0.04 ranked within the last four positions. This hints that the CHILDES sum is not a important feature.

## Next stage feature engineering

- Maximum, minimum, and sum of occurrences in the same size among corpora.
- Averaged occurrences in each size group of corpora

After, I perform a GlobalModel test:

Initially, I deploy a top-down method. 

- With all new features, kappa: 0.655853, which is lower than the best one using BNC_100M, kappa: 0.714009.

Therefore, top-down method for feature selection is not good for our task.

Next, the feature selection using bottom-up method:

- Step 1 (base: []): add 'min_1m', kappa: 0.715145

- Step 2: (base:['min_1m']): no kappa gain

  **Still tuning...**

