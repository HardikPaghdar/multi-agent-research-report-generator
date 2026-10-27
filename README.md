# Multi-Agent Research & Report Generator

A deterministic research pipeline prototype separating source intake, evidence extraction, theme discovery, and report assembly into inspectable stages.

## Features
- Accept multiple source records with title and URL provenance
- Extract sentence-level evidence linked to its source
- Surface recurring long terms as exploratory themes
- Assemble a report with explicit human-review caveats
- FastAPI docs, tests, and CI

## Run
```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
Visit http://127.0.0.1:8000/docs and call `POST /research`.

## Example request
```json
{"topic":"AI reliability","sources":[{"title":"Research notes","url":"https://example.org/notes","text":"Evaluation improves reliability. Teams should verify claims."}]}
```

## Honest scope
This version does not browse the web, call LLMs, or autonomously verify facts. It is a deterministic multi-stage scaffold. Next steps: add a search adapter, typed workflow state, citation verification, retries, and model-backed synthesis with explicit tool permissions.

## Stack
Python, FastAPI, Pydantic, pytest. Free/open-source dependencies.

## Explore more

- [Multi-Agent Software Engineer](https://github.com/HardikPaghdar/multi-agent-software-engineer) — human-supervised task planning.
- [Production RAG Pipeline](https://github.com/HardikPaghdar/production-rag-pipeline) — evidence-grounded retrieval.
- [AI Agent Evaluation Platform](https://github.com/HardikPaghdar/ai-agent-evaluation-platform) — evaluation of recorded agent runs.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
