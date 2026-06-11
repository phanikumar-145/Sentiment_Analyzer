from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client safely
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_review(review):
    prompt = f"""
You are an AI assistant that analyzes product reviews.

Review:
{review}

Return the output in this format:
1. Sentiment (Positive / Negative / Neutral)
2. Short Summary
3. Key Insights
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content