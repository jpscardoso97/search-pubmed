import requests

class PubMedClient:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    search_url = base_url + "esearch.fcgi"
    fetch_url = base_url + "efetch.fcgi"
    appName = "PubMedSearch"

    def __init__(self, email: str):
        self.email = email

    def search(self, query: str, retmax: int = 10):
        params = {
            "db": "pubmed",
            "term": query,
            "retmax": retmax,
            "retmode": "json"
        }
        response = requests.get(self.search_url, params=params)
        response.raise_for_status()
        
        return response.json()

            