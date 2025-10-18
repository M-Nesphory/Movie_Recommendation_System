# Couch-Potato Movie Recommendation System 

## Overview  
The Couch-Potato Movie Recommendation System is a project
designed to help users discover movies they’ll love using personalized recommendations. It is built with the MovieLens 100K dataset. This system uses Collaborative Filtering (CF) technique to learn from user rating patterns and suggest the top movies they are most likely to enjoy.  

## Problem Statement

With thousands of available titles users often face:

* Decision fatigue while browsing large catalogs

* Difficulty finding movies aligned with their tastes

* Missed opportunities to discover new favorite films

This project aims to solve that by recommending movies tailored to individual preferences using machine learning.
  
  ## Technical Approach

The system leverages Collaborative Filtering to identify user similarities and predict unseen movie ratings.

### Steps:

1. Data Preprocessing

* Load and clean the MovieLens dataset

* Prepare the user–item matrix

2. Exploratory Data Analysis 

* Examine rating distributions and popular genres

* Identify trends across users and items

3. Modeling

* Implemented Matrix Factorization using SVD (Singular Value Decomposition) from the surprise library

* Trained and evaluated the model with RMSE metrics

* Generated Top 5 movie recommendations per user

4. Evaluation

* Measure prediction accuracy

  
1. Recommendation Generation

* Produced top 5 movie suggestions for given user input

* Displayed recommendations in readable format

## Dataset

Source: MovieLens 100K Dataset

Contents:

* 100,000 ratings from 943 users on 1,682 movies

* Ratings range from 1 (least preferred) to 5 (most preferred)

* Includes user and movie IDs, titles, and genres