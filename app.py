'''
Author: Ashutosh devpura
Email: ashutoshdevpura@gmail.com

'''

import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters



# Set page title and favicon
st.set_page_config(page_title="CineMate", page_icon=":clapper:", layout="wide")

# Add page title and subtitle
st.title("CineMate: Your Personal Movie Recommendation Engine")
st.write("Find your next favorite movie!")

# Load data and create dropdown
movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))
movie_list = movies['title'].values
selected_movie = st.selectbox("Please select a movie from the dropdown menu or type the name of the movie", movie_list)

# Add button to show recommendations
if st.button('Get Recommendations'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    st.write('\n')
    st.write("Top 5 recommended movies similar to **{}** :".format(selected_movie))
    st.write('\n')

    # Add columns to display recommended movies and posters
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], width=150)
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], width=150)
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], width=150)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], width=150)
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], width=150)

# Add footer text
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')
st.write('\n')



st.write("Made with :heart: by Ashutosh Devpura")
