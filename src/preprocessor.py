import re

def clean_text(text):
     """Removes special characters, links, and normalizes text structure."""
     if not text:
          return ""

     text = text.lower()
     text = re.sub(r'http\S+\s*', '  ' , text)
     text = re.sub(r'\S+@\S+', '  ' , text)
     text = re.sub(r'[^\w\s]', '  ' , text)
     text = re.sub(r'\s+', '  ' , text).strip()
     return text
          