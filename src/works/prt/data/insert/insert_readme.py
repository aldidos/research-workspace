import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_readmes
from src.util.data_file_rw import DataFileReader
from pathlib import Path
import asyncio
from src.task.async_task_runner import AsyncTaskRunner

async def load_data(file_path : Path) : 
    readme = DataFileReader.from_json(file_path)

    repo_id = file_path.name.split('.')[0]
    repo_id = int(repo_id)

    readme['repo_id'] = repo_id

    return readme

async def main() : 
    task_dataset = DataFileReader.find_files('../data/raw/READMES', 'json')
    task_args = [ [data] for data in task_dataset]
   
    results = await AsyncTaskRunner.run(load_data, task_args)          
    
    col_readmes.insert_many(results)

if __name__ == '__main__' : 
    asyncio.run(main())    