#Day 75: Recommendation system


#Build a recommendation system.


#Content-Based Filtering (Using TF-IDF & Cosine Similarity)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {'title': ["The Great Gatsby", "To Kill a Mockingbird", "1984", "Pride and Prejudice", "Moby Dick"],
        'description': ["A story of wealth and tragedy in the 1920s.",
                        "A young girl grows up facing racial injustice.",
                        "A dystopian future with surveillance and control.",
                        "A romantic novel about love and society.",
                        "A sea captain's obsessive quest for revenge."]}

df = pd.DataFrame(data)

# Convert descriptions to TF-IDF features
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['description'])

# Compute similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Recommendation function
def recommend(title, df, cosine_sim):
    idx = df.index[df['title'] == title][0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]  # Top 3 recommendations
    book_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[book_indices]

# Example usage
print(recommend("The Great Gatsby", df, cosine_sim))
