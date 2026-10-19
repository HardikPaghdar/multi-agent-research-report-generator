from fastapi import FastAPI
from pydantic import BaseModel, Field
from collections import Counter

app = FastAPI(title="Multi-Agent Research & Report Generator", version="0.1.0")

class Source(BaseModel):
    title: str = Field(min_length=1)
    url: str = ""
    text: str = Field(min_length=1)

class ResearchRequest(BaseModel):
    topic: str = Field(min_length=2)
    sources: list[Source] = Field(min_length=1)

def build_report(topic: str, sources: list[Source]) -> dict:
    evidence = []
    for i, source in enumerate(sources, start=1):
        sentences = [s.strip() for s in source.text.replace("!", ".").split(".") if s.strip()]
        evidence.extend({"source_id": i, "source_title": source.title, "url": source.url, "claim": sentence}
                        for sentence in sentences)
    counts = Counter(word.lower().strip(".,!?") for s in sources for word in s.text.split() if len(word) > 5)
    themes = [word for word, _ in counts.most_common(5)]
    return {"topic": topic, "source_count": len(sources), "evidence": evidence,
            "recurring_terms": themes,
            "report": f"Research brief: {topic}\n\nSources reviewed: {len(sources)}. Extracted evidence statements: {len(evidence)}.\n\nRecurring terms: {', '.join(themes) or 'None detected'}.\n\nEvidence is listed separately below for human review; recurring terms are exploratory signals, not verified conclusions."}

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/research")
def research(request: ResearchRequest): return build_report(request.topic, request.sources)
