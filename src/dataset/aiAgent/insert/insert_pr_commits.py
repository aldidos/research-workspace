import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_pr_commits, raw_dataset_path
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader

async def load_data(file_path) : 
    repo_id = file_path.parts[-2]
    repo_id = int(repo_id)
    number = file_path.parts[-1].split('.')[0]
    number = int(number)
    dataset = DataFileReader.from_json(file_path)
    temp_dataset = []
    for data in dataset : 
        url = data['url']
        temp_urls = url.split('/')
        owner = temp_urls[4]
        repo = temp_urls[5]
        pr_url = f'https://api.github.com/repos/{owner}/{repo}/pulls/{number}'
        data['pr_url'] = pr_url
        
        data['repo_id'] = repo_id
        data['number'] = number
        temp_dataset.append(data)
    return temp_dataset
    
async def main() :  
    path = f'{raw_dataset_path}/raw/PR_COMMITS'

    task_args = [ [file_path] for file_path in DataFileReader.find_files(path, 'json') ]
    results = []    

    temp_results = await AsyncTaskRunner.run(load_data, task_args)      
    # results = ConcurTaskRunner(128).run(processing_data, task_args)  

    [ results.extend(r) for r in temp_results ]

    try : 
        col_pr_commits.insert_many(results, ordered=False)
    except Exception as e : 
        print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )    