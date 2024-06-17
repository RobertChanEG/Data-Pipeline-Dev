import luigi
import logging
import logging.config

# Configure loggings
logging.basicConfig(
    filename='logs/luigi.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Configure the logger
logger = logging.getLogger('luigi-interface')

class Task_A(luigi.Task):
    param = luigi.Parameter(default='default_value')

    def requires(self):
        None

    def output(self):
        return luigi.LocalTarget(f'output/task_a_{self.param}.txt')

    def run(self):
        logger.info('Starting LongRunningTask...')
        # Simulate a long-running task by sleeping for 1 minute (60 seconds)
        time.sleep(10)
        # Write to the output file to mark the task as complete
        with self.output().open('w') as f:
            f.write('Task completed successfully')
        logger.info('Finished LongRunningTask.')

