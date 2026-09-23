import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_contributor_last_urls, col_pull_request_last_urls
from src.util.data_file_rw import DataFileReader
import re
import asyncio
from src.task.async_task_runner import AsyncTaskRunner

async def parse_data(data) : 
    n_page = None
    if data['response_status_code'] == 200 : 
        n_page = 1
        if data['last_page_url'] != 'None' : 
            mat = re.search(r'&page=[\d]+', data['last_page_url'])
            n_page = mat.group().split('=')[1]
            n_page = int(n_page)
    data['n_page'] = n_page

    return data  

async def main() : 
    # file_path = '../data/contributors_last_urls.json'
    file_path = '../data/temp_pr_last_urls.json'
    dataset = DataFileReader.from_json(file_path)
    work_args = [ [data] for data in dataset] 

    results = await AsyncTaskRunner.run(parse_data, work_args)

    # col_contributor_last_urls.insert_many(results)
    col_pull_request_last_urls.insert_many(results)

if __name__ == '__main__' : 
    asyncio.run( main() )