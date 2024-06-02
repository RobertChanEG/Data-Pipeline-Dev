@echo off
REM Activate the Anaconda environment
call C:\Users\robert.chan\anaconda3\Scripts\activate.bat C:\Users\Rob\anaconda3\envs\data_pipe_dev

REM Set LUIGI_CONFIG_PATH to point to your configuration file
SET LUIGI_CONFIG_PATH = "C:/Users/robert.chan/Downloads/Data-Pipeline-Dev/Luigi/luigi.cfg"

REM Run the Python script with the specified Luigi task
python "C:/Users/robert.chan/Downloads/Data-Pipeline-Dev/Luigi/pipeline.py"

REM Pause the command window to see the output
PAUSE