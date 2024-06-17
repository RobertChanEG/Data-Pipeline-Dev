import luigi
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

    