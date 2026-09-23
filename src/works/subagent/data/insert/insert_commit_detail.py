import sys
sys.path.append('.')
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.works.subagent.data.collections import col_commit_detail

async def load_data(file_path) : 
    repo_id = file_path.parts[-2]
    repo_id = int(repo_id)
    commit_detail = DataFileReader.from_json(file_path)
    commit_detail['repo_id'] = repo_id

    return commit_detail
    
async def main() :  
    path = f'e:/research_subagent/data/raw/COMMIT_DETAIL'
    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]    
    temp_results = await AsyncTaskRunner.run(load_data, task_args)     

    try : 
        col_commit_detail.insert_many(temp_results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() ) 