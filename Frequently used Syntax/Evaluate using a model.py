# Evaluating a ML model

################
#Normal scoring
clf.score(X_train, y_train)

################
# cross_val_score
# Import cross_val_score from the model_selection module
from sklearn.model_selection import cross_val_score
#with cross validation
#the default scoring parameter is 'accuracy' (for classifier)
cross_val_score(clf, X, y, cv = 5)


################
# ROC
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

fpr, tpr, thresholds = roc_curve(y_test, y_probs_positive) 
roc_auc_score(y_test, y_probs_positive)


#Plot the ROC curve
#Plot ROC curve
import matplotlib.pyplot as plt

def plot_roc_curve(fpr, tpr):
    """
    Plots a ROC curve given the false positive rate (fpr)
    and true positive rate (tpr) of a model
    """
    #Plot ROC curve
    plt.plot(fpr, tpr, color = 'orange', label = 'ROC')
    
    #Plot line with no predictive power (baseline)
    plt.plot([0, 1], [0,1], 
             color = 'darkblue', 
             ls = '--', 
             label = 'Guessing')
    
    #customize the plot
    plt.xlabel("False positive rate (fpr)")
    plt.ylabel("True positive rate (tpr)")
    plt.title("Receiver Operating Charaterstics (ROC) Curve")
    plt.legend()
    plt.show()
    
plot_roc_curve(fpr, tpr)



##############
# Confusion Matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test, y_preds)

# Plots heatmap of confusion matrix
fig, ax = plt.subplots(figsize = (3, 3))
ax = sns.heatmap(conf_mat,
                annot = True, #this will populate the boxes with conf_mat info,
                cbar = False) #this will remove the heat bar

ax.set(xlabel = 'True Label', ylabel = 'Predict label')

##############
# Classification Report
from sklearn.metrics import classification_report

print(classification_report(y_test, y_preds))

##############
# R2, MAE, MSE
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

#after creating the model and predicting the output
y_test_mean = np.full(len(y_test), y_test.mean())
r2_score(y_test, y_test_mean) 
# this is zero
r2_score(y_test, y_test)
# this is 1

y_preds = model.predict(X_test)
mae = mean_absolute_error(y_test, y_preds)
mse = mean_squared_error(y_test, y_preds)

##############
# Scoring parameter (for classifier)
#default scoring paramter = accuracy (for classifier)
cv_acc = cross_val_score(clf, X, y, cv = 5, scoring = 'accuracy')
#precision
cv_precision = cross_val_score(clf, X, y, cv = 5, scoring = 'precision')
#Recall
cv_recall = cross_val_score(clf, X, y, cv = 5, scoring = 'recall')
#f1
cv_f1 = cross_val_score(clf, X, y, cv = 5, scoring = 'f1')

#OR
accuracy_score(y_test, y_preds)
precision_score(y_test, y_preds)
recall_score(y_test, y_preds)
f1_score(y_test, y_preds)

##############
# Scoring parameter (for regression)

#default scoring paramter = r2 (for regression)
cv_r2 = cross_val_score(model, X, y, scoring = 'r2')

#OR
r2_score(y_test, y_preds)
mean_absolute_error(y_test, y_preds)
mean_squared_error(y_test, y_preds)

##############
# Classification Report
