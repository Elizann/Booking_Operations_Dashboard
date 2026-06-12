import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_insight(data):

    if not API_KEY:
        return "Error: OPENROUTER_API_KEY is missing in .env file"

    prompt = f"""
You are an Operations Analyst.

Analyze this booking data.

Provide:

1. Key Trends  
2. Risks  
3. Anomalies  
4. Recommendations  

Keep insights short, clear, and actionable.

IMPORTANT: Use branch_name and service_name for interpretation. Do not treat IDs as meaningful.

Data:
{data}
"""

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json",
                "HTTP-Referer": "http://localhost:8501",
                "X-Title": "Booking Dashboard"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            },
            timeout=30
        )

        response.raise_for_status()
        result = response.json()

        return (
            result.get("choices", [{}])[0]
            .get("message", {})
            .get("content", "No response generated")
        )

    except requests.exceptions.RequestException as e:
        return f"API Request Error: {str(e)}"

    except Exception as e:
        return f"Unexpected Error: {str(e)}"