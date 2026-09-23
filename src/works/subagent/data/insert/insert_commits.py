import sys
sys.path.append('.')
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.works.subagent.data.collections import col_commits

async def load_data(file_path) : 
    repo_id = file_path.parts[-2]
    repo_id = int(repo_id)
    commits = DataFileReader.from_json(file_path)
    results = []
    for commit in commits : 
        commit['repo_id'] = repo_id
        results.append(commit)
    return results
    
async def main() :  
    path = f'e:/research_subagent/data/raw/COMMITS'
    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]    
    temp_results = await AsyncTaskRunner.run(load_data, task_args) 

    results = []
    [ results.extend(r) for r in temp_results]

    try : 
        col_commits.insert_many(results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() ) 