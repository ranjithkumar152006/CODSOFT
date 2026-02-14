import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Movie dataset
data = {
    "movie": [
        "Avengers", "Iron Man", "Batman", "Superman",
        "Titanic", "The Notebook", "Inception", "Interstellar"
    ],
    "genre": [
        "action superhero",
        "action superhero",
        "action superhero",
        "action superhero",
        "romance drama",
        "romance drama",
        "sci-fi thriller",
        "sci-fi space"
    ]
}

df = pd.DataFrame(data)

# Convert genres to vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df["genre"])

# Compute cosine similarity
similarity = cosine_similarity(genre_matrix)

# Display available movies
print("Available Movies:")
for movie in df["movie"]:
    print("-", movie)

# Case-insensitive user input
user_input = input("\nEnter a movie name: ").strip().lower()

# Create lowercase mapping
movie_map = {movie.lower(): idx for idx, movie in enumerate(df["movie"])}

def recommend(movie_input):
    if movie_input not in movie_map:
        print("\n❌ Movie not found!")
        return

    movie_index = movie_map[movie_input]

    similarity_scores = list(enumerate(similarity[movie_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print(f"\n🎬 Top 3 movies similar to '{df.iloc[movie_index].movie}':\n")

    count = 0
    for idx, score in similarity_scores:
        if idx != movie_index:
            print("✔", df.iloc[idx].movie)
            count += 1
        if count == 3:
            break

recommend(user_input)
