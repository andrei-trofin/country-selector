import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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


