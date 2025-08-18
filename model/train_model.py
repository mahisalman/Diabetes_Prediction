import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import json
import os

# Load dataset
df = pd.read_csv("../data/diabetes.csv")  # Adjust path as needed

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier()
}

best_model = None
best_score = 0
metrics_summary = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred)
    }
    metrics_summary[name] = metrics
    if metrics["f1_score"] > best_score:
        best_model = model
        best_score = metrics["f1_score"]

# Save best model and metrics
joblib.dump(best_model, "../app/diabetes_model.pkl")
with open("../app/metrics.json", "w") as f:
    json.dump(metrics_summary, f, indent=4)

print("Model and metrics saved.")