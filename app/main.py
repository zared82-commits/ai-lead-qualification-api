from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os, json
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

app = FastAPI(title="AI Lead Qualification API", version="1.0.0")
client = OpenAI(api_key=API_KEY)

class LeadRequest(BaseModel):
    message: str
    source: str | None = "website"
    budget: str | None = "unknown"
    language: str | None = "en"

SYSTEM_PROMPT = (
    "You are a sales assistant that qualifies incoming leads.\n"
    "Return ONLY valid JSON with keys:\n"
    "lead_score (1-10), intent, recommended_action, confidence (low|medium|high), notes (optional).\n"
    "No markdown. JSON only."
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze-lead")
def analyze_lead(payload: LeadRequest):
    if not API_KEY or API_KEY == "dummy":
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY missing in .env")

    user_content = {
        "message": payload.message,
        "source": payload.source,
        "budget": payload.budget,
        "language": payload.language,
    }

    try:
        resp = client.chat.completions.create(
            model=MODEL,
            temperature=0.2,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": json.dumps(user_content, ensure_ascii=False)},
            ],
        )
        text = resp.choices[0].message.content.strip()
        return json.loads(text)
    except json.JSONDecodeError:
        raise HTTPException(status_code=502, detail="Model returned non-JSON output")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

