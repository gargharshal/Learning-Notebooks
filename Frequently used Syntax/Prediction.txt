# Make predictions using a machine learning model

#choosing the correct model and import
from sklearn.ensemble import RandomForestClassifier

#setup random seed
np.random.seed(42)

#create the input and output
X = heart_disease.drop('target', axis = 1)
y = heart_disease['target']

#split into test and train
X_train, X_test, y_trian, y_test = train_test_split(X, y, test_size = 0.2)

#train the model and instatntiate Random Forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_trian)

#Evalute
clf.score(X_test, y_test)

#################
#M-1 to make prediction
clf.predict(X_test)

#################
#M-2
# predict_proba returns probability of a classification label
# returns the probability of 0, 1 for each input case
clf.predict_proba(X_test[:5])
