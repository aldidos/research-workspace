import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_issues
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.dataset.aiAgent.db_collection import raw_dataset_path

async def load_data(file_path) : 
    repo_id = file_path.name.split('.')[0]
    repo_id = int(repo_id)
    dataset = DataFileReader.from_json(file_path)
    temp_dataset = []
    for data in dataset : 
        data['repo_id'] = repo_id
        temp_dataset.append(data)
    return temp_dataset
    
async def main() :  
    path = f'{raw_dataset_path}/raw/ISSUES'

    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]
    results = []    

    temp_results = await AsyncTaskRunner.run(load_data, task_args)      

    [ results.extend(r) for r in temp_results ]

    try : 
        col_issues.insert_many(results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )    