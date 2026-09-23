import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_pull_request_templates, col_contributing_files
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader

async def load_data(file_path) : 
    data = DataFileReader.from_json(file_path)
    return data
    
async def main() :  
# def main() :      
    path = '../data/raw/TEMP_CONTRIBUTING_FILES'

    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]
    results = []    

    results = await AsyncTaskRunner.run(load_data, task_args)      
    # results = ConcurTaskRunner(128).run(processing_data, task_args)  

    try : 
        col_contributing_files.insert_many(results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )    
