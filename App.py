import pandas as pd
import streamlit as st
import pickle
import requests

# Load the movie data and similarity matrix
movies_dict  = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Function to fetch poster image URL from TMDB API
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=fc0b97564ceada34e42bc827cd026ee7&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()

    # Check if poster_path is in the response
    poster_path = data.get('poster_path', None)
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
        return full_path
    else:
        # Return a placeholder image if poster_path is missing
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

# Function to recommend similar movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id  # Assuming movie_id is available
        recommended_movies.append(movies.iloc[i[0]].title)
        # Fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters



# Load the similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app UI (Title)
st.markdown("<h1 style='text-align: center;'>  Movie Recommender System</h1>", unsafe_allow_html=True)


#movie_list = movies['title'].values
#selected_movie = st.selectbox('Find the Movie',movie_list)

movie_list = movies['title'].values

# Center-align the selectbox and button using columns
col1, col2, col3 = st.columns([1, 4, 1])  # middle column is wider
with col2:
    selected_movie = st.selectbox('🔍 Search the Movie', movie_list)

# Center the Recommend button separately
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 1])
with col_btn2:
    recommend_clicked = st.button(' Recommend')


# Show recommendations fullscreen
if recommend_clicked:
    # Centered spinner
    with st.spinner("🔄 Fetching recommendations..."):
        try:
            names, posters = recommend(selected_movie)

            # Heading centered
            st.markdown(
                "<h3 style='text-align: center;'>Recommended Movies</h3>",
                unsafe_allow_html=True
            )

            # First row: first 5 recommendations
            row1 = st.columns(5)
            for i in range(5):
                with row1[i]:
                    st.image(posters[i], use_container_width=True)
                    st.markdown(f"<p style='text-align: center;'>{names[i]}</p>", unsafe_allow_html=True)

            # Second row: next 5 recommendations
            row2 = st.columns(5)
            for i in range(5, 10):
                with row2[i - 5]:
                    st.image(posters[i], use_container_width=True)
                    st.markdown(f"<p style='text-align: center;'>{names[i]}</p>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
