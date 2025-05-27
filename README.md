🎬 Movie Recommendation System
This is a machine learning-powered movie recommendation system that suggests the top 10 similar movies based on a user's selected title. Built using Python and a clean Streamlit interface, it lets users quickly discover movies similar to the one they love.

👉 Live Demo on Render

🔍 Features
🔎 Search any movie from the database and receive top 10 similar recommendations

🧠 Uses content-based filtering with machine learning

🎨 Sleek, interactive UI built with Streamlit

🖼️ Displays movie posters with titles in a responsive layout

☁️ Hosted on Render for easy web access

🛠️ Tech Stack
Python (core logic and data handling)

Pandas, Scikit-learn for data manipulation & ML

Streamlit for frontend user interface

Render for cloud deployment

TMDB API for fetching movie details and posters

📊 Data & API
The movie data is based on a dataset retrieved from The Movie Database (TMDB)

The application uses the TMDB API to fetch:

Movie details

Posters

Metadata used for recommendations

🔐 Note: A valid TMDB API key is required to fetch data. The key is securely handled in the backend and not exposed to users.

🚀 How it Works
User selects a movie title

The ML model computes cosine similarity based on movie metadata

The app returns 10 visually rich recommendations (with posters and names), in a 2-row layout

📎 Live Project
🎥 Check out the app here:
👉 https://movie-recommender-system-1-h7uj.onrender.com
