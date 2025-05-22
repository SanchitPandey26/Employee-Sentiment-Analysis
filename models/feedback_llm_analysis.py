import os
import json
from google import genai
from google.genai import types

def call_feedback_llm(feedback_json, api_key):
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash"

    prompt_feedbacks = []
    for entry in feedback_json:
        prompt_lines = []
        # Add all possible fields if available
        prompt_lines.append(f"Employee ID: {entry.get('employee_id', None)}" if entry.get('employee_id') else "")
        prompt_lines.append(f"Name: {entry.get('name', None)}" if entry.get('name') else "")
        prompt_lines.append(f"Dept: {entry.get('dept', None)}" if entry.get('dept') else "")
        prompt_lines.append(f"Tenure: {entry.get('tenure', None)}" if entry.get('tenure') else "")
        prompt_lines.append(f"Gender: {entry.get('gender', None)}" if entry.get('gender') else "")
        prompt_lines.append(f"Location: {entry.get('location', None)}" if entry.get('location') else "")
        prompt_lines.append(f"Email: {entry.get('email', None)}" if entry.get('email') else "")
        prompt_lines.append(f"Phone: {entry.get('phone', None)}" if entry.get('phone') else "")
        prompt_lines = [line for line in prompt_lines if line]
        meta = " | ".join(prompt_lines)
        if meta:
            prompt_feedbacks.append(f"{meta}\nFeedback: {entry.get('feedback', '')}")
        else:
            prompt_feedbacks.append(f"Feedback: {entry.get('feedback', '')}")

    feedbacks_block = "\n\n".join(prompt_feedbacks)

    prompt_text = f"""
Analyze the following employee feedback and return a JSON object with:
- employee_id (from the data, or null if not available)
- sentiment (positive, neutral, or negative)
- attrition_risk (low, medium, or high)
- summary (one-line summary of the main issue, praise, or theme)
- hr_action (suggested HR action, or null if not needed)

If any field is missing, set it to null.

After analyzing all feedback entries, group the feedbacks by similar summary/theme.
For each group, provide a separate JSON object with:
- summary (the shared summary/theme)
- employee_ids (list of employee IDs in this group, omit or set to null if not available)
- hr_action (a single, actionable HR recommendation for the group)

Output two sections:
1. "individual_analysis": a list of JSON objects for each feedback as above
2. "grouped_actions": a list of JSON objects for each group as above

Only output valid minified JSON, no commentary.

Feedback:

{feedbacks_block}
"""

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt_text)],
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=0.2,
        response_mime_type="application/json",
        system_instruction=[
            types.Part.from_text(text="""
You are an expert HR analyst.
Your task is to analyze employee feedback and extract actionable insights.
For each feedback entry, provide your output as a valid minified JSON object with the following fields:
employee_id (if available, otherwise null)
sentiment (positive, neutral, or negative)
attrition_risk (low, medium, or high)
summary (one-line summary of the main issue, praise, or theme)
hr_action (suggested HR action, or null if not needed)
Be accurate, unbiased, and concise. If a field is missing or not applicable, set it to null. Do not include any commentary, only the JSON.
"""),
        ],
    )

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        response_text += chunk.text

    response_text = response_text.strip()
    if response_text.startswith("```"):
        response_text = response_text[7:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]
    return response_text
