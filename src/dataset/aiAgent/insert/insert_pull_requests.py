import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_pull_requests, raw_dataset_path
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader

async def load_data(file_path) : 
    repo_id = file_path.parts[-2]
    repo_id = int(repo_id)
    data = DataFileReader.from_json(file_path)
    data['repo_id'] = repo_id
    return data    
    
async def main() :  
# def main() :      
    path = f'{raw_dataset_path}/raw/PULL_REQUESTS'

    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]
    
    temp_results = await AsyncTaskRunner.run(load_data, task_args)      

    try : 
        col_pull_requests.insert_many(temp_results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )    