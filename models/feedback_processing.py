import re
import json

FIELD_PATTERNS = {
    'employee_id': r'Employee ID:\s*([^\|\n]+)',
    'name': r'Name:\s*([^\|\n]+)',
    'dept': r'Dept:\s*([^\|\n]+)',
    'tenure': r'Tenure:\s*([^\|\n]+)',
    'gender': r'Gender:\s*([^\|\n]+)',
    'location': r'Location:\s*([^\|\n]+)',
    'email': r'Email:\s*([^\|\n]+)',
    'phone': r'Phone:\s*([^\|\n]+)',
}

def parse_feedback_file(file_path):
    feedbacks = []
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    entries = re.split(r'\n\s*\n', content.strip())
    for entry in entries:
        entry_data = {key: None for key in FIELD_PATTERNS}
        lines = entry.splitlines()
        meta_line = lines[0] if lines and 'Feedback:' not in lines[0] else ""
        for key, pattern in FIELD_PATTERNS.items():
            match = re.search(pattern, meta_line)
            if match:
                value = match.group(1).strip()
                if key == 'employee_id':
                    try:
                        value = int(value)
                    except Exception:
                        value = None
                entry_data[key] = value
        feedback = None
        feedback_match = re.search(r'Feedback:\s*(.*)', entry, re.DOTALL)
        if feedback_match:
            feedback = feedback_match.group(1).strip()
        else:
            feedback_lines = []
            for line in lines:
                if not re.match(r'^(Employee ID:|Name:|Dept:|Tenure:|Gender:|Location:|Email:|Phone:)', line):
                    feedback_lines.append(line.strip())
            feedback = ' '.join(feedback_lines).strip() if feedback_lines else None
        entry_data['feedback'] = feedback
        feedbacks.append(entry_data)
    return feedbacks