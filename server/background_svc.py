import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from celery import Celery
from clients.pubmed_cli import PubMedClient

app = Celery('background_svc', broker='redis://redis', backend='redis://redis')

pubmed_cli = PubMedClient(email="j040_k4rd050@hotmail.com")

@app.task
def process_query(search_query, ids):
    # For demonstration purposes
    start_time = time.time()

    time.sleep(3)
    #TODO: Fetch the actual data from PubMed

    end_time = time.time()
    run_time = end_time - start_time

    return {
        "run_seconds": run_time,
        "data":{
            "pmids": ids,
        }
    }