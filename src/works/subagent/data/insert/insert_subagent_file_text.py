import sys
sys.path.append('.')
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.works.subagent.data.collections import col_subagent_file_text

async def load_data(file_path) : 
    file_info = DataFileReader.from_json(file_path)    

    return file_info
    
async def main() :  
    path = f'e:/research_subagent/data/raw/SUBAGENT_FILES'
    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]    
    temp_results = await AsyncTaskRunner.run(load_data, task_args)     

    try : 
        col_subagent_file_text.insert_many(temp_results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() ) 