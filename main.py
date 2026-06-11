from fastapi import FastAPI
from schemas import ReviewRequest
from llm_service import analyze_review

app = FastAPI()



@app.get("/")
def home():
    return {
        "message":
        "Product Review Sentiment Analyzer Running"
    }


@app.post("/analyze-review")
def analyze(data: ReviewRequest):

    result = analyze_review(
        data.review
    )

    return {
        "analysis": result
    }