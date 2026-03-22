from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Browser Agent API running"}

@app.get("/quotes")
def get_quotes():
    with open("data/quotes_all.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/analysis")
def get_analysis():
    with open("data/analysis_report.json", "r", encoding="utf-8") as f:
        return json.load(f)