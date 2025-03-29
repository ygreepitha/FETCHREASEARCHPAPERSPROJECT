import argparse
from fetcher import fetch_pubmed_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed.")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()

    papers = fetch_pubmed_papers(args.query, debug=args.debug)

    if args.file:
        import pandas as pd
        df = pd.DataFrame(papers)
        df.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        for paper in papers:
            print(paper)

if __name__ == "__main__":
    main()
