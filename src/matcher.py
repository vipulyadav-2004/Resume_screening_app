from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

try:
    from sentence_transformers import SentenceTransformer, util
except ImportError:
    SentenceTransformer = None
    util = None

class AdvancedSemanticMatcher:
    def __init__(self):
        self.model = None
        if SentenceTransformer is not None:
            try:
                print("📥 Initializing Pre-trained Sentence-Transformer (all-MiniLM-L6-v2)...")
                self.model = SentenceTransformer('all-MiniLM-L6-v2')
            except Exception as exc:
                print(f"⚠️ Falling back to TF-IDF scoring because the transformer model could not be loaded: {exc}")
                self.model = None

    def calculate_match_score(self , resume_text , job_description_text):
        """
        Computes the deep semantic contextual match score between text profiles
        using vector cosine similarity over neural network embeddings.
        """
        if self.model is None or util is None:
            vectorizer = TfidfVectorizer(stop_words='english')
            corpus = [resume_text, job_description_text]
            tfidf_matrix = vectorizer.fit_transform(corpus)
            similarity_matrix = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
            return round(similarity_matrix[0][0] * 100, 2)

        resume_embedding = self.model.encode(resume_text , convert_to_tensor=True)
        job_desc_embedding = self.model.encode(job_description_text , convert_to_tensor = True)

        cosine_score = util.cos_sim(resume_embedding , job_desc_embedding)

        match_percentage = float(cosine_score[0][0])*100

        return round(max(0.0 , min(100.0 , match_percentage)),2)

matcher_engine = AdvancedSemanticMatcher()
match_engine = matcher_engine
