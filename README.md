# Resume Screening App

A lightweight AI-powered resume screening project that compares uploaded resumes against a job description and returns a ranked match score for each file.

## What it does

- Accepts a job description and multiple resume uploads.
- Cleans and normalizes text before scoring.
- Uses a semantic matching model based on `sentence-transformers` when available.
- Falls back to TF-IDF cosine similarity if the neural model cannot be loaded.
- Displays ranked results in a simple web interface.

## Project Structure

- `app.py` - Flask web app for the UI.
- `src/main.py` - FastAPI service for API-based screening.
- `src/preprocessor.py` - Text cleaning utilities.
- `src/matcher.py` - Match scoring logic.
- `templates/index.html` - Front-end form and results table.
- `download_model.py` - Pre-downloads the embedding model for offline/container use.
- `Data/` - Sample job descriptions and resume files for testing.

## Requirements

This project uses Python and the following packages:

- `flask`
- `fastapi`
- `uvicorn`
- `sentence-transformers`
- `scikit-learn`
- `python-multipart`

## Setup

1. Create and activate a virtual environment.
2. Install the dependencies listed above.
3. If you want the semantic model cached locally, run `python download_model.py` once.

## Run the Flask UI

```bash
python app.py
```

Then open the local server shown in the terminal and upload resumes as plain text files for testing.

## Run the FastAPI Service

```bash
uvicorn src.main:app --reload
```

The API exposes `POST /api/v1/screen` with form fields for `job_description` and `resumes`.

## Notes

- The current matching logic is optimized for text-based resume files.
- Sample files under `Data/` can be used to test the workflow quickly.
- If the transformer model is unavailable, the app still works with TF-IDF scoring.
