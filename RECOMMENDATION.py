from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

movies = {
    0: "The Matrix",
    1: "The Lord of the Rings",
    2: "Harry Potter",
    3: "The Dark Knight",
    4: "Inception"
}

features = [
    "sci-fi action",
    "fantasy adventure",
    "fantasy magic",
    "action superhero",
    "sci-fi thriller"
]

ratings_data = {
    "The Matrix": [5, 4, 0, 0],
    "The Lord of the Rings": [4, 5, 0, 0],
    "Harry Potter": [0, 4, 5, 0],
    "The Dark Knight": [0, 0, 4, 5],
    "Inception": [0, 0, 5, 4]
}
users = ["User1", "User2", "User3", "User4"]
ratings = pd.DataFrame(ratings_data, index=users)

vectorizer = CountVectorizer()
feature_vectors = vectorizer.fit_transform(features)
content_similarity = cosine_similarity(feature_vectors)

def recommend_content_flexible():
    movie_title = input("Enter a movie title: ")
    movie_index = None
    for idx, title in movies.items():
        if title.lower() == movie_title.lower():
            movie_index = idx
            break
    if movie_index is not None:
        scores = list(enumerate(content_similarity[movie_index]))
        scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:]
        print(f"\nBecause you liked '{movie_title}', you may also like:")
        for i, _ in scores[:3]:
            print(f"- {movies[i]}")
    else:
        genre_input = input("Movie not found. Enter the genre (e.g., sci-fi, fantasy): ")
        genre_vec = vectorizer.transform([genre_input])
        scores = cosine_similarity(genre_vec, feature_vectors)[0]
        ranked_idx = scores.argsort()[::-1][:3]
        print(f"\nBased on genre '{genre_input}', you may like:")
        for i in ranked_idx:
            print(f"- {movies[i]}")

user_similarity = cosine_similarity(ratings)
user_similarity_df = pd.DataFrame(user_similarity, index=users, columns=users)

def recommend_collaborative():
    print("Available users:", ", ".join(users))
    user = input("Enter a user (e.g., User1): ")
    if user not in users:
        print("User not found!")
        return
    print(f"\nRecommendations for {user}:")
    similar_users = user_similarity_df[user].sort_values(ascending=False).index[1:]
    recommended = set()
    for sim_user in similar_users:
        for movie in ratings.columns:
            if ratings.loc[user, movie] == 0 and ratings.loc[sim_user, movie] >= 4:
                recommended.add(movie)
    if recommended:
        for r in recommended:
            print(f"- {r}")
    else:
        print("No new recommendations found.")

def main():
    print("🎬 Simple Recommendation System")
    print("1. Content-Based Filtering (by movie or genre)")
    print("2. Collaborative Filtering (by user)")
    choice = input("Choose option (1/2): ")
    if choice == "1":
        recommend_content_flexible()
    elif choice == "2":
        recommend_collaborative()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
