# Semantics: Word2Vec

One of the generative semantic features is from **Word2Vec**, short form **W2V**, which is a famous word embedding method. We try to employ it into the feature group for predicting the basic level.

## Pre-trained models

Using Gensim library, we can have several pre-trained W2V models:

| Name                             | Dataset                                             | Records   | Dimensions |
| -------------------------------- | --------------------------------------------------- | --------- | ---------- |
| fasttext-wiki-news-subwords-300  | Wikipedia 2017 (16B tokens)                         | 999,999   | 300        |
| conceptnet-numberbatch-17-06-300 | ConceptNet, word2vec, GloVe, and OpenSubtitles 2016 | 1,917,247 | 300        |
| word2vec-google-news-300         | Google News (about 100 billion words)               | 3,000,000 | 300        |
| glove-wiki-gigaword-300          | Wikipedia 2014 + Gigaword 5 (6B tokens)             | 400,000   | 300        |
| glove-twitter-200                | Twitter (2B tweets, 27B tokens, 1.2M vocabularies)  | 1,193,514 | 200        |

According to the records and datasets, we decide to employ vectors from concept_300: https://github.com/commonsense/conceptnet-numberbatch

## Multiword ngrams

There are many concepts in multiword ngrams which are not directly in the vocabulary of some pre-trained model vectors, such as glove-wiki-gigaword-300. We have to only choose the models with multiword ngrams, ConceptNet. Otherwise, it is required to continue to train the model with sentences including those multiword ngrams. Plus, we use the latest version 19.08 of ConceptNet_numberbatch.

However, it does not exactly contain all the phrases in our dataset. There are 63 concepts tested not be found in the ConceptNet_numberbatch vocabulary, one of which belongs to the basic level. Therefore, we have two solutions to get the training data:

- Eliminate those which are not included in the vocabulary
  
  - 776 concepts included (174 of them - basic level), 63 concepts missing (1 basic level)

- Compute new vectors for every concepts using a well-trained model

## Semantic Feature Engineering

Because the benchmark classifier we use is Random Forest with SMOTE Algorithm, it is not a good idea to feed the vectors into it directly. The reason is that the vectors contain semantics implicitly not as other structural and frequency features. Therefore, it is necessary to do feature engineering on the W2V data. 

1. The aggregation method would be the vector distance between the concepts and their domain

2. **Otherwise**, use SVM as the classifier.

## Model Tests

### GlobalModel Test

To discover the efficiency of semantic features, we first only test with the structural and semantic features, no frequency features involved. It could reveal how much the semantic features would contribute to improve.

**Benchmark: Random Forest**

    **Structural+W2V distance**:

- kappa: 0.71454

- balanced accuracy: 0.85938

### LocalModel Test

Similar to GlobalModel Test, 

**Benchmark: Random Forest**

    **Structural+W2V distance**:

- kappa: 0.69334

- balanced accuracy: 0.85302

### TransferModel Test

Also similar to GlobalModel Test,

**Benchmark: Random Forest**

    **Structural+W2V distance**:

- kappa: 0.52200

- balanced accuracy: 0.80478
