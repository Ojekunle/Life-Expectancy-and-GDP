import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class PredictiveModel:
    """Class to train a predictive model and make future predictions."""

    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data
        self.model = None

    def train_model(self, feature_col, target_col):
        """
        Trains a linear regression model using specified feature and target columns.
        """
        X = self.data[[feature_col]].values.reshape(-1, 1)
        y = self.data[target_col].values
        self.model = LinearRegression().fit(X, y)

    def predict_future(self, future_values):
        """
        Predicts future target values based on provided future feature values.
        """
        if not self.model:
            raise ValueError("Model has not been trained yet.")
        future_values = np.array(future_values).reshape(-1, 1)
        predictions = self.model.predict(future_values)
        return predictions
