from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import plot_tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('marketing_campaign.xlsx')
# print(df.head())
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'])
df['Year'] = df['Dt_Customer'].dt.year
df['Month'] = df['Dt_Customer'].dt.month
df['Day'] = df['Dt_Customer'].dt.day

df.drop('Dt_Customer', axis=1, inplace=True)
categorical_features = ['Education', 'Marital_Status']
one_hot_encoder = OneHotEncoder()
transformer = ColumnTransformer(transformers=[('encoder', one_hot_encoder, categorical_features)],
                                remainder='passthrough')
# print(transformer)
X = df.drop('Response', axis=1)
y = df['Response']
X = transformer.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
regressor = DecisionTreeRegressor(random_state=42)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse: .2f}')

plt.figure(figsize=(20, 10))
plot_tree(regressor, filled=True, feature_names=transformer.get_feature_names_out(), rounded=True, max_depth=3, fontsize=8)
plt.show()