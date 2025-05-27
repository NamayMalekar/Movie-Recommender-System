# 🎬 Movie Recommendation System

This is a machine learning-powered movie recommendation system that suggests the top 10 movies similar to a user's selected title. Built using Python and a Streamlit frontend, the application allows users to quickly discover movies they might enjoy based on their preferences.

~ [Live Demo on Render](https://movie-recommender-system-1-h7uj.onrender.com)


### Features : 
Search any movie from the dataset and receive real-time recommendations

Content-based filtering using machine learning to find similar movies

Interactive UI built with Streamlit for a smooth user experience

Posters and movie titles displayed in a clean, responsive layout

Deployed on Render, accessible from any browser without local setup

### Tech Stack : 
Python – Core programming language for backend logic and data handling

Pandas & Scikit-learn – For data manipulation and building the recommendation model

Streamlit – Used for building the user-facing web application

Render – For deploying the application in the cloud

TMDB API – Used to fetch movie posters, titles, and metadata

### Data and API :
The recommendation system is built using a movie metadata dataset sourced from The Movie Database (TMDB). It relies on the TMDB API to:

Retrieve movie details

Display high-quality movie posters

Enhance the recommendations with real-world metadata

##### Note : A valid TMDB API key is required to access the movie data. The key is securely managed in the backend and is not exposed publicly.

### How it Works : 
The user selects or searches for a movie from the dropdown list

The app uses cosine similarity to identify the top 10 most similar movies from the dataset

These recommendations are displayed in two rows, each containing 5 movies, along with their posters and titles

Live Project
🎥 Try it out here:
👉 https://movie-recommender-system-1-h7uj.onrender.com
