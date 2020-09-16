# What if there were missing values?

#Tells the number of missing values
car_sales_missing.isna().sum()

car_sales_missing["Doors"].value_counts()
####################
#Fill the missing values using pandas

car_sales_missing['Make'].fillna("missing", 
                                 inplace = True)

car_sales_missing['Colour'].fillna("missing", 
                                   inplace = True)

car_sales_missing['Odometer (KM)'].fillna(car_sales_missing['Odometer (KM)'].mean(), 
                                          inplace = True) #Taking the avg

car_sales_missing['Doors'].fillna(4, # filling with max number of doors
                                  inplace = True) 
								  

########################
#Fill missing values with Scikit-Learn

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

#Fill missing values
cat_imputer = SimpleImputer(strategy = 'constant', fill_value = 'missing')
door_imputer = SimpleImputer(strategy = 'constant', fill_value = 4)
num_imputer = SimpleImputer(strategy = 'mean')

# define columns
cat_features = ['Make', 'Colour']
door_features = ['Doors']
num_features = ['Odometer (KM)']

#create an imputer (something that fills the missing data)
imputer = ColumnTransformer([
    ('cat_imputer', cat_imputer, cat_features),
    ('door_imputer', door_imputer, door_features),
    ('num_imputer', num_imputer, num_features)
])

#transform the data
filled_x = imputer.fit_transform(x)
filled_x