import sys
sys.path.append('.')
from src.dataset.aiAgent.db_collection import col_exp_prs
from src.database.agg_stages import match, project, lookup
from src.database.exp_stat import expr, eq, array_element_at, get_field, date_diff, date_from_string, size, get_array_obj_field, gte

class ExpPRDao : 

    def get_dataset(self) : 
        stages = [                        
            # match({ '$expr' : { '$eq' : [ { '$size' : '$labels' }, 1]  } }),
            lookup( 'pull_requests', 'url', 'url', 'pr' ),  
            project( {
                '_id' : 0, 
                'repo_id' : 1, 
                'body' : 1, 
                # 'label' : array_element_at('$labels', 0), 
                'closed_time' : date_diff( 
                    date_from_string( get_array_obj_field('$pr', 0, 'created_at') ),
                    date_from_string( get_array_obj_field('$pr', 0, 'closed_at') ), 
                    'minute'
                    ), 
                'assignee' : get_array_obj_field('$pr', 0, 'assignee'), 
                'n_comments' : get_array_obj_field('$pr', 0, 'comments'),                 
                'n_review_comments' : get_array_obj_field('$pr', 0, 'review_comments'), 
                'n_commits' : get_array_obj_field('$pr', 0, 'commits'), 
                'n_additions' : get_array_obj_field('$pr', 0, 'additions'), 
                'n_deletions' : get_array_obj_field('$pr', 0, 'deletions'), 
                'n_changed_files' : get_array_obj_field('$pr', 0, 'changed_files') 
            } )
        ]

        return col_exp_prs.aggregate(stages)
    
expPRDao = ExpPRDao()

if __name__ == '__main__' : 
    cur = expPRDao.get_dataset()
    dataset = [ doc for doc in cur ]
    print( len(dataset))
