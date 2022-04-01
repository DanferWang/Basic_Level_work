# Basic_Level_work
Focusing on Basic Level research. For internship at HCDA, CWI

## Updating Kappa Board

| Type                     | Model         | Kappa     |
| ------------------------ | ------------- | --------- |
| **Structural (WordNet)** | GlobalModel   | 0.67300   |
|                          | LocalModel    | 0.64046   |
|                          | TransferModel | 0.52074   |
| **Frequency (BNC_100M)** | GlobalModel   | 0.68926   |
|                          | LocalModel    | 0.66197   |
|                          | TransferModel | 0.55583   |
| **(Google Ngram)**       | GlobalModel   | 0.71443   |
|                          | *LocalModel*  | *0.68000* |
|                          | TransferModel | 0.58955   |
| **Semantic (W2V)**       |               |           |

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

## Third work: Frequency feature Google Ngram

1. Find out the policy of Google server request limit. Reschedule the sleep strategy to 72 requests then wait 580 seconds every round. It can save 21% of the time on the dataset which is now 11,000 seconds can cover 850 synsets.
2. Read  **Syntactic Annotations for the Google Books Ngram Corpus** and know how Google Ngram corpus organizes the frequency of words.
3. Write a time checker to find how much improvement in speedup. The benchmark is sleeping 10 seconds each request.
4. Write scripts to obtain the frequency features automatically.
5. Calculate the mean and maximal frequency of synsets in 1 year, 5, 10, 20, 50, 100, 200, 400, and 500 years.
6. Design experiments and write codes for Google Ngram year period model test: GlobalModel, LocalModel, and TransferModel. 1 year, 5, 10, 20, 50, 100, 200, 400, and 500 years with mean and max.
7. Simply analyze the results in plots and make some conclusions.
8. Frequency feature selection in GlobalModel and TransferModel using bottom-up, top-down, and grid search methods.
