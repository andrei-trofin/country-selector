import re


def categorize_gdp_per_capita_value(gdp_value):
    """Gets GDP per capita value and outputs the group it is in based on values on this website:
    https://blogs.worldbank.org/opendata/new-world-bank-country-classifications-income-level-2021-2022

        Parameters
        ----------
        gdp_value : float
            A number representing a GDP per capita value

        Returns
        -------
        string
            one of the strings in {'low', 'lower_middle', 'upper_middle', 'high'} representing
            the group this GDP per capita value is a part of
        """
    group = 'high'
    if gdp_value < 1046:
        group = 'low'
    elif gdp_value < 4096:
        group = 'lower_middle'
    elif gdp_value < 12696:
        group = 'upper_middle'

    return group


def rename_columns(dataset):
    """Rename world bank dataset columns. Replace useless info from brackets. Replace spaces with underscores.
    Lowercase all letters.
        Parameters
        ----------
        dataset : pd.DataFrame
            The dataframe that we will be preprocessing

        Returns
        -------
        pd.DataFrame
            the preprocessed dataframe
        """
    dataset = dataset.rename(columns=lambda c: c.replace(" ", "_").lower())
    dataset = dataset.rename(columns=lambda c: re.sub(r'_\[.*\]', '', c))

    return dataset


def fill_nulls_keeping_one_value_column(dataset):
    """Fill null values from 2021 column with values from 2020 column if present.
    Drop column 2020 after this process
        Parameters
        ----------
        dataset : pd.DataFrame
            The dataframe that we will be preprocessing

        Returns
        -------
        pd.DataFrame
            the preprocessed dataframe
        """
    # Fill null values of 2021 column with values of 2020 if existent
    dataset['2021'] = dataset.loc[:, '2021'].fillna(dataset.loc[:, '2020'])

    # Drop 2020 column
    dataset = dataset.drop(columns='2020')

    return dataset


def pivot_dataset(dataset):
    """Use values in the column series_name as columns with the help of table pivoting.
        Parameters
        ----------
        dataset : pd.DataFrame
            The dataframe that we will be preprocessing

        Returns
        -------
        pd.DataFrame
            the preprocessed dataframe
        """
    return dataset.pivot_table(values='2021', index="country_name", columns=['series_name']).reset_index()


def preprocess_world_bank_data(dataset):
    """Preprocesses all data sets from world bank. These are similar data sets and can be (up until one point)
    be preprocessed the same way.
        Parameters
        ----------
        dataset : pd.DataFrame
            The dataframe that we will be preprocessing

        Returns
        -------
        pd.DataFrame
            the preprocessed dataframe
        """
    # Rename columns
    dataset = rename_columns(dataset)
    # Drop irrelevant columns
    dataset = dataset.drop(columns=["country_code", "series_code"])
    # Fill NAs of 2021 with values of 2020 if possible
    dataset = fill_nulls_keeping_one_value_column(dataset)
    # Pivot table
    dataset = pivot_dataset(dataset)

    return dataset


def categorize_secure_internet_servers_per_million_people(number_of_servers_per_one_million_people):
    """Gets the number of secure internet servers per 1 million people and outputs a group.
    I have come up with these groups so there is no statistical foundation for them.

        Parameters
        ----------
        number_of_servers_per_one_million_people : float
            A number representing secure internet servers per 1 million people

        Returns
        -------
        string
            one of the strings in {'low', 'lower_middle', 'middle', 'upper_middle', 'high'} representing
            the group this number of server is part of
        """
    group = 'high'
    if number_of_servers_per_one_million_people < 250:
        group = 'low'
    elif number_of_servers_per_one_million_people < 1000:
        group = 'lower_middle'
    elif number_of_servers_per_one_million_people < 10000:
        group = 'middle'
    elif number_of_servers_per_one_million_people < 60000:
        group = 'upper_middle'

    return group


def inverse_feature_values(feature_series, scaler_type):
    """
    Function used to transform feature values so that the lowest value will be converted to highest and vice versa.
    This is done so that all features have the same meaning: lower values = bad; higher values = good
    :param scaler_type: type of scaler used for scaling data: min_max or standard
    :param feature_series: the original values of the feature for each entry
    :return: modified feature values for each entry
    """
    if scaler_type == "min_max":
        return 1.0 - feature_series
    else:
        return - feature_series
