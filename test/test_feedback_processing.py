import json
from Employee_sentiment_analysis.models.feedback_processing import parse_feedback_file

feedback_json = parse_feedback_file('../feedback_data/feedback.txt')
print(json.dumps(feedback_json, indent=2, ensure_ascii=False))