import sys
sys.path.append('.')
from src.works.subagent.data.collections import col_repositories
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader

async def load_data(file_path) : 
    dataset = DataFileReader.from_json(file_path)
    return dataset
    
async def main() :      
    path = f'e:/research_subagent/data/raw/REPOSITORIES'    

    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]

    temp_results = await AsyncTaskRunner.run(load_data, task_args)     

    try : 
        col_repositories.insert_many(temp_results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )    