# Basic_Level_work

Focusing on Basic Level research. For internship at HCDA, CWI

## Updating Score Board

| Type                     | Model         | Kappa   | Balanced Accuracy |
| ------------------------ | ------------- | ------- | ----------------- |
| **Structural (WordNet)** | GlobalModel   | 0.67300 | 0.84365           |
|                          | LocalModel    | 0.64046 | 0.82480           |
|                          | TransferModel | 0.52074 | 0.80250           |
| **Frequency (BNC_100M)** | GlobalModel   | 0.68927 | 0.84950           |
|                          | LocalModel    | 0.66197 | 0.84191           |
|                          | TransferModel | 0.55583 | 0.81412           |
| **(Google Ngram)**       | GlobalModel   | 0.71443 | 0.86463           |
|                          | LocalModel    | 0.71150 | 0.86223           |
|                          | TransferModel | 0.58955 | 0.82433           |
| **Semantic (W2V)**       | GlobalModel   | 0.71454 | 0.85938           |
|                          | LocalModel    | 0.69334 | 0.85302           |
|                          | TransferModel | 0.52200 | 0.80478           |
| **(BART)**               | GlobalModel   | 0.88077 | 0.95491           |
|                          | LocalModel    | 0.89768 | 0.95206           |
|                          | TransferModel | 0.70536 | 0.89478           |

## First work: Reproducing Niamh's project

Three experiments in several settings and run to get the results

## Second work: Try different corpora size

Whether corpora size would influence performance on kappa, balanced AVG, and precision

- Splitting the corpora Niamh used in the project into fixed size

- Conducting feature engineering on corpora

- Merging frequency features to synsets in WordNet

- Performing GlobalModel test

- 10 times sampling CHILDES

- The next stage feature engineering

## Third work: Frequency features Google Ngram

1. Find out the policy of Google server request limit. Reschedule the sleep strategy to 72 requests then wait 580 seconds every round. It can save 21% of the time on the dataset which is now 11,000 seconds can cover 850 synsets.
2. Read  **Syntactic Annotations for the Google Books Ngram Corpus** and know how Google Ngram corpus organizes the frequency of words.
3. Write a time checker to find how much improvement in speedup. The benchmark is sleeping 10 seconds each request.
4. Write scripts to obtain the frequency features automatically.
5. Calculate the mean and maximal frequency of synsets in 1 year, 5, 10, 20, 50, 100, 200, 400, and 500 years.
6. Design experiments and write codes for Google Ngram year period model test: GlobalModel, LocalModel, and TransferModel. 1 year, 5, 10, 20, 50, 100, 200, 400, and 500 years with mean and max.
7. Simply analyze the results in plots and make some conclusions.
8. Frequency feature selection in GlobalModel and TransferModel using bottom-up, top-down, and grid search methods.

## Fourth work: Semantic features from Word2Vec

1. Define a pre-trained model, test its validity, and pick the most suitable one.
2. Deal with embeddings with multiword ngrams.
   1. eliminate from the dataset
   2. compute new vectors using the existing model for WordNet
3. Conduct feature engineering for W2V data: distance as similarity
4. Deploy the three model tests with the two solutions to multiwords.
5. Test distance and W2V embedding vectors as semantic features with the three models.

## Fifth work: Semantic features from BART

1. Read literature on BART and Generation of English semantic features
2. Organize the method of generation English semantic features
3. Acquire dataset to train a mapping from words to English features
4. Learn some modules of Transformers
5. Implement and train the BART-based translation model from norms to English semantic features
6. Implement two feature generation models: One to One Gen and One to Some Gen
7. Generate English semantic features for all concepts in the dataset
8. Define a formula and implement to calculate cue validity for each concept
9. Do the three model tests and interpret the results
