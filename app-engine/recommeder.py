from sklearn.tree import DecisionTreeClassifier
X = [[1, 0], [0, 1]]  # aptitude, preference
y = ["Retail Sales", "Data Entry"]
model = DecisionTreeClassifier().fit(X, y)
print(model.predict([[1, 0]]))  # Output: ['Retail Sales']
