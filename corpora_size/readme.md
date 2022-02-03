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

**The tables and figures are updated with 50 samplings' averaged results.**

### Results on kappa

|             |   1M    |  2.4M   |  5.7M   |    100M    |
| :---------: | :-----: | :-----: | :-----: | :--------: |
|   **BNC**   | 0.67999 | 0.67486 | 0.67536 |  0.68926   |
| **CHILDES** | 0.66660 | 0.67355 | 0.67473 |            |
|  **CABNC**  | 0.67382 | 0.67205 |         |            |
|  **KBNC**   | 0.68617 |         |         |            |
| **NGrams**  |         |         |         | *0.677357* |

![kappa](https://github.com/DanferWang/Basic_Level_work/raw/main/corpora_size/readme.assets/size_output_kappa.png)

BNC's are distinct from others rather than CHILDES the last setting.

### Results on balanced accuracy

|             |   1M    |  2.4M   |  5.7M   |    100M    |
| :---------: | :-----: | :-----: | :-----: | :--------: |
|   **BNC**   | 0.84349 | 0.84258 | 0.84228 |  0.84950   |
| **CHILDES** | 0.84088 | 0.84519 | 0.84554 |            |
|  **CABNC**  | 0.84027 | 0.83978 |         |            |
|  **KBNC**   | 0.84835 |         |         |            |
| **NGrams**  |         |         |         | *0.838679* |

![acc](https://github.com/DanferWang/Basic_Level_work/raw/main/corpora_size/readme.assets/size_output_acc.png)

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


# Several times sampling

In order to find whether there is dependency between the kappa value and its corpus size, I deploy 50 times sampling for BNC, CHILDES, and CABNC with corresonding size in the previous setting. Then, performing the GlobalModel test can give us kappa values and balanced accuracy saved in .npy file.

LocalModel test and TransferModel test are also conducted. The values of kappa and balanced accuracy each setting are the mean results of five correspoding models in every sampling.

To find out whether there is a dependency between the size of a corpus and the results, we perform Wilcoxon rank-sum test. The null hypothesis of the test is that the results by different sizes of one corpus are from the same distribution. The p-value of the tests are as follows:

### GlobalModel Test

|     kappa     |  CABNC  | CHILDES |    BNC     |
| :-----------: | :-----: | :-----: | :--------: |
|  **1M-2.4M**  | 0.35561 | 0.00043 |  0.01495   |
|  **1M-5.7M**  |         | 0.00012 |  0.03431   |
|  **1M-100M**  |         |         | 2.4536e-5  |
| **2.4M-5.7M** |         | 0.68420 |  0.82004   |
| **2.4M-100M** |         |         | 7.6277e-11 |
| **5.7M-100M** |         |         | 1.8512e-8  |

| balanced accuracy |  CABNC  |  CHILDES  |    BNC    |
| :---------------: | :-----: | :-------: | :-------: |
|    **1M-2.4M**    | 0.23032 | 8.1844e-6 |  0.36648  |
|    **1M-5.7M**    |         | 5.1090e-6 |  0.28218  |
|    **1M-100M**    |         |           | 1.8692e-6 |
|   **2.4M-5.7M**   |         |  0.93133  |  0.78274  |
|   **2.4M-100M**   |         |           | 1.0752e-8 |
|   **5.7M-100M**   |         |           | 3.8451e-8 |

### LocalModel Test

|     kappa     |  CABNC  | CHILDES |    BNC    |
| :-----------: | :-----: | :-----: | :-------: |
|  **1M-2.4M**  | 0.24400 | 0.07197 |  0.00205  |
|  **1M-5.7M**  |         | 0.00253 |  0.01307  |
|  **1M-100M**  |         |         | 2.1711e-8 |
| **2.4M-5.7M** |         | 0.14964 |  0.50369  |
| **2.4M-100M** |         |         |  0.00688  |
| **5.7M-100M** |         |         |  0.00041  |

| balanced accuracy |   CABNC   | CHILDES |    BNC     |
| :---------------: | :-------: | :-----: | :--------: |
|    **1M-2.4M**    | 1.5527e-7 | 0.22766 |  0.01075   |
|    **1M-5.7M**    |           | 0.02054 |  0.00231   |
|    **1M-100M**    |           |         | 7.1346e-10 |
|   **2.4M-5.7M**   |           | 0.13111 |  0.67410   |
|   **2.4M-100M**   |           |         | 1.8709e-7  |
|   **5.7M-100M**   |           |         | 6.7998e-7  |

### TransferModel Test

|     kappa     |   CABNC   | CHILDES |    BNC     |
| :-----------: | :-------: | :-----: | :--------: |
|  **1M-2.4M**  | 1.5922e-5 | 0.08114 |  0.06669   |
|  **1M-5.7M**  |           | 0.00069 |  0.00037   |
|  **1M-100M**  |           |         | 2.1730e-11 |
| **2.4M-5.7M** |           | 0.07530 |  0.16797   |
| **2.4M-100M** |           |         | 6.4897e-8  |
| **5.7M-100M** |           |         | 6.7423e-6  |

| balanced accuracy |  CABNC  | CHILDES |   BNC   |
| :---------------: | :-----: | :-----: | :-----: |
|    **1M-2.4M**    | 0.00051 | 0.78274 | 0.00471 |
|    **1M-5.7M**    |         | 0.05273 | 0.01186 |
|    **1M-100M**    |         |         | 0.08114 |
|   **2.4M-5.7M**   |         | 0.08606 | 0.47340 |
|   **2.4M-100M**   |         |         | 0.93407 |
|   **5.7M-100M**   |         |         | 0.33794 |

## Results by the size

With the same size, we try to find which corpus has the best performance each time among 50 samplings. The figures firstly show the plots of kappa and balanced accuracy under GlobalModel.

