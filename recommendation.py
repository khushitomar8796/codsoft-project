import numpy as np

# Example movie dataset (movies and their genres)
movies = {
    'Movie1': ['Action', 'Sci-Fi'],
    'Movie2': ['Drama'],
    'Movie3': ['Comedy'],
    'Movie4': ['Action', 'Adventure'],
    'Movie5': ['Action', 'Adventure'],
    'Movie6': ['Drama', 'Romance']
}

# Example user preferences (preferred genres)
user_preferences = ['Action', 'Adventure']

# Function to calculate similarity between user preferences and movies
def calculate_similarity(user_preferences, movie_genres):
    user_preferences_set = set(user_preferences)
    movie_genres_set = set(movie_genres)
    similarity_score = len(user_preferences_set.intersection(movie_genres_set)) / float(len(user_preferences_set.union(movie_genres_set)))
    return similarity_score

# Function to recommend movies based on user preferences
def recommend_movies(user_preferences, movies):
    recommendations = []
    for movie, genres in movies.items():
        similarity_score = calculate_similarity(user_preferences, genres)
        recommendations.append((movie, similarity_score))
    
    # Sort recommendations by similarity score in descending order
    recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)
    return recommendations

# Get movie recommendations
recommendations = recommend_movies(user_preferences, movies)

# Print recommendations
print("Movie Recommendations:")
for movie, score in recommendations:
    print(f"{movie}: {score:.2f}")