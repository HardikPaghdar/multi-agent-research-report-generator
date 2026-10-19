from app import Source, build_report

def test_report_keeps_evidence_provenance():
    result = build_report("AI reliability", [Source(title="Paper", url="https://example.org", text="Evaluation improves reliability. Teams should verify claims.")])
    assert result["source_count"] == 1
    assert result["evidence"][0]["source_title"] == "Paper"
    assert result["evidence"][0]["url"] == "https://example.org"
    assert "human review" in result["report"]

def test_empty_sentence_set_is_safe():
    result = build_report("topic", [Source(title="Notes", text="...")])
    assert result["evidence"] == []
