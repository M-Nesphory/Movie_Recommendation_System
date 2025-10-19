#  Couch-Potato Movie Recommendation System

## Overview

This project helps users discover movies they'll love through **personalized recommendations**.  
The primary objective is to suggest the **top 5 movies** that best match each user’s viewing preferences and past rating behavior.

---

## Problem Statement

With thousands of movies to choose from users often experience:

* **Decision fatigue** when navigating vast catalogs  
* **Difficulty discovering** films that match their personal tastes  
* **Missed chances** to uncover new favorites

This project addresses these challenges by leveraging **machine learning** to deliver personalized movie recommendations tailored to each user’s preferences.

---

## Technical Approach

The system utilizes **Collaborative Filtering** to identify relationships between users and predict ratings for movies they haven’t yet watched.

---

## Dataset

The dataset used in this project is sourced from the [MovieLens Dataset](https://grouplens.org/datasets/movielens/latest/), a collection of user movie ratings and metadata.

---

## Tools Used

- **Python:** Pandas, Scikit-learn, NumPy, Matplotlib, Seaborn, SciPy, Scikit-surprise  
- **Model Deployment:** Streamlit  
- **IDE / Notebook:** Jupyter Notebook, Visual Studio Code

---

## Recommendations

* Revive **Film-Noir** classics to help new audiences appreciate the evolution of cinema.  
* Focus on **non-fictional** films, which tend to receive higher ratings in the dataset.  
* Offer a **wide variety of genres** as ratings show minimal deviation across genre types.  
* Emphasize **post-1982 releases** to appeal to modern audiences, while still including older classics.  
* Incorporate **recently updated datasets** to include new and upcoming movie releases.

---

## Getting Started

To replicate this Movie Recommendation System locally, follow these steps:

---

### 1. Clone the repository

```bash
git clone git@github.com:M-Nesphory/Movie_Recommendation_System.git
cd Movie_Recommendation_System
```

---

### 2. Set up your Conda Environment  

Make sure Anaconda is installed then create and activate a new environment 

conda create --name movie-recommender python=3.10
conda activate movie-recommender

---

### 3. Install Required Packages  

pip install pandas numpy scikit-learn matplotlib seaborn scipy streamlit scikit-surprise

---

### 4. Load the Dataset  
 
 Download the MovieLens Dataset(https://grouplens.org/datasets/movielens/latest/)  

Once downloaded, extract the files and place them inside a data directory within your project folder.

---

### 5. Launch the Streamlit App 

Once your model and dataset are ready run the interactive web app to generate personalized recommendations.

Ensure that:

Your trained model file (final_svd_model.pkl) is in the project directory.

The processed dataset (final_df.csv) is available for the app.

Start the Streamlit server by running: 

streamlit run recommender_system_app.py

Access it in your browser at: http://localhost:8501/