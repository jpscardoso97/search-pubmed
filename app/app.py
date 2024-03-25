import streamlit as st
import pandas as pd
import time

from fetcher import send_query, fetch_data

# Page title
st.set_page_config(page_title='PubMed Explorer', page_icon='💉')
st.title('PubMed Explorer')

# Sidebar
st.sidebar.header('PubMed Search')
st.sidebar.markdown('Search for articles in the PubMed repository')
  # Search query
search_query = st.sidebar.text_input('Enter search query', 'COVID-19')
# choose number of results (maximum of 100)
max_results = st.sidebar.slider('Number of results', 1, 100, 10)

data = "Perform a search to see the results"

if st.sidebar.button('Search'):
  st.write(f'Searching for articles on "{search_query}"...')
  res = send_query(search_query)
  task_id = res['task_id']
  st.write(f"Found {res['records']} records for search")

  attempts = 0
  st.write(f'Fetching data for task ID: {task_id}')
  while attempts < 5:
    data = fetch_data(task_id)
    if data['status'] == 'completed':
      data = pd.DataFrame(data.get('result')['pmids'], columns=['PMID']).head(max_results)
      break
    time.sleep(2)
    attempts += 1

st.write(data)
