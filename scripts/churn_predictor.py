import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load processed parquet
df = pd.read_parquet("s3://telco-churn-data-hauwa/processed/")

# Drop non-numeric and customerID
df = df.drop(columns=['customerID'])
df = pd.get_dummies(df)

X = df.drop('Churn_Yes', axis=1)
y = df['Churn_Yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))
