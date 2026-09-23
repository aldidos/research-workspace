import sys
sys.path.append('.')
from pathlib import Path
from src.util.data_file_rw import DataFileReader
from src.works.prt.data.db_collection import col_pull_requests, col_pull_requests_exp_01
from src.util.date_time_util import to_datetime
import concurrent.futures
from src.task.async_task_runner import AsyncTaskRunner
import asyncio

async def insert(file_path) : 
    print(file_path)
    repo_id = file_path.parts[-2]
    repo_id = int(repo_id)

    dataset = []
    temp_dataset = DataFileReader.from_json(file_path)
    
    for data in temp_dataset : 
        data['repo_id'] = repo_id
        dataset.append( data )
    
    return dataset

async def main() :
    base_dir_path = '../data/raw/PULL_REQUESTS_EXP_01'
    temp_file_paths = Path(base_dir_path).glob('**/*.json')
    file_paths = [ [fp] for fp in temp_file_paths ]     
    
    temp_results = await AsyncTaskRunner.run( insert, file_paths )
    results = []
    [ results.extend(r) for r in temp_results ] 

    try : 
        col_pull_requests_exp_01.insert_many( results, ordered = False )
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )