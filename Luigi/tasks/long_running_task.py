import luigi
import time
import logging
from tasks.transform_tasks import FlattenAndSaveParquet

# Set up logging
logger = logging.getLogger('luigi-interface')

class LongRunningTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget('data/long_running_task.txt')

    def requires(self):
        return FlattenAndSaveParquet()

    def run(self):
        logger.info('Starting LongRunningTask...')
        # Simulate a long-running task by sleeping for 1 minute (60 seconds)
        time.sleep(60)
        # Write to the output file to mark the task as complete
        with self.output().open('w') as f:
            f.write('Task completed successfully')
        logger.info('Finished LongRunningTask.')
