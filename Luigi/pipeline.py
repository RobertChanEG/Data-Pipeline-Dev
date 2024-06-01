import luigi
from tasks.transform_tasks import FlattenAndSaveParquet
import logging

# Debugging: Check if the configuration is loaded
from luigi.configuration import get_config

def print_configurations():
    config = get_config()
    print("Core Configuration:")
    print("Default Scheduler Host:", config.get('core', 'default-scheduler-host'))
    print("Default Target Directory:", config.get('core', 'default-target-directory'))
    print("Logging Configuration:")
    print("Log File:", config.get('logging', 'log-file'))
    print("Log Level:", config.get('logging', 'log-level'))

if __name__ == '__main__':
    # Print configurations to verify they are loaded correctly
    print_configurations()

    # Configure logging
    logging.basicConfig(
        filename='C:/Users/Rob/Downloads/Data Pipeline Dev/Luigi/logs/luigi.log',
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    luigi.run(['FlattenAndSaveParquet', '--local-scheduler'])
