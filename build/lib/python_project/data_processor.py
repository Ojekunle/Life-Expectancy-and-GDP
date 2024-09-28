import pandas as pd

class DataProcessor:
    """Class to handle data cleaning and preparation."""

    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data

    def clean_data(self):
        """
        Cleans the data by handling missing values and ensuring correct data types.
        Fills missing values with the median and converts data types where necessary.
        """
        self.data = self.data.fillna(self.data.median(numeric_only=True))
        self.data['Year'] = self.data['Year'].astype(int)
        self.data['GDP'] = self.data['GDP'].astype(float)
        return self.data
