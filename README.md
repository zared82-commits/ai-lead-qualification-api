# AI Lead Qualification API

AI-powered REST API that analyzes incoming leads and returns:

- Lead score (0–10)
- Intent classification
- Recommended next action
- Confidence level
- AI reasoning notes

## Tech Stack

- FastAPI
- OpenAI API
- Python 3.11
- Uvicorn

## Example Request

POST /analyze-lead

```json
{
  "message": "Hi, I want pricing for your premium package. Can we schedule a call?",
  "source": "website",
  "budget": "unknown",
  "language": "en"
}

📤 Example Response
{
  "lead_score": 8,
  "intent": "requesting pricing and scheduling a call",
  "recommended_action": "Schedule a call to discuss premium package pricing",
  "confidence": "high",
  "notes": "Lead is actively seeking information on pricing and is open to a call."
}

▶ How To Run Locally

pip install -r requirements.txt
uvicorn app.main:app --reload

Open Swagger UI:
http://localhost:8000/docs

👨‍💻 Author

Eduard Zaremba
Backend / DevOps / AI Integration Engineer






