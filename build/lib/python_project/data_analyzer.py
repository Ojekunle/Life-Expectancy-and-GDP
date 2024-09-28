import pandas as pd


class DataAnalyzer:
    """Class to perform statistical analysis on the data."""

    def __init__(self, data):
        """Initialize with a DataFrame."""
        self.data = data

    def calculate_statistics(self):
        """
        Calculates basic statistics like mean, median, and standard deviation
        for life expectancy and GDP.
        """
        life_expectancy_stats = self.data['Life expectancy at birth (years)'].describe()
        gdp_stats = self.data['GDP'].describe()
        return life_expectancy_stats, gdp_stats

    def analyze_life_expectancy(self):
        """
        Analyzes life expectancy trends over the years and returns average life expectancy per year.
        """
        avg_life_expectancy = self.data.groupby('Year')['Life expectancy at birth (years)'].mean()
        return avg_life_expectancy
