import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_repo_contents
from src.util.data_file_rw import DataFileReader
from pathlib import Path
import asyncio
from src.task.async_task_runner import AsyncTaskRunner

async def load_data(file_path) : 
    contents = []
    repo_id = file_path.name.split('.')[0]
    repo_id = int(repo_id)

    temp_contents = DataFileReader.from_json(file_path)
    for c in temp_contents : 
        c['repo_id'] = repo_id
        contents.append(c)
    
    return contents

async def main() : 
    task_dataset = Path('../data/raw/REPO_CONTENTS').glob('**/*.json')
    task_args = [ [file_path] for file_path in task_dataset]

    task_results = await AsyncTaskRunner.run(load_data, task_args) 
    results = []
    [ results.extend(r) for r in task_results ]

    col_repo_contents.insert_many(results)

if __name__ == '__main__' : 
    asyncio.run(main())