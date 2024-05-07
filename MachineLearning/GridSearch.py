from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

param_grid = {'n_neighbors': [1, 3, 5, 7, 11, 13, 15]}
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
print(f'Geriausi hiperpamatrai: {grid_search.best_params_}')
print(f'Geriausias tikslumas: {grid_search.best_score_}')

best_knn = grid_search.best_estimator_
y_pred_best = best_knn.predict(X_test)

# accuracy_best = accuracy_score(y_test, y_pred_best)
# recall_best = recall_score(y_test, y_pred_best, average='macro')
# precision_best = precision_score(y_test, y_pred_best, average='macro')
# f1_best = f1_score(y_test, y_pred_best, average='macro')

# print("Accuracy: ", accuracy_best)
# print("Recall: ", recall_best)
# print("Precision: ", precision_best)
# print("F1: ", f1_best)

# metrics_after = [accuracy_best, recall_best, precision_best, f1_best]

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred, average='macro')
precision = precision_score(y_test, y_pred, average='macro')
f1 = f1_score(y_test, y_pred, average='macro')

metrics_before = [accuracy, recall, precision, f1]

# print("Accuracy: ", accuracy)
# print("Recall: ", recall)
# print("Precision: ", precision)
# print("F1: ", f1)

metrics_names = ['accuracy', 'recall', 'precision', 'f1']
mean_scores = grid_search.cv_results_['mean_test_score']

# fig, ax = plt.subplots()
# index = range(len(metrics_names))
# bar_width = 0.35
# rects1 = ax.bar(index, metrics_before, bar_width, label='Pries optimizavima')
# rects2 = ax.bar([p + bar_width for p in index], metrics_after, bar_width, label='Po optimizavimo')
# ax.set_xlabel('Metrika')
# ax.set_ylabel('Reiksmes')
# ax.set_title('Modelio veikimo metriku palyginimas')
# ax.set_xticks([p + bar_width / 2 for p in index])
# ax.set_xticklabels(metrics_names)
# ax.legend()
# plt.show()

plt.figure(figsize=(10, 8))
plt.plot(param_grid['n_neighbors'], mean_scores, marker='o')
plt.xlabel('Kaimynu skaicius')
plt.ylabel('Vidutinis tikslumas')
plt.title('KNN modelio tikslumo priklausomybe nuo kaimynu skaiciaus')
plt.grid(True)
plt.show()





