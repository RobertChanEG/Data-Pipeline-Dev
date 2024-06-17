# Luigi Project

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
