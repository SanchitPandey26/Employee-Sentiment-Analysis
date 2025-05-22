import os
import json
from dotenv import load_dotenv
from Employee_sentiment_analysis.models.feedback_llm_analysis import call_feedback_llm
from Employee_sentiment_analysis.models.feedback_processing import parse_feedback_file

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

feedback_json = parse_feedback_file('../feedback_data/feedback.txt')
llm_result_str = call_feedback_llm(feedback_json, api_key)
try:
    llm_result = json.loads(llm_result_str)
except Exception:
    llm_result = llm_result_str
print(llm_result)
