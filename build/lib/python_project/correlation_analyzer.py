import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class CorrelationAnalyzer:
    """Class to analyze and visualize correlations between numerical variables."""

    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data

    def compute_correlation(self):
        """
        Computes and displays the correlation matrix for numerical columns in the data.
        """
        numerical_data = self.data.select_dtypes(include=['number'])
        correlation_matrix = numerical_data.corr()
        return correlation_matrix

    def plot_correlation(self):
        """
        Plots the correlation matrix using a heatmap for visualization.
        """
        numerical_data = self.data.select_dtypes(include=['number'])
        plt.figure(figsize=(10, 6))
        sns.heatmap(numerical_data.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix')
        plt.show()
