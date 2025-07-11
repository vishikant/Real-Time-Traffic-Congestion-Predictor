import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
from preprocess import build_pipeline
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score

# Load and label data
df = pd.read_csv('/Users/vaishalikant/Downloads/Real-Time-Traffic-Congestion-Predictor/src/historical_traffic.csv')
# Use quantiles (33%, 66%) to label Low/Medium/High dynamically
df['congestion_level'] = pd.qcut(df['travel_time_min'], q=3, labels=["Low", "Medium", "High"])


X = df[['timestamp', 'travel_time_min', 'distance_km']]
y = df['congestion_level']

# Build preprocessing + model pipeline
pipeline = build_pipeline()
X_transformed = pipeline.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

scores = cross_val_score(model, X_transformed, y, cv=5)
print(scores)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))



cm = confusion_matrix(y_test, y_pred, labels=["Low", "Medium", "High"])
sns.heatmap(cm, annot=True, fmt="d", xticklabels=["Low", "Medium", "High"], yticklabels=["Low", "Medium", "High"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


print("Label distribution:")
print(df['congestion_level'].value_counts())

# Save model and pipeline
joblib.dump(model, 'models/traffic_model.pkl')
joblib.dump(pipeline, 'models/preprocess_pipeline.pkl')
