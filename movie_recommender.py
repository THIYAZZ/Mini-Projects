import pandas as pd

# Movie dataset
movies = {
    'Movie': ['Inception', 'Titanic', 'Avengers', 'Interstellar', 'Joker'],
    'Genre': ['Sci-Fi', 'Romance', 'Action', 'Sci-Fi', 'Drama']
}

df = pd.DataFrame(movies)

# User input
user_genre = input("Enter your preferred genre: ")

# Recommendation logic
recommended_movies = df[df['Genre'].str.contains(user_genre, case=False)]

if not recommended_movies.empty:
    print("\nRecommended Movies:")
    for movie in recommended_movies['Movie']:
        print("-", movie)
else:
    print("\nNo movies found for this genre.")
