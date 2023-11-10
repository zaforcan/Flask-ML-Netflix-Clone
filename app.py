# A Netflix-like Web App for basic movie recommendation

from flask import Flask
from flask import render_template, request
import pandas as pd

app = Flask(__name__)

selected_option = None

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        selected_option = request.form['dropdown']
        try:
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
                recommended_movies = [data.iloc[i[0]].title for i in movies_list]

                return recommended_movies

            recommended_movies = recommend(selected_option)

            return render_template("index.html", recommended_movies=recommended_movies)
        
        except:
            return render_template("index.html") 
        
    else: 
        return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)


