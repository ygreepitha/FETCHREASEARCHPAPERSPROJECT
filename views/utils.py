import pandas as pd

def save_to_csv(papers: list, filename: str):
    """Save the extracted paper details to CSV."""
    df = pd.DataFrame(papers)
    df.to_csv(filename, index=False)

