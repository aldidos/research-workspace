import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_prt_text_info, col_pull_request_templates
from src.docs.parser.prt_parser import PRTParser
from src.task.async_task_runner import AsyncTaskRunner
import asyncio

async def task_func(prt) : 
    prt_parser = PRTParser( prt['text'] )
    heading_titles = prt_parser.get_heading_titles()
    checklist_items = prt_parser.get_checklist_items()

    return  {
        'repo_id' : prt['repo_id'],
        'file_path' : prt['file_path'],
        'heading_titles' : heading_titles,
        'checklist_items' : checklist_items            
    }

async def main() : 
    args = [ [prt] for prt in col_pull_request_templates.find() ]
    results = await AsyncTaskRunner.run(task_func, args)
    col_prt_text_info.insert_many( results )  

if __name__ == '__main__' : 
    asyncio.run( main() )
