import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_contributing_file_features, col_contributing_files, col_pull_request_templates, col_pull_request_template_features
import asyncio
from src.task.async_task_runner import AsyncTaskRunner
from src.docs.html_doc import HtmlDoc
from src.tools.markdown_processiong import to_html_text

async def processing_data(doc) :     
# def processing_data(doc) :     
    html_doc = HtmlDoc(to_html_text(doc['text']))
    
    return { 
        # 'contributing_file_id' : doc['id'],
        'repo_id' : doc['repo_id'],
        'file_path' : doc['file_path'],
        'tag_counts' : html_doc.num_tag_categories(),
        'tags' : html_doc.get_tag_list(),
        'heading_texts' : html_doc.get_head_tags_text()
    }
    
async def main() :  
# def main() :  

    no_md_files = 2

    in_cols = [col_contributing_files, col_pull_request_templates]
    out_cols = [col_contributing_file_features, col_pull_request_template_features]

    for i in range(no_md_files) : 
    # task_args = [ [doc] for doc in col_contributing_files.find() ]
        task_args = [ [doc] for doc in in_cols[i].find() ]
        results = []    

        results = await AsyncTaskRunner.run(processing_data, task_args)      
        
        out_cols[i].insert_many(results)
        # col_contributing_file_features.insert_many(results)

if __name__ == '__main__' : 
    asyncio.run( main() )
    # main()
