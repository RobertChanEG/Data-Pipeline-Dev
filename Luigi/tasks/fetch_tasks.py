# tasks/fetch_tasks.py

import luigi
import requests
import json
import logging

# Set up logging
logger = logging.getLogger('luigi-interface')

class FetchAPIData(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data/api_response.json')

    def run(self):
        logger.info('Starting FetchAPIData task...')
        
        # Make a GET request to the public API
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        
        # Check if the request was successful
        if response.status_code == 200:
            logger.info('API request successful.')
        else:
            logger.error(f'API request failed with status code: {response.status_code}')
        
        # Parse the JSON response
        data = response.json()
        
        # Write the JSON data to a file
        with self.output().open('w') as f:
            json.dump(data, f, indent=4)
        
        logger.info('Finished FetchAPIData task.')
