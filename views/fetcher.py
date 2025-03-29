import requests
from typing import List, Dict

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query: str, debug: bool = False) -> List[Dict]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  
    }
    
    response = requests.get(PUBMED_API_URL, params=params)
    
    if response.status_code != 200:
        raise Exception(f"PubMed API error: {response.status_code}")
    
    data = response.json()
    paper_ids = data["esearchresult"].get("idlist", [])

    papers = []
    for pubmed_id in paper_ids:
        paper_details = get_paper_details(pubmed_id)
        papers.append(paper_details)

        if debug:
            print(f"Fetched: {paper_details}")

    return papers

def get_paper_details(pubmed_id: str) -> Dict:
    params = {
        "db": "pubmed",
        "id": pubmed_id,
        "retmode": "json"
    }
    
    response = requests.get(PUBMED_SUMMARY_URL, params=params)
    
    if response.status_code != 200:
        return {"PubmedID": pubmed_id, "Title": "N/A", "Publication Date": "N/A"}

    data = response.json()
    result = data["result"].get(pubmed_id, {})

    return {
        "PubmedID": pubmed_id,
        "Title": result.get("title", "N/A"),
        "Publication Date": result.get("pubdate", "N/A"),
    }
