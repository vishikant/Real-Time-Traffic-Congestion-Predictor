import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
#from sklearn.compose import ColumnTransformer
from sklearn.base import BaseEstimator, TransformerMixin

class TimeFeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X['hour'] = pd.to_datetime(X['timestamp']).dt.hour
        X['day_of_week'] = pd.to_datetime(X['timestamp']).dt.dayofweek
        return X[['hour', 'day_of_week']]
    
def build_pipeline():
    pipeline = Pipeline(steps=[
        ('time_features', TimeFeatureExtractor()),
        ('scaler', StandardScaler())
    ])
    return pipeline