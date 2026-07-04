from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from src.preprocessor import clean_text
from src.matcher import matcher_engine

app = FastAPI(title="AI Resume Screening Microservice")

@app.post("/api/v1/screen")
async def screen_resumes(
    job_description: str = Form(...), 
    resumes: List[UploadFile] = File(...)
):
    cleaned_jd = clean_text(job_description)
    results = []
    
    for file in resumes:
        contents = await file.read()
        # Decode the file stream buffer safely
        raw_text = contents.decode('utf-8', errors='ignore')
        cleaned_resume = clean_text(raw_text)
        
        # Calculate semantic cosine score using sentence-transformer embeddings
        score = matcher_engine.calculate_match_score(cleaned_resume, cleaned_jd)
        results.append({"filename": file.filename, "score": score})
        
    return {"results": sorted(results, key=lambda x: x['score'], reverse=True)}