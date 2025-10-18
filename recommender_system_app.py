# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st
import random
import pickle

final_df = pd.read_csv("Data/final_df.csv")
final_model = pickle.load(open("Model/final_svd_model.pkl", "rb"))


def get_svd_recommendations_from_input(input_movie_title, user_id, n=5):
    
    # Find movie by partial, case-insensitive title 
    movie_matches = final_df[final_df['title'].str.lower().str.contains(input_movie_title.strip().lower(), na=False)]

    # Handle no match
    if movie_matches.empty:
        print(f"No movies found matching '{input_movie_title}'.")
        return pd.DataFrame(columns=['Recommended Movie', 'Genre', 'Predicted Rating'])
    
    # Select first matched movie
    input_movie_row = movie_matches.iloc[0]
    input_movie_id = input_movie_row['movieId']
    input_genres = input_movie_row['genres']

    # Find similar movies by genre 
    similar_movies = final_df[final_df['genres'] == input_genres][['movieId', 'title', 'genres']].drop_duplicates()

    # if few or no genre matches, recommend from all movies
    if similar_movies.empty or len(similar_movies) < n:
        similar_movies = final_df[['movieId', 'title', 'genres']].drop_duplicates()

    # Exclude the selected movie
    candidate_movies = similar_movies[similar_movies['movieId'] != input_movie_id]

    # Predict ratings for candidate movies
    predictions = []
    for mid in candidate_movies['movieId'].values:
        pred = final_model.predict(user_id, mid)
        predictions.append((mid, pred.est))

    # Sort by predicted rating
    top_predictions = sorted(predictions, key=lambda x: x[1], reverse=True)[:n]

    # Map movie IDs back to titles
    recommended_movies = []
    for mid, rating in top_predictions:
        movie_row = final_df.loc[final_df['movieId'] == mid]
        if movie_row.empty:
            continue  # skip missing IDs
        title = movie_row['title'].iloc[0]
        genres = movie_row['genres'].iloc[0]
        recommended_movies.append((title, genres, round(rating, 2)))

    # Handle empty case 
    if not recommended_movies:
        print("No recommendations available for this input.")
        return pd.DataFrame(columns=['Recommended Movie', 'Genre', 'Predicted Rating'])

    # Return results as DataFrame
    return pd.DataFrame(recommended_movies, columns=['Recommended Movie', 'Genre', 'Predicted Rating'])

def main():
    # Title
    st.title("Couch-Potato Recommender System")
    
    # Getting the input
    input = st.text_input("Enter a movie you liked")
    
    # Getting recommendations
    recommendations = ""
    
    # Creating a button
    if st.button("Get recommendations"):
        recommendations = get_svd_recommendations_from_input(input, user_id = int(random.choice(final_df['userId'].unique())), n=5)
        
        # Display results
        if not recommendations.empty:
            st.subheader("🎥 Recommended Movies")
            st.dataframe(recommendations)
        else:
                st.warning("No recommendations found for that movie.")
    
    
if __name__ == '__main__':
    main()
