import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier
from imblearn.pipeline import make_pipeline
from sklearn.metrics import classification_report, cohen_kappa_score, balanced_accuracy_score
from itertools import combinations

import warnings
warnings.filterwarnings("ignore")

# read the pre-processed data all agreed
data = pd.read_csv('./features_google_ngram.csv', index_col=None)
base_feature = ['nrdirhypers_x',
                'nrhypos_x',
                'nrpartrels_normalised_x',
                'depthfromtopsynset_normalised_x',
                'glosslength_normalised_x',
                'minwordlength_x',
                'nroflemmas_x',
                'polyscore_max_x']

target = ['vote_x']

candidate_feature_list = ['ngram_1y_mean', 'ngram_1y_max',
                          'ngram_5y_mean', 'ngram_5y_max',
                          'ngram_10y_mean', 'ngram_10y_max',
                          'ngram_20y_mean', 'ngram_20y_max',
                          'ngram_50y_mean', 'ngram_50y_max',
                          'ngram_100y_mean', 'ngram_100y_max',
                          'ngram_200y_mean', 'ngram_200y_max',
                          'ngram_400y_mean', 'ngram_400y_max',
                          'ngram_500y_mean', 'ngram_500y_max']

# split training set and testing set using K-Flod
def new_features_global_model_test(dataset, feature, new_features, target):
    K = 10
    random_seed = 7 # R
    data = dataset.reset_index()
    if new_features == None:
        feature_list = feature
    else:
        feature_list = feature + [new_features]
    X = data[feature_list]
    y = data[target]

    K_Flod = StratifiedKFold(n_splits=K, shuffle=True, random_state=random_seed)
    K_Flod.get_n_splits(X, y)
    cohen_kappa = []
    balanced_acc = []
    for train_index, test_index in K_Flod.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        # SMOTE algorithm
        smote = SMOTE(random_state=random_seed, k_neighbors=2)
        X_train, y_train = smote.fit_resample(X_train, y_train)

        # define random forest model
        rf = RandomForestClassifier(random_state=random_seed, max_features='sqrt', n_estimators=1400, min_samples_split=2, min_samples_leaf=1, max_depth=50, oob_score=True, criterion='gini', bootstrap=True).fit(X_train, y_train)

        # predict and make score
        pipeline = make_pipeline(smote, rf)
        y_pred = pipeline.predict(X_test)

        kappa = cohen_kappa_score(y_test, y_pred)
        cohen_kappa.append(kappa)
        balanced_accuracy = balanced_accuracy_score(y_test, y_pred)
        balanced_acc.append(balanced_accuracy)

    result_kappa = np.mean(cohen_kappa)

    # importance of features
    importance = rf.feature_importances_
    importance = pd.DataFrame([feature_list, importance]).transpose()
    importance = importance.rename(columns={0:'feature', 1:'importance'}).sort_values('importance', ascending=False)

    return result_kappa, importance

grid_base = base_feature
grid_candidate = candidate_feature_list

best_kappa = 0
best_importance = None

print('Start...')
for candidate_num in range(len(grid_candidate)):
    candidate_num += 1
    candidate_sets = list(combinations(candidate_feature_list, candidate_num))
    for candidate_group in candidate_sets:
        candidate_group = list(candidate_group)
        training_features = grid_base + candidate_group
        kappa, importance = new_features_global_model_test(data, training_features, None, target)
        if kappa > best_kappa:
            best_kappa = kappa
            best_importance = importance
            string = 'Features: ' + str(candidate_group) + ' kappa=' + str(best_kappa) + '\n'
            with open('./grid_search_GlobalModel.txt', 'a+') as f:
                f.write(string)
            print(string)
with open('./grid_search_GlobalModel.txt', 'a+') as f:
    f.write(importance)
print('Finish!')