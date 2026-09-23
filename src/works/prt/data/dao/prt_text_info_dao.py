import sys
sys.path.append('.')
from src.works.prt.data.db_collection import col_prt_text_info
from src.database.agg_stages import match, lookup, unwind, project
from src.database.exp_stat import And, gte, expr, size
import pandas as pd

class PRTTextInfoDao : 

    def get_by_heading_titles_and_checklists(self) : 
        stages = [
            match(
                expr( And( [ 
                        gte( size('$heading_titles'), 1 ), 
                        gte( size('$checklist_items'), 1 ) 
                        ]) )
            ), 
            lookup('pull_request_templates', 'repo_id', 'repo_id', 'prt'),
            unwind('$prt'),
            project({
                '_id' : 0, 
                'id' : '$repo_id',
                'repo_id' : 1,
                'text' : '$prt.text'
            })
        ]

        return col_prt_text_info.aggregate(stages)
    
if __name__ == '__main__' : 
    dao = PRTTextInfoDao()
    cur = dao.get_by_heading_titles_and_checklists()
    df = pd.DataFrame(cur) 

    df.to_json('../data/exp_data/exp_prt_set.json', orient='records')
       