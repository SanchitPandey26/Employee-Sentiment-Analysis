from fastapi import FastAPI, UploadFile, File
import os
import json
from dotenv import load_dotenv
from Employee_sentiment_analysis.models.feedback_llm_analysis import call_feedback_llm
from Employee_sentiment_analysis.models.feedback_processing import parse_feedback_file

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

app = FastAPI()

@app.post("/analyze_feedback/")
async def analyze_feedback(feedback_file: UploadFile = File(...)):
    content = await feedback_file.read()
    temp_path = f"/tmp/{feedback_file.filename}"
    with open(temp_path, "wb") as f:
        f.write(content)
    feedback_json = parse_feedback_file(temp_path)
    os.remove(temp_path)
    llm_result_str = call_feedback_llm(feedback_json, api_key)
    try:
        llm_result = json.loads(llm_result_str)
    except Exception:
        llm_result = llm_result_str
    return llm_result

@app.get("/")
def read_root():
    return {"message": "Employee Feedback Analysis API is running."}
