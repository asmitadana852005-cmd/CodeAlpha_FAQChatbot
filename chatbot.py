import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class FAQChatbot:

    def __init__(self, csv_file):

        # Load FAQ dataset
        self.data = pd.read_csv(csv_file)

        # Create TF-IDF vectorizer
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english"
        )

        # Convert FAQ questions into vectors
        self.question_vectors = self.vectorizer.fit_transform(
            self.data["question"]
        )


    def get_answer(self, user_question):

        # Convert user's question into a TF-IDF vector
        user_vector = self.vectorizer.transform(
            [user_question]
        )

        # Calculate cosine similarity
        similarities = cosine_similarity(
            user_vector,
            self.question_vectors
        )

        # Find the most similar FAQ
        best_index = similarities.argmax()

        # Get similarity score
        best_score = similarities[0][best_index]

        # Minimum similarity threshold
        if best_score < 0.20:

            return (
                "Sorry, I could not find a relevant answer "
                "to your question."
            )

        # Get corresponding answer
        answer = self.data.iloc[best_index]["answer"]

        return answer