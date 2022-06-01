import streamlit as st
import json
from app_variables import magnitude_dictionary, nat_areas_dictionary, development_dictionary, safety_dictionary
import numpy as np


def load_data():
    groups = json.load(open("../data/groups.json", 'r'))
    group_scores = json.load(open("../data/group_scores.json", 'r'))
    indices = json.load(open("../data/indices.json"))

    return groups, group_scores, indices


def get_group(lc_value, na_value, cs_value, pg_value, s_value, td_value, group_scores):
    """
    Function which outputs the group having indices values closest to indices values provided by the user.
    If more groups have the same euclidean distance in terms of indices scores between group score and user score,
    the first group that has this minimum value will be returned.
    :param group_scores: scores from each group on the given indices
    :param lc_value: living cost value, int
    :param na_value: natural areas value, int
    :param cs_value: country size value, int
    :param pg_value: generosity value, int
    :param s_value: safety value, int
    :param td_value: technology development, int
    :return: string value representing the group these values are closest to
    """

    # The order is very important since we are going to compute distances between points in space
    current_values_vector = [lc_value, na_value, cs_value, pg_value, s_value, td_value]

    min_val = np.infty
    min_index = None

    # Check what group has the scores closest to what the user has inputted
    for key in group_scores.keys():
        curr_val = np.linalg.norm(np.array(group_scores.get(key)) - np.array(current_values_vector))
        if curr_val < min_val:
            min_val = curr_val
            min_index = key

    return min_index


def show_main_page(groups, group_scores, indices):
    st.markdown("<h1 style='text-align: center; color: green'>Country selector</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: green'>🗺️</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center'>See what countries fit your needs best!</h3>", unsafe_allow_html=True)
    st.text(" ")
    st.text(" ")
    st.text(" ")
    st.text(" ")

    living_costs_value = st.select_slider("Living costs", options=["Smaller", "Normal", "Higher"], value="Normal")
    st.text(" ")
    natural_areas_value = st.select_slider("Natural areas",
                                           options=["Fewer than normal", "Normal", "More than normal"],
                                           value="Normal")
    st.text(" ")
    country_size_value = st.select_slider("Country size", options=["Smaller", "Normal", "Higher"], value="Normal")
    st.text(" ")
    people_generosity_value = st.slider("People generosity", min_value=1, max_value=3, value=2)
    st.text(" ")
    safety_value = st.select_slider("Safety",
                                    options=["Not very safe", "Generally safe", "Very safe"],
                                    value="Generally safe")
    st.text(" ")
    development_value = st.select_slider("Technological development",
                                         options=["Not so advanced", "Normal", "Advanced"],
                                         value="Normal")

    is_clicked = st.button(label="Show me the countries 🔍")

    if is_clicked:
        lc_value = magnitude_dictionary.get(living_costs_value)
        cs_value = magnitude_dictionary.get(country_size_value)
        na_value = nat_areas_dictionary.get(natural_areas_value)
        s_value = safety_dictionary.get(safety_value)
        td_value = development_dictionary.get(development_value)

        countries = groups.get(get_group(
            lc_value, na_value, cs_value, people_generosity_value, s_value, td_value, group_scores))
        st.table(countries)
