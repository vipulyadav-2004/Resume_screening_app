from flask import Flask, render_template, request
from src.preprocessor import clean_text
from src.matcher import matcher_engine  # Import our advanced singleton instance

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', results=None)

@app.route('/score', methods=['POST'])
def score_resumes():
    if request.method == 'POST':
        job_desc = request.form.get('job_description', '')
        cleaned_job_desc = clean_text(job_desc)
        
        uploaded_files = request.files.getlist('resumes')
        scores_list = []
        
        for file in uploaded_files:
            if file.filename == '':
                continue
                
            raw_resume_text = file.stream.read().decode('utf-8', errors='ignore')
            cleaned_resume_text = clean_text(raw_resume_text)
            
            # --- CALL THE ADVANCED NEURAL MATCHER ---
            match_pct = matcher_engine.calculate_match_score(cleaned_resume_text, cleaned_job_desc)
            
            scores_list.append({
                'filename': file.filename,
                'score': match_pct
            })
            
        ranked_results = sorted(scores_list, key=lambda x: x['score'], reverse=True)
        return render_template('index.html', results=ranked_results)

if __name__ == '__main__':
    app.run(debug=True)