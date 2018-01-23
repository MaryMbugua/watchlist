from flask import render_template
from app import app
from .request import get_movies

#Views
@app.route('/')
def index():
    '''
    view  root page function that returns 
    the index page and its data
    '''
        #getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home -Welcome to the Best Movie Review Website Online!'
    return render_template('index.html',title = title,popular = popular_movies)
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    view movie page function
    that returns the movie details page 
    and its data
    '''
    id = movie_id
    title = f"Hello Movie {id}"
    return render_template('movie.html',title = title)