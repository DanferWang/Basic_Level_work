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

## Test results

result_plot.ipynb

### GlobalModel

The importance of each random forest can be found in the notebook.

**The tables and figures are updated with 50 samplings' averaged results.**

#### Results on kappa

|             |   1M    |  2.4M   |  5.7M   |    100M    |
| :---------: | :-----: | :-----: | :-----: | :--------: |
|   **BNC**   | 0.67999 | 0.67486 | 0.67536 |  0.68926   |
| **CHILDES** | 0.66660 | 0.67355 | 0.67473 |            |
|  **CABNC**  | 0.67382 | 0.67205 |         |            |
|  **KBNC**   | 0.68617 |         |         |            |
| **NGrams**  |         |         |         | *0.677357* |



![global_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/updated_50samplings_avg_kappa.png?raw=true)


#### Results on balanced accuracy

|             |   1M    |  2.4M   |  5.7M   |    100M    |
| :---------: | :-----: | :-----: | :-----: | :--------: |
|   **BNC**   | 0.84349 | 0.84258 | 0.84228 |  0.84950   |
| **CHILDES** | 0.84088 | 0.84519 | 0.84554 |            |
|  **CABNC**  | 0.84027 | 0.83978 |         |            |
|  **KBNC**   | 0.84835 |         |         |            |
| **NGrams**  |         |         |         | *0.838679* |

![global_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/updated_50samplings_avg_balancedacc.png?raw=true)

The influence to balanced accuracy is slight.

### LocalModel

#### Results on kappa

|             |   1M    |  2.4M   |  5.7M   |  100M   |
| :---------: | :-----: | :-----: | :-----: | :-----: |
|   **BNC**   | 0.65046 | 0.65689 | 0.65519 | 0.66197 |
| **CHILDES** | 0.64324 | 0.64671 | 0.64875 |         |
|  **CABNC**  | 0.64296 | 0.64473 |         |         |
|  **KBNC**   | 0.63305 |         |         |         |

![local_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/LocalModel_50samplings_avg_kappa.png?raw=true)

#### Results on balanced accuracy

|             |   1M    |  2.4M   |  5.7M   |  100M   |
| :---------: | :-----: | :-----: | :-----: | :-----: |
|   **BNC**   | 0.83332 | 0.83668 | 0.83698 | 0.84191 |
| **CHILDES** | 0.83013 | 0.83154 | 0.83266 |         |
|  **CABNC**  | 0.82858 | 0.83292 |         |         |
|  **KBNC**   | 0.82662 |         |         |         |

![local_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/LocalModel_50samplings_avg_balancedacc.png?raw=true)

### TransferModel

#### Results on kappa

|             |   1M    |  2.4M   |  5.7M   |  100M   |
| :---------: | :-----: | :-----: | :-----: | :-----: |
|   **BNC**   | 0.53205 | 0.53935 | 0.54275 | 0.55583 |
| **CHILDES** | 0.52360 | 0.52084 | 0.51763 |         |
|  **CABNC**  | 0.51049 | 0.51581 |         |         |
|  **KBNC**   | 0.53073 |         |         |         |

![transfer_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/TransferModel_50samplings_avg_kappa.png?raw=true)

#### Results on balanced accuracy

|             |   1M    |  2.4M   |  5.7M   |  100M   |
| :---------: | :-----: | :-----: | :-----: | :-----: |
|   **BNC**   | 0.81148 | 0.81465 | 0.81577 | 0.81412 |
| **CHILDES** | 0.80852 | 0.80833 | 0.80630 |         |
|  **CABNC**  | 0.79613 | 0.79882 |         |         |
|  **KBNC**   | 0.80986 |         |         |         |

![transfer_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/TransferModel_50samplings_avg_balancedacc.png?raw=true)

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

## Wilcoxon rank-sum test on size

copussize_proformance_test.ipynb

To find out whether there is a dependency between the size of a corpus and the results, we perform Wilcoxon rank-sum test. The null hypothesis of the test is that the results by different sizes of one corpus are from the same distribution. The tables are organized by alternative hypothesis that the distribution of sample1 is less, two-sided, or greater than that of sample2 . The p-value of the tests are as follows: (p-values less than 0.05 is **bold**)

Furthermore, the types and audience of corpus are taken into account. The types include written and spoken corpora. The audience include general and children. To be specific, there are four sets of groups. The written is BNC + KBNC. The spoken is CHILDES + CABNC. The general is BNC + CABNC. And the children is KBNC + CHILDES. The tests are conducted similarly to the individual tests. The p-value is rounded with 5 decimals.

### GlobalModel Test

#### Individual

| kappa(less/two-sided/greater) |            CABNC            |            CHILDES            |              BNC              |
| :----------------------------: | :-------------------------: | :---------------------------: | :---------------------------: |
|          **1M-2.4M**           | 0.82220 / 0.35561 / 0.17780 |  **0.00021** / **0.00043** / 0.99979  |  0.99252 / **0.01495** / **0.00748**  |
|          **1M-5.7M**           |                             | **5.9847e-5** / **0.00012** / 0.99994 |  0.98284 / **0.03431** / **0.01716**  |
|          **1M-100M**           |                             |                               |  **1.2268e-5** / **2.4536e-5** / 1.0  |
|         **2.4M-5.7M**          |                             |    0.34210 / 0.68420 / 0.65790    |    0.58998 / 0.82004 / 0.41002    |
|         **2.4M-100M**          |                             |                               | **3.8138e-11** / **7.6277e-11** / 1.0 |
|         **5.7M-100M**          |                             |                               |  **9.2562e-9** / **1.8512e-8** / 1.0  |

| balanced accuracy(less/two-sided/greater) |            CABNC            |               CHILDES                |                 BNC                  |
| :---------------------------------------: | :-------------------------: | :----------------------------------: | :----------------------------------: |
|                **1M-2.4M**                | 0.88484 / 0.23032 / 0.11516 | **4.09222e-6** / **8.1844e-6** / 1.0 |     0.81676 / 0.36648 / 0.18324      |
|                **1M-5.7M**                |                             | **2.5545e-6** / **5.1090e-6** / 1.0  |     0.85891 / 0.28218 / 0.14109      |
|                **1M-100M**                |                             |                                      | **9.3459e-7** / **1.8692e-6** / 1.0  |
|               **2.4M-5.7M**               |                             |     0.53434 / 0.93133 / 0.46566      |     0.60863 / 0.78274 / 0.39137      |
|               **2.4M-100M**               |                             |                                      | **5.3758e-9** / **11.0752e-8** / 1.0 |
|               **5.7M-100M**               |                             |                                      | **1.9226e-8** / **3.8451e-8** / 1.0  |

#### GlobalModel: Types and audience
| kappa(less/two-sided/greater) |         Written: KBNC + BNC         |       Spoken: CHILDES + CABNC       |        General: BNC + CABNC         |  Children: KBNC + CHILDES   |
| :---------------------------: | :---------------------------------: | :---------------------------------: | :---------------------------------: | :-------------------------: |
|          **1M-2.4M**          |       1.0 / **0.0** / **0.0**       | **0.01636** / **0.03272** / 0.98364 | 0.99339 / **0.01323** / **0.00661** | 0.93710 / 0.12579 / 0.06290 |
|          **1M-5.7M**          | 0.99997 / **0.00007** / **0.00003** | **0.00308** / **0.00616** / 0.99692 |     0.86266 / 0.27467 / 0.13734     | 0.86527 / 0.26945 / 0.13473 |
|          **1M-100M**          | **0.00017** / **0.00034** / 0.99983 |                                     |       **0.0** / **0.0** / 1.0       |                             |
|         **2.4M-5.7M**         |     0.58998 / 0.82004 / 0.41002     |     0.07392 / 0.14785 / 0.92608     |     0.35838 / 0.71676 / 0.64162     | 0.34210 / 0.68420 / 0.65790 |
|         **2.4M-100M**         |       **0.0** / **0.0** / 1.0       |                                     |       **0.0** / **0.0** / 1.0       |                             |
|         **5.7M-100M**         |       **0.0** / **0.0** / 1.0       |                                     |       **0.0** / **0.0** / 1.0       |                             |

| balanced accuracy(less/two-sided/greater) |         Written: KBNC + BNC         |       Spoken: CHILDES + CABNC       |    General: BNC + CABNC     |  Children: KBNC + CHILDES   |
| :---------------------------------------: | :---------------------------------: | :---------------------------------: | :-------------------------: | :-------------------------: |
|                **1M-2.4M**                | 0.99990 / **0.00019** / **0.00010** | **0.00742** / **0.01485** / 0.99258 |  0.9187 / 0.1626 / 0.0813   | 0.22259 / 0.44519 / 0.77741 |
|                **1M-5.7M**                | 0.99985 / **0.00030** / **0.00015** |       **0.0** / **0.0** / 1.0       | 0.34654 / 0.69307 / 0.65346 | 0.22558 / 0.45115 / 0.77442 |
|                **1M-100M**                | **0.00016** / **0.00033** / 0.99984 |                                     |   **0.0** / **0.0** / 1.0   |                             |
|               **2.4M-5.7M**               |     0.60863 / 0.78274 / 0.39137     | **0.00012** / **0.00024** / 0.99988 | 0.10899 / 0.21799 / 0.89101 | 0.53434 / 0.93133 / 0.46566 |
|               **2.4M-100M**               |       **0.0** / **0.0** / 1.0       |                                     |   **0.0** / **0.0** / 1.0   |                             |
|               **5.7M-100M**               |       **0.0** / **0.0** / 1.0       |                                     |   **0.0** / **0.0** / 1.0   |                             |

### LocalModel Test

|     kappa(less/two-sided/greater)     |          CABNC          |           CHILDES           |             BNC             |
| :-----------: | :---------------------: | :-------------------------: | :-------------------------: |
|  **1M-2.4M**  | 0.12200 / 0.24400 / 0.87800 | **0.03599**/ 0.07197 / 0.96401 | **0.00103** / 0.00205 / 0.99897 |
|  **1M-5.7M**  |                         | **0.00126** / 0.00253 / 0.99873 | **0.00654** / 0.01307 / 0.99346 |
|  **1M-100M**  |                         |                             |          **1.0856e-8** / **2.1711e-8** / 1.0          |
| **2.4M-5.7M** |                         |   0.07482 / 0.14964 / 0.92518   |           0.75816 / 0.50369 / 0.66295           |
| **2.4M-100M** |                         |                             |           **0.00344** / **0.00688** / 0.99656           |
| **5.7M-100M** |                         |                             |           0.00020 / 0.00041 / 0.99980           |

| balanced accuracy(less/two-sided/greater) |                CABNC                |               CHILDES               |                  BNC                  |
| :---------------------------------------: | :---------------------------------: | :---------------------------------: | :-----------------------------------: |
|                **1M-2.4M**                | **7.7635e-8** / **1.5527e-7** / 1.0 |     0.11383 / 0.22766 / 0.88617     |  **0.00235** / **0.01075** / 0.99765  |
|                **1M-5.7M**                |                                     | **0.01027** / **0.02054** / 0.98973 |  **0.00116** / **0.00231** / 0.99884  |
|                **1M-100M**                |                                     |                                     | **3.5673e-10** / **7.1346e-10** / 1.0 |
|               **2.4M-5.7M**               |                                     |     0.06555 / 0.13111 / 0.93445     |      0.33705 / 0.67410 / 0.66295      |
|               **2.4M-100M**               |                                     |                                     |  **9.3545e-8** / **1.8709e-7** / 1.0  |
|               **5.7M-100M**               |                                     |                                     | **3.3999e-7** /  **6.7998e-7** / 1.0  |

#### LocalModel: Types and audience

| kappa(less/two-sided/greater) |         Written: KBNC + BNC         |       Spoken: CHILDES + CABNC       |        General: BNC + CABNC         |  Children: KBNC + CHILDES   |
| :---------------------------: | :---------------------------------: | :---------------------------------: | :---------------------------------: | :-------------------------: |
|          **1M-2.4M**          |       **0.0** / **0.0** / 1.0       | **0.01253** / **0.02505** / 0.98747 | **0.00387** / **0.00774** / 0.99613 |   **0.0** / **0.0** / 1.0   |
|          **1M-5.7M**          |       **0.0** / **0.0** / 1.0       | **0.00032** / **0.00063** / 0.99968 |     **0.0** / **0.00001** / 1.0     |   **0.0** / **0.0** / 1.0   |
|          **1M-100M**          |       **0.0** / **0.0** / 1.0       |                                     |       **0.0** / **0.0** / 1.0       |                             |
|         **2.4M-5.7M**         |     0.74816 / 0.50369 / 0.25184     |     0.07392 / 0.14785 / 0.92608     | **0.00257** / **0.00513** / 0.99743 | 0.07482 / 0.14964 / 0.92518 |
|         **2.4M-100M**         | **0.00344** / **0.00688** / 0.99656 |                                     |       **0.0** / **0.0** / 1.0       |                             |
|         **5.7M-100M**         | **0.00020** / **0.00041** / 0.99980 |                                     | **0.00020** / **0.00041** / 0.99980 |                             |

| balanced accuracy(less/two-sided/greater) |     Written: KBNC + BNC     |       Spoken: CHILDES + CABNC       |        General: BNC + CABNC         |      Children: KBNC + CHILDES       |
| :---------------------------------------: | :-------------------------: | :---------------------------------: | :---------------------------------: | :---------------------------------: |
|                **1M-2.4M**                |   **0.0** / **0.0** / 1.0   | **0.00002** / **0.00004** / 0.99998 |       **0.0** / **0.0** / 1.0       | **0.00007** / **0.00014** / 0.99993 |
|                **1M-5.7M**                |   **0.0** / **0.0** / 1.0   | **0.00022** / **0.00044** / 0.99978 |       **0.0** / **0.0** / 1.0       |       **0.0** / **0.0** / 1.0       |
|                **1M-100M**                |   **0.0** / **0.0** / 1.0   |                                     |       **0.0** / **0.0** / 1.0       |                                     |
|               **2.4M-5.7M**               | 0.33705 / 0.67410 / 0.66295 | **0.00356** / **0.00712** / 0.99644 | **0.00157** / **0.00314** / 0.99843 |     0.06555 / 0.13111 / 0.93445     |
|               **2.4M-100M**               |   **0.0** / **0.0** / 1.0   |                                     |       **0.0** / **0.0** / 1.0       |                                     |
|               **5.7M-100M**               |   **0.0** / **0.0** / 1.0   |                                     |       **0.0** / **0.0** / 1.0       |                                     |

### TransferModel Test

|     kappa     |                  CABNC                  |               CHILDES               |                  BNC                  |
| :-----------: | :-------------------------------------: | :---------------------------------: | :-----------------------------------: |
|  **1M-2.4M**  | **7.9610e-6** / **1.5922e-5** / 0.99999 |   0.95943 / 0.08114 / **0.04057**   |  **0.00538** / **0.01075** / 0.99462  |
|  **1M-5.7M**  |                                         | 0.99965 / **0.00069** / **0.00035** |  **0.00019** / **0.00037** / 0.99981  |
|  **1M-100M**  |                                         |                                     | **1.0865e-11** / **2.1730e-11** / 1.0 |
| **2.4M-5.7M** |                                         |   0.96235 / 0.07530 / **0.03765**   |      0.08398 / 0.16797 / 0.91602      |
| **2.4M-100M** |                                         |                                     |  **3.2449e-8** / **6.4897e-8** / 1.0  |
| **5.7M-100M** |                                         |                                     |  **3.3712e-6** / **6.7423e-6** / 1.0  |

| balanced accuracy |                CABNC                |             CHILDES             |                 BNC                 |
| :---------------: | :---------------------------------: | :-----------------------------: | :---------------------------------: |
|    **1M-2.4M**    | **0.00026** / **0.00051** / 0.99974 |   0.60863 / 0.78274 / 0.39137   | **0.03335** / **0.06669** / 0.96665 |
|    **1M-5.7M**    |                                     | 0.97364 / 0.05273 / **0.02636** | **0.00593** / **0.01186** / 0.99407 |
|    **1M-100M**    |                                     |                                 |   **0.04057** / 0.08114 / 0.95943   |
|   **2.4M-5.7M**   |                                     | 0.95697 / 0.08606 / **0.04303** |     0.23670 / 0.47340 / 0.76330     |
|   **2.4M-100M**   |                                     |                                 |     0.53297 / 0.93407 / 0.46703     |
|   **5.7M-100M**   |                                     |                                 |     0.83103 / 0.33794 / 0.16897     |

#### TransferModel: Types and audience

| kappa(less/two-sided/greater) |         Written: KBNC + BNC         |   Spoken: CHILDES + CABNC   |        General: BNC + CABNC         |      Children: KBNC + CHILDES       |
| :---------------------------: | :---------------------------------: | :-------------------------: | :---------------------------------: | :---------------------------------: |
|          **1M-2.4M**          | **0.00043** / **0.00086** / 0.99957 | 0.12897 / 0.25793 / 0.87103 | **0.00119** / **0.00239** / 0.99881 | 0.99997 / **0.00005** / **0.00003** |
|          **1M-5.7M**          |       **0.0** / **0.0** / 1.0       | 0.24645 / 0.49289 / 0.75355 |       **0.0** / **0.0** / 1.0       |       1.0 / **0.0** / **0.0**       |
|          **1M-100M**          |       **0.0** / **0.0** / 1.0       |                             |       **0.0** / **0.0** / 1.0       |                                     |
|         **2.4M-5.7M**         |     0.08398 / 0.16797 / 0.91602     | 0.50954 / 0.98092 / 0.49046 |       **0.0** / **0.0** / 1.0       |   0.96235 / 0.0753 / **0.03765**    |
|         **2.4M-100M**         |       **0.0** / **0.0** / 1.0       |                             |       **0.0** / **0.0** / 1.0       |                                     |
|         **5.7M-100M**         |     **0.0** / **0.00001** / 1.0     |                             |     **0.0** / **0.00001** / 1.0     |                                     |

| balanced accuracy(less/two-sided/greater) |         Written: KBNC + BNC         |       Spoken: CHILDES + CABNC       |        General: BNC + CABNC         |      Children: KBNC + CHILDES       |
| :---------------------------------------: | :---------------------------------: | :---------------------------------: | :---------------------------------: | :---------------------------------: |
|                **1M-2.4M**                |       **0.0** / **0.0** / 1.0       |     0.10369 / 0.20738 / 0.89631     | **0.01161** / **0.02321** / 0.98839 | **0.00007** / **0.00014** / 0.99993 |
|                **1M-5.7M**                | **0.00003** / **0.00006** / 0.99997 | **0.00044** / **0.00088** / 0.99956 |       **0.0** / **0.0** / 1.0       |       **0.0** / **0.0** / 1.0       |
|                **1M-100M**                | **0.00063** / **0.00126** / 0.99937 |                                     |       **0.0** / **0.0** / 1.0       |                                     |
|               **2.4M-5.7M**               |     0.23670 / 0.47340 / 0.76330     | **0.00062** / **0.00124** / 0.99938 |       **0.0** / **0.0** / 1.0       |   0.95697 / 0.08606 / **0.04303**   |
|               **2.4M-100M**               |     0.53297 / 0.93407 / 0.46703     |                                     |       **0.0** / **0.0** / 1.0       |                                     |
|               **5.7M-100M**               |     0.83103 / 0.33794 / 0.16897     |                                     |     0.83103 / 0.33794 / 0.16897     |                                     |

## Results by the size

results_by_size.ipynb

With the same size, we try to find which corpus has the best performance each time among 50 samplings. The figures only show the plots of kappa and box plots under GlobalModel, LocalModel, and TransferModel. The balanced accuracy is shown in the notebook.

The overall results by each model are respectively shown in a boxplot with the size.

### GlobalModel

- 1M

![global_1m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_1m_kappa.png?raw=true)
![global_1m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_1m_kappa_box.png?raw=true)

- 2.4M

![global_2_4m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_2_4m_kappa.png?raw=true)
![global_2_4m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_2_4m_kappa_box.png?raw=true)

- 5.7M

![global_5_7m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_5_7m_kappa.png?raw=true)
![global_5_7m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_5_7m_kappa_box.png?raw=true)

- Overall

  ![global_overall](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_kappa_overall_box.png?raw=true)

  ![global_overall](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Global_acc_overall_box.png?raw=true)

### LocalModel

- 1M

![local_1m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_1m_kappa.png?raw=true)
![local_1m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_1m_kappa_box.png?raw=true)

- 2.4M

![local_2_4m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_2_4m_kappa.png?raw=true)
![local_2_4m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_2_4m_kappa_box.png?raw=true)

- 5.7M

![local_5_7m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_5_7m_kappa.png?raw=true)
![local_5_7m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_5_7m_kappa_box.png?raw=true)

- Overall

![local_overall](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_kappa_overall_box.png?raw=true)

![local_overall](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Local_acc_overall_box.png?raw=true)

### TransferModel

- 1M

![transfer_1m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_1m_kappa.png?raw=true)
![transfer_1m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_1m_kappa_box.png?raw=true)

- 2.4M

![transfer_2_4m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_2_4m_kappa.png?raw=true)
![transfer_2_4m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_2_4m_kappa_box.png?raw=true)

- 5.7M

![transfer_5_7m_kappa](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_5_7m_kappa.png?raw=true)
![transfer_5_7m_acc](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_5_7m_kappa_box.png?raw=true)

- Overall

![transfer_overall](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_kappa_overall_box.png?raw=true)

![transfer_overall](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/Transfer_acc_overall_box.png?raw=true)
