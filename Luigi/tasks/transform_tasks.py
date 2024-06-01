# tasks/transform_tasks.py

import luigi
import pandas as pd
import json
import logging
from tasks.fetch_tasks import FetchAPIData

# Set up logging
logger = logging.getLogger('luigi-interface')

class FlattenAndSaveParquet(luigi.Task):
    def requires(self):
        return FetchAPIData()

    def output(self):
        return luigi.LocalTarget('data/flattened_data.parquet')

    def run(self):
        logger.info('Starting FlattenAndSaveParquet task...')
        
        # Read the JSON data from the output of the FetchAPIData task
        with self.input().open('r') as f:
            data = json.load(f)
        
        # Flatten the JSON data using pandas
        df = pd.json_normalize(data)
        
        # Save the flattened data as a Parquet file
        df.to_parquet(self.output().path, index=False)
        
        logger.info('Finished FlattenAndSaveParquet task.')
