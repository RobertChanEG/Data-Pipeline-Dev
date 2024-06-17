import luigi
import logging

# Configure the logger
logger = logging.getLogger('luigi-interface')

class ExampleTask(luigi.Task):
    param = luigi.Parameter(default='default_value')

def requires(self):
    # Specify any dependencies here
    None

def output(self):
    # Define the output target for this task
    return luigi.LocalTarget(f'output/{self.param}.txt')

def run(self):
    try:
        # Log the start of the task
        logger.info(f'Running ExampleTask with parameter {self.param}')
        
        # Simulate a task failure for demonstration purposes
        if self.param == 'fail':
            raise ValueError("Simulated failure")
        
        # Write the output to the specified target
        with self.output().open('w') as f:
            f.write(f'This is an example task with parameter {self.param}')
        
        # Log the completion of the task
        logger.info('ExampleTask completed successfully')

    except ValueError as e:
        # Log the simulated failure
        logger.error(f"Error: {e}")
        # Exit with a specific error code
        sys.exit(1)

