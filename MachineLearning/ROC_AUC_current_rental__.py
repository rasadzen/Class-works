from sklearn.metrics import roc_curve, auc
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('current-rental-properties-1.csv')
df['permit_expires'] = pd.to_datetime(df['permit_expires'])
current_date = pd.to_datetime('2023-04-12')
df['expires_soon'] = ((df['permit_expires'] - current_date) / pd.Timedelta(days=1) <= 365).astype(int)

label_encoder = LabelEncoder()
df['property_type'] = label_encoder.fit_transform(df['property_type'])
df['building_type'] = label_encoder.fit_transform(df['building_type'])

X = df[['property_type', 'building_type', 'bedrooms', 'occup_load']]
y = df['expires_soon']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)
y_scores = clf.predict_proba(X_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_test, y_scores)
roc_auc = auc(fpr, tpr)
# print(f'ROC AUC: {roc_auc}')

plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area =%0.2f' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True positive rate')
plt.title('ROC curve')
plt.legend(loc="lower right")
plt.show()
