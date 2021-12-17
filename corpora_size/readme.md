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

|             |    100M    |    5.7M    |    2.4M    |     1M     |
| :---------: | :--------: | :--------: | :--------: | :--------: |
|   **BNC**   | *0.714009* |  0.712823  |  0.709009  |  0.698233  |
| **CHILDES** |            | *0.660334* |  0.683559  |  0.685825  |
|  **CABNC**  |            |            | *0.699077* |  0.685486  |
|  **KBNC**   |            |            |            | *0.691517* |
| **NGrams**  | *0.677357* |            |            |            |

Results in *italics* are the baseline performing Niamh's

![image-20211217130301493](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/image-20211217130301493.png?raw=true)

CHILDES is distinct from others. It uses the relative sum as feature.

### Results on balanced accuracy

|             |    100M    |    5.7M    |    2.4M    |    1M     |
| :---------: | :--------: | :--------: | :--------: | :-------: |
|   **BNC**   | *0.859528* |  0.860965  |  0.860044  | 0.853742  |
| **CHILDES** |            | *0.840341* |  0.853283  | 0.854018  |
|  **CABNC**  |            |            | *0.853742* | 0.851834  |
|  **KBNC**   |            |            |            | *0.85023* |
| **NGrams**  | *0.838679* |            |            |           |

Results in *italics* are the baseline performing Niamh's

![image-20211217130450989](https://github.com/DanferWang/Basic_Level_work/blob/main/corpora_size/readme.assets/image-20211217130450989.png?raw=true)

The influence to balanced accuracy is slight.

## Discussion

- There are many punctuations in corpora. Considering the efficiency and performance of using such features, whether should we eliminate them from the corpora?
- The content from spoken corpora, like CABNC and CHILDES, there are some oral expressions, abbreviations, and some cultural habits of speakers. How do we deal with these?
- The words or lemmas in corpora are with multiple meanings. For example, 'bill' in the domain of tool is not basic level however it might be a basic level in other domains. What to do so our model can differ them?
- The bottleneck would be memory now maybe and future.
