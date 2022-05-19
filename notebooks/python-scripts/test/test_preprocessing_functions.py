from unittest import TestCase
import numpy as np
from preprocessing_functions import categorize_gdp_per_capita_value, rename_columns,\
    pivot_dataset, fill_nulls_keeping_one_value_column, preprocess_world_bank_data, \
    categorize_secure_internet_servers_per_million_people
import pandas as pd


class TestPreprocessingFunctions(TestCase):
    def test_categorize_gdp_per_capita_value(self):
        actual = [categorize_gdp_per_capita_value(x) for x in [3230, 13673.23, 667.11, 4096, 1045.99]]
        expected = ['lower_middle', 'high', 'low', 'upper_middle', 'low']
        self.assertEqual(actual, expected)

    def test_rename_columns(self):
        test_df = pd.DataFrame({'Test Col 1 [text here]': [1], 'BREAD [12] Not Cool': [2]})
        actual = set(rename_columns(test_df).columns.values)
        expected = {'test_col_1', 'bread_not_cool'}
        self.assertSetEqual(actual, expected)

    def test_pivot_dataset(self):
        test_df = pd.DataFrame({
            'country_name': ['Denmark', 'Denmark', 'Denmark', 'Bulgaria', 'Bulgaria', 'Bulgaria'],
            'series_name': ["jobs", "stores", "places", "jobs", "stores", "places"],
            '2021': [1, 2, 3, 4, 5, 6]})
        actual = set(pivot_dataset(test_df).columns.values)
        expected = {'country_name', 'jobs', 'stores', 'places'}
        self.assertSetEqual(actual, expected)

    def test_fill_nulls_keeping_one_value_column(self):
        test_df = pd.DataFrame({
            'country_name': ['Denmark', 'Denmark', 'Denmark', 'Bulgaria', 'Bulgaria', 'Bulgaria'],
            'series_name': ["jobs", "stores", "places", "jobs", "stores", "places"],
            '2020': [1, 2, 3, 4, 5, 6],
            '2021': [None, 6, 5, None, 3, 2]})
        expected_values = {1, 6, 5, 4, 3, 2}
        expected_columns = {'country_name', 'series_name', '2021'}
        new_dataset = fill_nulls_keeping_one_value_column(test_df)

        actual_columns = set(new_dataset.columns.values)
        self.assertSetEqual(actual_columns, expected_columns)

        actual_values = set(new_dataset['2021'].values)
        self.assertSetEqual(actual_values, expected_values)

    def test_preprocess_world_bank_data(self):
        test_df = pd.DataFrame({
            'Country Name': ['Denmark', 'Denmark', 'Denmark', 'Bulgaria', 'Bulgaria', 'Bulgaria'],
            'Country Code': ['DEN', 'DEN', 'DEN', "BUL", "BUL", "BUL"],
            'Series Name': ["jobs", "stores", "places", "jobs", "stores", "places"],
            'Series Code': ['AB1', 'AB2', 'AB3', 'AB1', 'AB2', 'AB3'],
            '2020 [YR2020]': [5, 2, np.nan, 4, np.nan, 6],
            '2021 [YR2021]': [np.nan, 8, 3, np.nan, np.nan, 2]})
        expected_columns = {'country_name', 'jobs', 'stores', 'places'}
        new_dataset = preprocess_world_bank_data(test_df)

        actual_columns = set(new_dataset.columns.values)
        self.assertSetEqual(actual_columns, expected_columns)

        self.assertEqual(new_dataset.loc[new_dataset['country_name'] == 'Denmark', 'jobs'].values, np.array([5]))
        self.assertEqual(new_dataset.loc[new_dataset['country_name'] == 'Denmark', 'stores'].values, np.array([8]))
        self.assertEqual(new_dataset.loc[new_dataset['country_name'] == 'Denmark', 'places'].values, np.array([3]))
        self.assertEqual(new_dataset.loc[new_dataset['country_name'] == 'Bulgaria', 'jobs'].values, np.array([4]))
        self.assertTrue(np.isnan(new_dataset.loc[new_dataset['country_name'] == 'Bulgaria', 'stores'].values[0]))
        self.assertEqual(new_dataset.loc[new_dataset['country_name'] == 'Bulgaria', 'places'].values, np.array([2]))

    def test_categorize_secure_internet_servers_per_million_people(self):
        actual = [categorize_secure_internet_servers_per_million_people(x) for x in [
            12, 13673, 667, 66666, 1045, 55999]]
        expected = ['low', 'upper_middle', 'lower_middle', 'high', 'middle', 'upper_middle']
        self.assertEqual(actual, expected)
