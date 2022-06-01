from unittest import TestCase
import pandas as pd
from clustering_functions import get_countries_ordering


class TestPreprocessingFunctions(TestCase):
    def test_get_countries_ordering(self):
        actual = get_countries_ordering(pd.DataFrame({0: [1, 1, 1], 1: [1, 2, 3], 2: [1, 2, 3]},
                                                     index=["Brazil", "Argentina", "Uruguay"]),
                                        cluster_coordinates=[3, 3, 3])
        expected = ['Uruguay', 'Argentina', 'Brazil']
        self.assertListEqual(actual, expected)