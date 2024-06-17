import os

# Define the structure of directories and files
project_name = 'luigi_project'

directories = [
    project_name,
    os.path.join(project_name, 'tasks'),
    os.path.join(project_name, 'configs'),
    os.path.join(project_name, 'logs'),
    os.path.join(project_name, 'state'),
    os.path.join(project_name, 'output')
]

files = {
    os.path.join(project_name, 'luigi.cfg'): """[core] # Core configuration for Luigi
state-path = ./state # Directory to store the state of the workflows
local-scheduler = True # Local scheduler configuration
default-log-level = DEBUG # Setting to control the log level for Luigi tasks
config-path = ./configs/luigi_logging.conf # Path to the configuration file for logging

[worker] # Worker configuration for Luigi
workers = 4 # Number of parallel processes for Luigi workers
keep-alive = True # Keep alive interval for workers in seconds
timeout = 3600 # Timeout period for worker processes in seconds

[resources] # Resource management configuration
example_resource = 1 # Specify resources available to tasks

[task_history] # Task history configuration
record_task_history = True # Enable/disable task history for monitoring

[logging] # Logging configuration for Luigi
config-path = ./configs/luigi_logging.conf # Specify logging configuration file path

[notifications] # Notifications configuration for Luigi
email = True # Enable email notifications for task failures
email-prefix = [Luigi] # Prefix for the subject line of notification emails

# SMTP server settings
smtp-host = smtp.example.com
smtp-port = 587
smtp-ssl = False
smtp-user = your_email@example.com
smtp-password = your_password

# Recipient email address
receiver = recipient@example.com

""",
    os.path.join(project_name, 'w_pipeline_init.py'): 
"""import luigi
import logging
import importlib

from tasks.t_example_task_a import Task_A
from tasks.t_example_task_b import Task_B
from tasks.t_example_task import ExampleTask

# Configure the logger
logger = logging.getLogger('luigi-interface')

if __name__ == '__main__':

    # Run TaskB using Luigi's local scheduler
    # TaskB will automatically run TaskA first because of the dependency
    luigi.build([
        ExampleTask(param='fail'),
        Task_B(param='B'),
        Task_A(param='A')
    ], local_scheduler=True)

    """,

    os.path.join(project_name, 'logs', 'luigi.log'): "",

    os.path.join(project_name, 'tasks', '__init__.py'): "",
    
    os.path.join(project_name, 'tasks', 't_example_task.py'): 
    
"""import luigi
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

""",
    os.path.join(project_name, 'tasks', 't_example_task_a.py'): 
"""import luigi
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

""",
    os.path.join(project_name, 'tasks', 't_example_task_b.py'): 
"""import luigi
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

""",

    os.path.join(project_name, 'configs', 'luigi_logging.conf'): 
    
"""
[loggers]
keys=root,luigi

[log file path]
log-file = .logs/luigi.log

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=consoleFormatter,fileFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler,fileHandler

[logger_luigi]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=luigi

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=consoleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=fileFormatter
args=('logs/luigi.log', 'a')

[formatter_consoleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=

[formatter_fileFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=

""",
    
    os.path.join(project_name, 'README.md'): 
"""# Luigi Project

This is a simple project setup for Luigi.

## Structure

- `tasks/`: Contains Luigi tasks.
- `configs/`: Contains configuration files.
- `logs/`: Directory for logs.
- `state/`: Directory for storing state information.
- `luigi.cfg`: Main configuration file for Luigi.

## Example Task

An example tasks is provided in `tasks/example_task.py`, which demonstrates a simple Luigi task with logging and error handling.
task_A and task_B are also provided to demonstrate task dependencies.

To run the wrapper task:
```sh
python w_pipeline_init.py
"""
}

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    print(f"Created directory: {directory}")

# Create files
for file_path, content in files.items():
    with open(file_path, 'w') as file:
        file.write(content)
        print(f"Created file: {file_path}")