#sklearn syntax

#import required libraries

# We'll use a Random Forest (for classification problem)
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()


# Create X (all the feature columns)
X = heart_disease.drop("target", axis=1)

# Create y (the target column)
y = heart_disease["target"]

# Split the data into training and test sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y)



#to train the model
clf.fit(X_train, y_train)

# Evaluate the model on the training set
clf.score(X_train, y_train)

# other evaluation methods
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

classification_report(y_test, y_preds)
confusion_matrix(y_test, y_preds)
accuracy_score(y_test, y_preds)

# Use the model to make a prediction on the test data (further evaluation)
y_preds = clf.predict(X_test)


# to find the parameters of the model
clf.get_params()

