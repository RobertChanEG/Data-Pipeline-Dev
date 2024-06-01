# tasks/fetch_tasks.py

import luigi
import requests
import json

class FetchAPIData(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data/api_response.json')

    def run(self):
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        data = response.json()
        with self.output().open('w') as f:
            json.dump(data, f, indent=4)
