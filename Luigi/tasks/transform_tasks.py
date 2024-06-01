# tasks/transform_tasks.py

import luigi
import pandas as pd
import json
from tasks.fetch_tasks import FetchAPIData

class FlattenAndSaveParquet(luigi.Task):
    def requires(self):
        return FetchAPIData()

    def output(self):
        return luigi.LocalTarget('data/flattened_data.parquet')

    def run(self):
        with self.input().open('r') as f:
            data = json.load(f)
        df = pd.json_normalize(data)
        df.to_parquet(self.output().path, index=False)
