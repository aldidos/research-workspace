import sys
sys.path.append('.')
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.works.subagent.data.collections import col_repo_contents

async def load_data(file_path) : 
    repo_id = file_path.parts[-1]
    repo_id = repo_id.split('_')[0]
    repo_id = int(repo_id)
    repo_contents = DataFileReader.from_json(file_path)
    results = []
    for repo_content in repo_contents : 
        repo_content['repo_id'] = repo_id
        results.append(repo_content)
    return results
    
async def main() :  
    path = f'e:/research_subagent/data/raw/REPO_CONTENTS'
    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]    
    temp_results = await AsyncTaskRunner.run(load_data, task_args) 

    # results = list( map(lambda x : x, temp_results) )    
    results = []
    [ results.extend(t) for t in temp_results]

    try : 
        col_repo_contents.insert_many(results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() ) 