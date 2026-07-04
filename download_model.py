# download_model.py
from sentence_transformers import SentenceTransformer

# Pre-download and cache model weights locally during the Docker image build phase
print("Pre-downloading 'all-MiniLM-L6-v2' weights...")
SentenceTransformer('all-MiniLM-L6-v2')
print("Model cached successfully!")