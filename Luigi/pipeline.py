import luigi  # Import the Luigi library
import requests  # Import requests to make HTTP requests to the API
import pandas as pd  # Import pandas for data manipulation and file saving
import json  # Import json to work with JSON data

# Define the first task to fetch data from a public API and save it as a JSON file
class FetchAPIData(luigi.Task):
    # Define the output of the task, which is a JSON file
    def output(self):
        return luigi.LocalTarget('data/api_response.json')  # The file path where the output will be saved

    # Define the run method where the main logic of the task is implemented
    def run(self):
        # Make a GET request to the public API
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        
        # Parse the JSON response
        data = response.json()
        
        # Write the JSON data to a file
        with self.output().open('w') as f:
            json.dump(data, f, indent=4)  # Save the JSON data with indentation for readability

# Define the second task to flatten the JSON data and save it as a Parquet file
class FlattenAndSaveParquet(luigi.Task):
    # Define the dependencies of this task
    def requires(self):
        return FetchAPIData()  # This task depends on the FetchAPIData task

    # Define the output of the task, which is a Parquet file
    def output(self):
        return luigi.LocalTarget('data/flattened_data.parquet')  # The file path where the output will be saved

    # Define the run method where the main logic of the task is implemented
    def run(self):
        # Read the JSON data from the output of the FetchAPIData task
        with self.input().open('r') as f:
            data = json.load(f)  # Load the JSON data
        
        # Flatten the JSON data using pandas
        df = pd.json_normalize(data)
        
        # Save the flattened data as a Parquet file
        df.to_parquet(self.output().path, index=False)

# The entry point of the script
if __name__ == '__main__':
    # Run the FlattenAndSaveParquet task using the local Luigi scheduler
    luigi.run(['FlattenAndSaveParquet', '--local-scheduler'])
