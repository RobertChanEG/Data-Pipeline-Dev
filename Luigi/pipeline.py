# pipeline.py

import luigi
from tasks.transform_tasks import FlattenAndSaveParquet

if __name__ == '__main__':
    luigi.run(['FlattenAndSaveParquet', '--local-scheduler'])
