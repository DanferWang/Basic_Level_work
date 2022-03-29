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

# generate the local dataframe for different domains
local_fruit = data.loc[data['domain_x']=='fruit']
local_tool = data.loc[data['domain_x']=='tool']
local_music = data.loc[data['domain_x']=='music']
local_furniture = data.loc[data['domain_x']=='furn']
local_garments = data.loc[data['domain_x']=='garm']

local_list = [local_fruit, local_tool, local_music, local_furniture, local_garments]

# generate the unseen(transfer) dataframe for different domains
unseen_fruit = data.loc[data['domain_x']!='fruit']
unseen_tool = data.loc[data['domain_x']!='tool']
unseen_music = data.loc[data['domain_x']!='music']
unseen_furniture = data.loc[data['domain_x']!='furn']
unseen_garments = data.loc[data['domain_x']!='garm']

unseen_list = [unseen_fruit, unseen_tool, unseen_music, unseen_furniture, unseen_garments]

def new_feature_transfer_model_test(train_list, test_list, base_feature, new_feature, target):
    random_seed = 7 # R
    transfer_kappa_list = []
    # transfer_balancedAcc_list = []
    for counter in range(len(train_list)):
        training_data = train_list[counter].reset_index()
        testing_data = test_list[counter].reset_index()
        if new_feature is None:
            feature_list = base_feature
        else:
            feature_list = base_feature + [new_feature]
        X_train = training_data[feature_list]
        y_train = training_data[target]
        X_test = testing_data[feature_list]
        y_test = testing_data[target]

        # SMOTE algorithm
        smote = SMOTE(random_state=random_seed, k_neighbors=2)
        X_train, y_train = smote.fit_resample(X_train, y_train)

        # define random forest model
        rf = RandomForestClassifier(random_state=random_seed, max_features='sqrt', n_estimators=1400, min_samples_split=2, min_samples_leaf=1, max_depth=50, oob_score=True, criterion='gini', bootstrap=True).fit(X_train, y_train)

        # predict and make score
        pipeline = make_pipeline(smote, rf)
        y_pred = pipeline.predict(X_test)

        kappa = cohen_kappa_score(y_test, y_pred)
        # balanced_accuracy = balanced_accuracy_score(y_test, y_pred)

        transfer_kappa_list.append(kappa)
        # transfer_balancedAcc_list.append(balanced_accuracy)

    transfer_kappa = np.mean(transfer_kappa_list) #, np.mean(transfer_balancedAcc_list)

    # importance of features
    importance = rf.feature_importances_
    importance = pd.DataFrame([feature_list, importance]).transpose()
    importance = importance.rename(columns={0:'feature', 1:'importance'}).sort_values('importance', ascending=False)

    return transfer_kappa, importance

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
        kappa, importance = new_feature_transfer_model_test(unseen_list, local_list, training_features, None, target)
        if kappa > best_kappa:
            best_kappa = kappa
            best_importance = importance
            string = 'Features: ' + str(candidate_group) + ' kappa=' + str(best_kappa) + '\n'
            with open('./grid_search_TransferModel.txt', 'a+') as f:
                f.write(string)
            print(string)
with open('./grid_search_TransferModel.txt', 'a+') as f:
    f.write(importance)
print('Finish!')