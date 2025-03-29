import pytest
from fetcher import fetch_pubmed_papers

def test_fetch_pubmed_papers():
    papers = fetch_pubmed_papers("cancer", debug=True)
    assert isinstance(papers, list)
    assert len(papers) > 0
    assert "PubmedID" in papers[0]
    assert "Title" in papers[0]
