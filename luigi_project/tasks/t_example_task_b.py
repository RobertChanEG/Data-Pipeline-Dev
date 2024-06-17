import luigi
import logging
from tasks.t_example_task_a import Task_A

# Configure the logger
logger = logging.getLogger('luigi-interface')

class Task_B(luigi.Task):
    param = luigi.Parameter(default='default_value')

    def requires(self):
        # TaskB depends on TaskA
        return Task_A(param=self.param)

    def output(self):
        return luigi.LocalTarget(f'output/task_b_{self.param}.txt')

    def run(self):
        logger.info(f'Running TaskB with parameter {self.param}')
        with self.output().open('w') as f:
            f.write(f'This is TaskB with parameter {self.param}')
        logger.info('TaskB completed successfully')

