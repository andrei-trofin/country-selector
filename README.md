<h1 style="text-align: center"> 🌍 Country Selector </h1>

## Business Case

This project aims to answer an interesting question: what countries would fit me
the most if I wanted to change states? I believe that a lot of people have the
opportunity to work remotely now and can decide to travel or even settle in a
new country. Using general data about countries, one can gain a little bit of
insight about what group of countries would suit her/his needs.

Using clustering we can split all the countries into groups and then draw
different conclusions about those groups. The aim was to find all
characteristics that differentiate these groups and use them for the little
country selector recommendation system.

## Table of Contents
<details open>
<summary>Show/Hide</summary>

1. [File/Folder descriptions](#1-filefolder-descriptions)
2. [Data preparation](#2-data-preparation)
3. [Exploratory Data Analysis](#3-exploratory-data-analysis)
    * [3.1 What we search for](#31-what-we-search-for)
    * [3.2 Extracting the statistics](#32-extracting-the-statistics)
4. [Modeling](#4-conclusion)
    * [4.1 What did I learn?](#41-what-did-i-learn)
    * [4.2 Future improvements](#42-future-improvements)
5. [Cluster EDA](#5-cluster-eda)
6. [Web application](#6-web-application)
7. [Conclusion](#7-conclusion)
</details>

## 1. File/Folder descriptions

<details open>
<summary>Show/Hide</summary>

* **data**: folder in which all data is stored
    * Economy.xlsx: excel formatted data about economy of countries from https://data.worldbank.org/
    * education.xlsx: excel formatted data about education of countries from https://data.worldbank.org/
    * employment.xlsx: excel formatted data about employment of countries from https://data.worldbank.org/
    * financial-indicators.xlsx: excel formatted data about financial indicators of countries from
  https://data.worldbank.org/
    * health.xlsx: excel formatted data about health of countries from https://data.worldbank.org/
    * infrastructure.xlsx: excel formatted data about infrastructure of countries from https://data.worldbank.org/
    * mean-temperature.nc: netcdf formatted data about temperatures of countries from 
  https://climateknowledgeportal.worldbank.org/download-data
    * population-and-environment.xlsx: excel formatted data about population and environment of countries from 
  https://data.worldbank.org/
    * poverty.xlsx: excel formatted data about poverty of countries from https://data.worldbank.org/
    * precipitation.nc: excel formatted data about rain statistics of countries from 
  https://climateknowledgeportal.worldbank.org/download-data
    * private-sector.xlsx: excel formatted data about the private sector of countries from https://data.worldbank.org/
    * public-sector.xlsx: excel formatted data about the public sector of countries from https://data.worldbank.org/
    * world-happiness-2022.csv: the world happiness report from 2022
    * crime-rates.json: json formatted data about crime index of countries from https://worldpopulationreview.com/
    * cleaned_data.csv: csv formatted data about countries resulted from preprocessing; this data is used for the
  application
* **models**: folder in which models or scalers are stored
* **notebooks**: where the jupyter notebooks and adjacent python scripts are stored
  * **1. Data Preprocessing.ipynb**: notebook used for preprocessing all data about countries
  * **python-scripts**: folder which contains python scripts used in notebooks and tests for functions where possible
    * **development**: folder in which all python scripts reside
      * **preprocessing_functions.py**: script containing functions used in notebooks
      * **preprocessing_variables.py**: script containing variables used in notebooks
    * **test**: folder containing test modules
      * **test_preprocessing_functions.py**: unit test module for functions in preprocessing_functions.py
* **research.txt**: text file I used to quickly find the most important factors for choosing a country where to move to
* **images**: folder holding images used in the presentation file

</details>


## 2. Data preparation

<details open>
<summary>Show/Hide</summary>

The work here was done in the [data processing notebook.](./notebooks/1.Data%20Preprocessing.ipynb)

I have downloaded data from different sites. I based my logic on research I have done in the 
[research file](research.txt). I wanted to see what are the main factors that people look for when
moving to a different country. After I have made a list, I went on and searched for data.
Because I did not manage to find one single place in which to download all data, I did not spend additional time
to learn the API of any particular site, but rather downloaded the raw data myself.

<p align="center">
  <img src="images/world-happiness.png" width="300"/>
</p>
<br>
<br>

I have put all the data in the [data folder](./data/) and went through it all and tried to make one clean dataset.
Some of the data such as precipitation, temperature, education, employment, poverty, private and public sector 
did not make it into the final set due to the lack of values for the majority of the countries.

Therefore, the [final dataset](./data/cleaned_data.csv) contains data about 117 countries. This data refers to: 
happiness, economy, crime rate, infrastructure, finance, health, population and environment. A total of 22 columns were 
extracted, making this dataset a 117 x 22 dataframe. This is the dataset used to create clusters upon which the 
application is built.

</details>


## 3. Exploratory data analysis

<details open>
<summary>Show/Hide</summary>

</details>


### 3.1 What we search for

<details open>
<summary>Show/Hide</summary>


</details>


### 3.2 Extracting the statistics

<details open>
<summary>Show/Hide</summary>



</details>


## 4. Conclusion

<details open>
<summary>Show/Hide</summary>

</details>

### 4.1 What did I learn?

<details open>
<summary>Show/Hide</summary>


</details>


### 4.2 Future improvements

<details open>
<summary>Show/Hide</summary>


</details>
