#Improve model by tunning hyper parameter




####################
#M-1 RandomizedSearchCV

grid = {'n_estimators' : [10, 100, 200, 500, 1000, 1200],
        'max_depth' : [None, 5, 10, 20 , 30],
        'max_features' : ['auto', 'sqrt'],
        'min_samples_split' : [2, 4, 6],
        'min_samples_leaf' : [1, 2, 4]}

rs_clf = RandomizedSearchCV(estimator = clf,
                            param_distributions = grid, 
                            #the dict defined aboove has all the desired hyperparameter 
                            #and their chosen value 
                            n_iter = 10, #number of combination of parameters to try
                            cv = 5,
                            verbose = 2)
							

#returns best parameter
rs_clf.best_params_

							
####################
#M-2 
							
							
grid_2  = {'n_estimators': [100, 200, 500],
 'max_depth': [ 10, 20, 30],
 'max_features': ['auto', 'sqrt'],
 'min_samples_split': [2],
 'min_samples_leaf': [4]}
 
from sklearn.model_selection import GridSearchCV, train_test_split

np.random.seed(42)

#shuffle the data
heart_disease_shuffled = heart_disease.sample(frac = 1) 

#split the data into X, y
X = heart_disease_shuffled.drop('target', axis = 1)
y = heart_disease_shuffled['target']

# split the data into train, validation, and test 
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                      test_size = 0.2)

#trian the model
clf = RandomForestClassifier(n_jobs = 1)

# Setup GridSearchCV
gs_clf = GridSearchCV(estimator = clf,
                            param_grid = grid_2, 
                            #the dict defined aboove has all the desired hyperparameter 
                            #and their chosen value 
                            cv = 5,
                            verbose = 2)
 
# Fit the RandomizedSearchCV version of clf
gs_clf.fit(X_train, y_train);

gs_clf.best_params_

gs_y_preds = gs_clf.predict(X_test)

#evalute the predictions, this function was defined in the Notebook
gs_metrics = evaluate_preds(y_test, gs_y_preds)