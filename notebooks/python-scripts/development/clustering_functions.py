import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_features_for_group(group_indexes, all_data, data_statistics):
    """
    Function which plots data for every feature within a group. Additional to that it plots the quantiles.
    This way it can be visually compared to group statistics.
    :param group_indexes: all the indexes representing the group to plot statistics for
    :param all_data: the initial dataset containing all countries
    :param data_statistics: data about the initial dataset for each feature, such as quantiles and mean
    """
    group_data = all_data.loc[group_indexes, :]
    fig, axes = plt.subplots(ncols=4, nrows=5, figsize=(20, 16))

    for i in range(len(group_data.columns)):
        ax = sns.histplot(ax=axes[i // 4, i % 4], x=group_data[group_data.columns.values[i]])
        y_axis = ax.get_yticks()
        ax.plot([data_statistics.loc['mean', group_data.columns[i]]] * len(y_axis), y_axis, 'r', linestyle='dashed')
        ax.plot(
            [data_statistics.loc['25%', group_data.columns[i]]] * len(y_axis), y_axis, 'darkgreen', linestyle='dashed')
        ax.plot(
            [data_statistics.loc['50%', group_data.columns[i]]] * len(y_axis), y_axis, 'darkgreen', linestyle='dashed')
        ax.plot(
            [data_statistics.loc['75%', group_data.columns[i]]] * len(y_axis), y_axis, 'darkgreen', linestyle='dashed')


def get_countries_ordering(countries_in_cluster_coordinates, cluster_coordinates):
    """
    Function that computes ordering of the countries based on cluster representation. Points closer to the cluster
    center are more representative of that cluster.
    :param countries_in_cluster_coordinates: coordinates of the countries in this cluster
    :param cluster_coordinates: coordinates of the cluster
    :return: ordered list of countries, descending in terms of how well they represent the cluster
    """
    working_df = countries_in_cluster_coordinates.copy()
    for index, row in working_df.iterrows():
        euclidean_distance = np.linalg.norm(np.array(row.values) - np.array(cluster_coordinates))
        working_df.loc[index, 'dist_to_cluster'] = euclidean_distance

    # Lower distance to cluster should be first as they are more representative
    return list(working_df.sort_values(by='dist_to_cluster').index.values)
