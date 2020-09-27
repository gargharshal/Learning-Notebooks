# when all the data is not in numeric format we need to convert in it
# there is 2 types of encoding, for details - https://medium.com/analytics-vidhya/types-of-categorical-data-encoding-schemes-a5bbeb4ba02b

##################
# M-1 One Hot Encoder

# Import car-sales-extended.csv
car_sales = pd.read_csv("../data/car-sales-extended.csv")
car_sales

# Split into X & y and train/test
X = car_sales.drop("Price", axis=1)
y = car_sales["Price"]

# Turn the categories (Make and Colour) into numbers
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

categorical_features = ["Make", "Colour", "Doors"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot", 
                                 one_hot, 
                                 categorical_features)],
                                 remainder="passthrough")
transformed_X = transformer.fit_transform(X)
transformed_X

#################3
# M-2,
# This method is ineficient and hence, not used  
# dummies = pd.get_dummies(car_sales[["Make", "Colour", "Doors"]])
# dummies

# Now Build Machine learning model
# this model return a number (instead of binary), other than that it is similar to classfier

from sklearn.ensemble import RandomForestRegressor 
model = RandomForestRegressor()
model.fit(x_train, y_train)