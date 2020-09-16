# Save and load a model 

###############
# M-1 pickle
import pickle 

#save an existing model to file
pickle.dump(gs_clf, open('gs_random_forest_model_1.pkl', 'wb'))

# Load the saved model
loaded_pickle_model = pickle.load(open('gs_random_forest_model_1.pkl', 
                                       "rb"))
#Make some predictions
pickle_y_preds = loaded_pickle_model.predict(X_test)
evaluate_preds(y_test, pickle_y_preds)

###############
# M-2 Joblib

from joblib import dump, load

#Save the model to a file
dump(gs_clf, filename = 'gs_random_forest_model_1.joblib')

# Import the saved joblib model
loaded_joblib_model = load(filename = 'gs_random_forest_model_1.joblib')

#Make and evalute joblib predictions
joblib_y_preds = loaded_joblib_model.predict(X_test)
evaluate_preds(y_test, joblib_y_preds)