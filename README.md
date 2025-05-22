# Employee Sentiment Analysis Pipeline

A modern, modular AI pipeline for analyzing employee feedback using Google Gemini LLM and embeddings. The system is wrapped as a FastAPI service for easy integration, batch processing, and cloud deployment.

---

## 🚀 Features

- 📝 **Flexible Feedback Parsing:** Handles structured, semi-structured, and unstructured feedback with various metadata fields.
- 🤖 **LLM Sentiment & Attrition Analysis:** Uses Gemini LLM to classify sentiment, predict attrition risk, summarize issues, and recommend HR actions.
- 📦 **Batch & API Support:** Upload a feedback file and get actionable insights in JSON.
- ☁️ **Cloud-Ready:** Easily deployable on Google Cloud, Azure, AWS, or locally.

---

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Google Gemini API](https://ai.google.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [NumPy](https://numpy.org/)

---

## Getting Started

### 1. Clone the Repository

```commandline
git clone https://github.com/SanchitPandey26/Employee_sentiment_analysis.git
cd Employee_sentiment_analysis
```

### 2. Install Dependencies

```commandline
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```dotenv
GEMINI_API_KEY=your-google-gemini-api-key-here
```

### 4. Add Your Data

- Place your feedback text file (e.g., `feedback.txt`) in the project directory.

---

## Running the FastAPI Server

From the `Employee_sentiment_analysis` directory, run:

```commandline
uvicorn api.feedback_api:app --reload
```

- The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Interactive API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Using the API

### Endpoint

- **POST** `/analyze_feedback/`

### Parameters

- `feedback_file`: Upload your feedback `.txt` file (supports structured and unstructured entries).

### Example Using Swagger UI

1. Go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Click "Try it out" on `/analyze_feedback/`
3. Upload your `feedback.txt` file and execute.

### Example Using cURL

```commandline
curl -X 'POST'
'http://127.0.0.1:8000/analyze_feedback/'
-F 'feedback_file=@feedback.txt'
```

---

## Project Structure

```text
Employee_sentiment_analysis/
├── models/
│ ├── feedback_processing.py
│ └── feedback_llm_analysis.py
├── api/
│ └── feedback_api.py # FastAPI app
├── feedback.txt # Example feedback file
├── requirements.txt
└── .env
```

---
## Output

- Returns a JSON object with:
  - `individual_analysis`: List of sentiment, attrition risk, summary, and HR action for each feedback.
  - `grouped_actions`: Summarized actions and employee IDs for each group of similar feedback.

---
## Contributing

*Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.*

---
## License

*This project is licensed under the [MIT License](./LICENSE) © 2025 Sanchit Pandey.*

You are free to use, modify, and distrivute this software with attribution.
See the LICENSE file for details.

---
## Contact

*For questions or demo requests, contact [sanchit.pdy@gmail.com].*

---

**Happy analyzing! 🚀**
