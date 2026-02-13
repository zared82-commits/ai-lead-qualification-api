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
