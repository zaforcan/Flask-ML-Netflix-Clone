# Model Test

import pandas as pd


selected_option = "Iron Man"

def load_data():
    movies = pd.read_pickle('datasets/models/movies.pkl')
    movies_data = pd.read_pickle('datasets/models/movies_data.pkl')
    similarity = pd.read_pickle('datasets/models/similarity.pkl')
    return movies, movies_data, similarity

def recommend(movie):
    movies, movies_data, similarity = load_data()            
    data = movies[['id', 'title', 'tags']]      
    movie_index = data[data['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    #to fetch movies from indeces


    
    liste = []
    for i in movies_list:
        liste.append(data.iloc[i[0]].title)
        print(data.iloc[i[0]].title)
    print(liste)

recommend(selected_option)      

