import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from datetime import datetime
from flask import Flask, jsonify, request

from clients.pubmed_cli import PubMedClient
from background_svc import process_query

pubmed_cli = PubMedClient(email="")

app = Flask(__name__)

# TODO: Would replace this with a database
tasks = {}

def search_ids(search_query):
    res = pubmed_cli.search(search_query)
    return res

@app.route('/search', methods=['GET'])
def search():
    search_query = request.args.get('term')
    if search_query is None:
        return jsonify({'error': 'Missing search term'}), 400
    pre_res = search_ids(search_query)

    res = process_query.delay(search_query, pre_res['esearchresult']['idlist'])
    tasks[res.id] = {
        "task": res,
        "created_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    return jsonify({
        'records': pre_res['esearchresult']['count'],
        'query': search_query,
        'task_id': res.id
    }), 200

@app.route('/fetch/<task_id>', methods=['GET'])
def fetch(task_id):
    if task_id in tasks:
        if tasks[task_id]["task"].ready():
            return jsonify({
                'task_id': task_id,
                'status': 'completed',
                'result': tasks[task_id]["task"].get().get('data'),
                'created_time': tasks[task_id]["created_time"],
                'run_seconds': tasks[task_id]["task"].get().get("run_seconds")
                }), 200
            
        return jsonify({
                'task_id': task_id,
                'status': 'processing',
                'created_time': tasks[task_id]["created_time"]
                }), 202
    else:
        return jsonify({'error': 'Task ID not found'}), 404
    
@app.route('/release', methods=['GET'])
def release_tasks():
    res = []
    for task in tasks:
        res.append(task["task"].get(timeout=1))

    return res

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
