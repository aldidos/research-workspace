import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_exp_agent_issues
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.util.data_file_rw import DataFileReader
from src.dataset.aiAgent.db_collection import raw_dataset_path

async def load_data(file_path, category) : 
    dataset = DataFileReader.from_json(file_path)
    temp_dataset = []
    for data in dataset : 
        data['category'] = category
        temp_dataset.append(data)
    return temp_dataset
    
async def main() :  
    for n in [1,2,3,4,5,6] : 
        path = f'{raw_dataset_path}/exp_data/samples/manual_analysis/{n}'
        category = n

        task_args = [ [file_path, category] for file_path in DataFileReader.find_files(path, 'json') ]
        results = []    

        temp_results = await AsyncTaskRunner.run(load_data, task_args)      

        [ results.extend(r) for r in temp_results ]

        try : 
            col_exp_agent_issues.insert_many(results, ordered=False)
        except Exception as e : 
            print(e)

if __name__ == '__main__' : 
    asyncio.run( main() )    