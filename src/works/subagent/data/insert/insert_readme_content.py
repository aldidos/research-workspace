import sys
sys.path.append('.')
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.works.subagent.data.collections import col_readme_contents

async def load_data(file_path) : 
    repo_id = file_path.parts[-1]
    repo_id = repo_id.split('.')[0]
    repo_id = int(repo_id)
    readme_content = DataFileReader.from_json(file_path)
    readme_content['repo_id'] = repo_id

    return readme_content
    
async def main() :  
    path = f'e:/research_subagent/data/raw/README_CONTENTS'
    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]    
    temp_results = await AsyncTaskRunner.run(load_data, task_args)     

    try : 
        col_readme_contents.insert_many(temp_results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() ) 