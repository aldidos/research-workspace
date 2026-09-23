import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_commits
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.dataset.aiAgent.db_collection import raw_dataset_path

async def load_data(file_path) : 
    repo_id = file_path.parts[-2]
    repo_id = int(repo_id)
    data = DataFileReader.from_json(file_path)
    data['repo_id'] = repo_id
    return data    
    
async def main() :  
    path = f'{raw_dataset_path}/raw/COMMITS'

    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]
    
    temp_results = await AsyncTaskRunner.run(load_data, task_args)      

    try : 
        col_commits.insert_many(temp_results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )    