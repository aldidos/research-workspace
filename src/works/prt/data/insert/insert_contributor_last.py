import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_contributor_last
from util.data_file_rw import DataFileReader
import asyncio
from pathlib import Path
from src.task.async_task_runner import AsyncTaskRunner

async def load_data(file_path : Path) : 
    repo_id = file_path.parts[-2]
    repo_id = int(repo_id)
    dataset = await DataFileReader.async_from_json(file_path)
    print(file_path)

    for data in dataset :         
        data['repo_id'] = repo_id

    return dataset

async def main() : 
    dataset = DataFileReader.find_files('../data/raw/CONTRIBUTORS_LAST', 'json')
    task_args = [ [data] for data in dataset]    

    task_results = await AsyncTaskRunner.run(load_data, task_args)      

    results = []
    [ results.extend(r) for r in task_results ]
        
    col_contributor_last.insert_many(results)

if __name__ == '__main__' : 
    asyncio.run( main() )