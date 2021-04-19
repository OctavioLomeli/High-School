from sklearn import neighbors
from sklearn import tree
import numpy as np
import pandas as pd


print("Which dataset will you want to work with?\n1. Wine Quality\n2. Cereal\n3. Iris Flowers\n4. Heart Failure")
choice = int(input("Enter the number near the dataset you wish to use:  "))
print()

if choice == 1:
  df = pd.read_csv("csv_files/winequality-red.csv")
elif choice == 2:
  df = pd.read_csv("csv_files/cereal.csv")
  df.drop(["name", "mfr", "type"], axis=1, inplace=True)
elif choice == 3:
  df = pd.read_csv("csv_files/iris.csv")
  df.drop(['Id'], axis=1, inplace=True)
  df = df.sample(frac=1)
else:
  df = pd.read_csv("csv_files/heart_failure.csv")
  df = df.sample(frac=1)

for index in range(len(df.columns)):
  print(index, df.columns[index])

while True:
  try:
    index_of_target = int(input("\nEnter the number near the column that you want as the target: "))
    10/0 if not (0 <= index_of_target <= len(df.columns) - 1) else 2/1
    break

  except:
    print("Enter a valid number.\n")
  
target_list = [df.columns[index_of_target]]
feature_list = [column for column in df.columns if column != df.columns[index_of_target]] 


# splitting the dataframe into targets and features
target_df = df[target_list]
feature_df = df[feature_list]

# number of samples
len_data = len(df)

# splitting the training and testing data
# 90% for training, 10% for testing
num_train = round((len_data * .9))

num_test = round((len_data * .1))

X = feature_df[:num_train]

X_test = feature_df[num_train: ]

Y = target_df[:num_train]
Y_test = target_df[num_train: ]

# Decision tree
dec_tree = tree.DecisionTreeRegressor()

# Training decision tree on training data
dec_tree = dec_tree.fit(X, Y)

# predictions for the training data
print("\nDecision Tree")
print('Prediction:')
print([round(element, 1) for element in dec_tree.predict(X_test)])
print('Actual Values:')
print([round(element[0], 1) for element in Y_test.to_numpy()]) 
correct = 0
for index in range(len(dec_tree.predict(X_test))):
  if dec_tree.predict(X_test)[index] == [element[0] for element in Y_test.to_numpy()][index]:
    correct += 1
print(f"Correct: {correct} out of {len(dec_tree.predict(X_test))}")
print("\nKNN")


# KNN
# converting to numpy array
X = X.to_numpy()
Y = Y.to_numpy()
X_test = X_test.to_numpy()
Y_test = Y_test.to_numpy()

# number of neighbors
n_neighbors = int(input("Enter number of neighbors: "))

# Create a KNN Model
knn = neighbors.KNeighborsRegressor(n_neighbors=n_neighbors)

# Train the model
knn.fit(X, Y)

# Predict samples on X_test
# predictions for the training data
print('Prediction:')
print([round(element[0], 1) for element in knn.predict(X_test)])
print('Actual Values:')
print([round(element[0], 1) for element in Y_test])
correct = 0
for index in range(len(knn.predict(X_test))):
  if knn.predict(X_test)[index] == [element[0] for element in Y_test][index]:
    correct += 1
print(f"Correct: {correct} out of {len(Y_test)}")
