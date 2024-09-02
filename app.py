from flask import Flask, jsonify, render_template, Response
import csv
import os
from feedgen.feed import FeedGenerator

app = Flask(__name__)

IMDB_EXPORT_FOLDER = 'imdb_exports'

@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template

@app.route('/get-list', methods=['GET'])
def get_list():
    movies = []
    for filename in os.listdir(IMDB_EXPORT_FOLDER):
        if filename.endswith('.csv'):
            filepath = os.path.join(IMDB_EXPORT_FOLDER, filename)
            movies.extend(parse_csv(filepath))
    
    return jsonify(movies)

@app.route('/rss-feed', methods=['GET'])
def rss_feed():
    fg = FeedGenerator()
    fg.title('My IMDb Movie List')
    fg.link(href='http://localhost:5000/rss-feed')
    fg.description('A list of movies from IMDb exports')
    
    movies = []
    for filename in os.listdir(IMDB_EXPORT_FOLDER):
        if filename.endswith('.csv'):
            filepath = os.path.join(IMDB_EXPORT_FOLDER, filename)
            movies.extend(parse_csv(filepath))
    
    for movie in movies:
        fe = fg.add_entry()
        fe.title(f"{movie['title']} ({movie['year']})")
        fe.link(href=movie['url'])
        fe.description(f"IMDb Rating: {movie['imdb_rating']}, Genres: {movie['genres']}")
    
    rssfeed = fg.rss_str(pretty=True)
    return Response(rssfeed, mimetype='application/rss+xml')

def parse_csv(filepath):
    movies = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movie = {
                'title': row.get('Title'),
                'year': row.get('Year'),
                'imdb_id': row.get('Const'),
                'imdb_rating': row.get('IMDb Rating'),
                'url': row.get('URL'),
                'genres': row.get('Genres')
            }
            movies.append(movie)
    return movies

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
