from unittest import TestCase
from preprocessing_functions import categorize_gdp_per_capita_value, rename_columns,\
    pivot_dataset, fill_nulls_keeping_one_value_column, preprocess_world_bank_data
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
            '2020 [YR2020]': [5, 2, None, 4, None, 6],
            '2021 [YR2021]': [None, 8, 3, None, None, 2]})
        expected_values = {5, 8, 3, 4, None, 2}
        expected_columns = {'country_name', 'jobs', 'stores', 'places'}
        new_dataset = preprocess_world_bank_data(test_df)

        actual_columns = set(new_dataset.columns.values)
        self.assertSetEqual(actual_columns, expected_columns)

        self.assertEqual(new_dataset.loc[0, 'jobs'], 5)