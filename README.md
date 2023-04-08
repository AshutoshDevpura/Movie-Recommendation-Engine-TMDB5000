# Movie-Recommendation-Engine-TMDB5000
In this project, I built a movie recommendation system using content-based filtering and various libraries such as Pandas, Numpy, Scikit-learn, and NLTK. The goal of the system is to provide users with movie recommendations based on their input.


## Data
The dataset used in this code is the TMDB 5000 Movie Dataset, which contains information on over 5,000 movies.

I used two datasets in this project, tmdb_5000_movies.csv and tmdb_5000_credits.csv, which contain information about movies such as their titles, genres, cast, crew, and plot summaries.

## Files


- artifacts/movie_list.pkl - Pickled Pandas dataframe containing movie metadata and tags
- artifacts/similarity.pkl - Pickled numpy array containing cosine similarity matrix
- data/tmdb_5000_movies.csv - Contains movie metadata
- data/tmdb_5000_credits.csv - Contains movie credits data
- src/utils/__ init __.py
- src/__ init __.py
- Data Analysis.ipynb
- README.md
- app.py
- requirements.txt
- setup.py
## Technologies Used

- Python 3
- Pandas
- scikit-learn
- NumPy
## Algorithms and Techniques

- Content-based filtering
- CountVectorizer
- Cosine similarity

##  Data Collection and Preprocessing

Before building the recommendation system, I had to preprocess the data to extract relevant features and convert them into a suitable format. This involved:

- Merging the two datasets based on movie titles.
- Removing unnecessary columns and handling missing values.
- Converting string representations of genres, cast, crew, and keywords into lists.
- Preprocessing the plot summaries by removing stop words, stemming, and converting to lowercase.



## Feature Extraction and Recommendation

To build the recommendation system, I used the following steps:

- Created a new dataframe containing movie titles and their corresponding preprocessed plot summaries, genres, cast, and crew.
- Used CountVectorizer to convert the preprocessed summaries into a matrix of token counts.
- Used cosine similarity to calculate the similarity between movies based on their token counts.
- Built a function that takes a movie title as input and returns the top 5 similar movies based on their cosine similarity scores.


## Run Locally

Clone the project

```bash
  git clone https://github.com/AshutoshDevpura/Movie-Recommendation-Engine-TMDB5000.git
```

Go to the project directory

```bash
  cd Movie-Recommendation-Engine-TMDB5000
```

Install dependencies

```bash
   pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```


## Deployment
I saved the preprocessed dataframe and similarity matrix as pickle files and deployed the system using Streamlit.
## Conclusion

Overall, this project demonstrated how to build a movie recommendation system using Python and various libraries. By preprocessing the data and using cosine similarity, I was able to create a system that provides movie recommendations based on user input.
