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
The importance of each random forest can be found in the notebook.

### Results on kappa

|             |     1M     |    2.4M    |    5.7M    |    100M    |
| :---------: | :--------: | :--------: | :--------: | :--------: |
|   **BNC**   |  0.687879  |  0.684052  |  0.689859  | *0.686256* |
| **CHILDES** |  0.665358  |  0.669301  | *0.673659* |            |
|  **CABNC**  |  0.674959  | *0.687207* |            |            |
|  **KBNC**   | *0.687594* |            |            |            |
| **NGrams**  |            |            |            | *0.677357* |

Results in *italics* are the baseline performing Niamh's



BNC's are distinct from others rather than CHILDES the last setting.

### Results on balanced accuracy

|             |     1M     |    2.4M    |    5.7M    |    100M    |
| :---------: | :--------: | :--------: | :--------: | :--------: |
|   **BNC**   |  0.846003  |  0.849977  |  0.851492  | *0.847429* |
| **CHILDES** |  0.842183  |  0.843092  | *0.844433* |            |
|  **CABNC**  |  0.838758  | *0.847429* |            |            |
|  **KBNC**   | *0.850898* |            |            |            |
| **NGrams**  |            |            |            | *0.838679* |

Results in *italics* are the baseline performing Niamh's



The influence to balanced accuracy is slight.

## Discussion

- There are many punctuations in corpora. Considering the efficiency and performance of using such features, whether should we eliminate them from the corpora?
- The content from spoken corpora, like CABNC and CHILDES, there are some oral expressions, abbreviations, and some cultural habits of speakers. How do we deal with these?
- The words or lemmas in corpora are with multiple meanings. For example, 'bill' in the domain of tool is not basic level however it might be a basic level in other domains. What to do so our model can differ them?
- The bottleneck would be memory now maybe and future.

## Several times sampling CHILDES

Because of the unexpected results that kappa values decrease with incremental size of samplings. Therefore, we try several times sampling for each 1 million, 2.4 million, 5.7 million, and 100 million from respective corpora and do the same experiments as the pervious.



## Next stage feature engineering

- Maximum, minimum, and sum of occurrences in the same size among corpora.
- Averaged occurrences in each size group of corpora

After, I perform a GlobalModel test:

Initially, I deploy a top-down method. 

- With all new features, kappa: 0.638242, which is lower than the best one using BNC_5_7M, kappa: 0.689859.

Therefore, top-down method for feature selection is not good for our task.

Next, the feature selection using bottom-up method:

- Step 1 (base: []): add 'avg_bnc', kappa: 0.706174

- Step 2: (base:['avg_bnc']): add 'max_1m', kappa: 0.707928

- Step 3: (base: ['avg_bnc', 'max_1m']): no kappa gains

  **Still tuning...**

